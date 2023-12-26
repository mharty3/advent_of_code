
from aocd.models import Puzzle
from collections import deque    
import numpy as np
from scipy.sparse import csr_matrix
import itertools
puzzle = Puzzle(2023, 21)
input_data = puzzle.input_data

from typing import Tuple,  Iterator, TypeVar
from copy import deepcopy
import numpy as np
from collections import deque

# grid classes, priority queue, and dijkstra search are adapted from
# https://www.redblobgames.com/pathfinding/a-star/implementation.html

GridLocation = Tuple[int, int]
Location = TypeVar('Location')

class SquareGrid:
    def __init__(self, width: int, height: int, walls: list[GridLocation], start: GridLocation):
        self.width = width
        self.height = height
        self.walls = walls
        self.start = start
    
    def in_bounds(self, id: GridLocation) -> bool:
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height
    
    def passable(self, id: GridLocation) -> bool:
        return id not in self.walls
    
    def neighbors(self, id: GridLocation) -> Iterator[GridLocation]:
        (x, y) = id
        neighbors = [(x+1, y), (x-1, y), (x, y-1), (x, y+1)] # E W N S
        
        results = filter(self.in_bounds, neighbors)
        results = filter(self.passable, results)
        return results
    
    def adjacency_matrix(self):
        xs = range(self.width)
        ys = range(self.height)
        node_list = []

        for id in itertools.product(xs, ys):
            if id not in self.walls:
                node_list.append(id)

        M = np.zeros((len(node_list), len(node_list)))

        for r, node in enumerate(node_list):
            for neighbor in self.neighbors(node):
                c = node_list.index(neighbor)
                M[r, c] = 1

        return csr_matrix(M), node_list


    @staticmethod
    def parse(input_data):
        grid = [
            list(line) for line in input_data.splitlines()
        ]

        ny = len(grid)
        nx = len(grid[0])

        walls = []
        for r, row in enumerate(grid):
            print(row)
            for c, val in enumerate(row):
                if val == '#':
                    walls.append((c, r))
                elif val == 'S':
                    start = (c, r)

        return SquareGrid(nx, ny, walls, start)
    

g = SquareGrid.parse(input_data)
M, keys = g.adjacency_matrix()
start_key = keys.index(g.start)

p = 64
M_copy = M.copy()

# take the power of the adjacency matrix to p. 
# The number of non zero entries in the row of the starting node is the number of nodes reachable in p steps
# https://cs.stackexchange.com/a/75900
for i in range(p - 1):
    M = M @ M_copy
answer_a = M[start_key, :].__gt__(0).sum()
