from aocd.models import Puzzle
import numpy as np
import itertools

from typing import Tuple, Dict, List, Iterator, Optional, TypeVar

from aocd.models import Puzzle
puzzle = Puzzle(2023, 23)
input_data = puzzle.input_data


GridLocation = Tuple[int, int]
Location = TypeVar('Location')

class SquareGrid:
    def __init__(self, width: int, height: int, walls: list[GridLocation], start: GridLocation, end: GridLocation, grid):
        self.width = width
        self.height = height
        self.walls = walls
        self.start = start
        self.end = end
        self.grid = grid
    
    def in_bounds(self, id: GridLocation) -> bool:
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height
    
    def passable(self, id: GridLocation) -> bool:
        return id not in self.walls
    
    def neighbors(self, id: GridLocation) -> Iterator[GridLocation]:
        x, y = id
        neighbors = [(x+1, y), (x-1, y), (x, y-1), (x, y+1)] # E W N S

        arrows = {'>': (x+1, y),
                  '<': (x-1, y),
                  'v': (x, y+1),
                  '^': (x, y-1)}
        
        if self.grid[y][x] in arrows:
            neighbors = [arrows[self.grid[y][x]]]
        
        results = filter(self.in_bounds, neighbors)
        results = filter(self.passable, results)
        return list(results)
    

    def to_dict(self):
        stack = []
        d = dict()
        stack.append(self.start)
        d[self.start] = self.neighbors(self.start)

        while stack:
            node = stack.pop()
            for neighbor in self.neighbors(node):
                if neighbor not in d.keys():
                    stack.append(neighbor)
                    d[neighbor] = [n for n in self.neighbors(neighbor)]# if n not in d.keys()]

        return d
    
    def junctions(self):
        xs = range(self.width)
        ys = range(self.height)
        node_intersections = dict()

        for id in itertools.product(xs, ys):
            if id not in self.walls:
                if len(self.neighbors(id)) > 2:
                    node_intersections[id] = self.neighbors(id)

        return node_intersections

    @staticmethod
    def parse(input_data):
        grid = [
            list(line) for line in input_data.splitlines()
        ]

        ny = len(grid)
        nx = len(grid[0])

        walls = []
        for r, row in enumerate(grid):
            # print(row)
            for c, val in enumerate(row):
                if val == '#':
                    walls.append((c, r))
                if r == 0 and val =='.':
                    start = (c, r)
                if r == max(range(ny)) and val == '.': 
                    end = (c, r)

        return SquareGrid(nx, ny, walls, start, end, grid)
    

import networkx as nx
grid = SquareGrid.parse(input_data)
d = grid.to_dict()

G = nx.DiGraph(d)
# for p in nx.all_simple_paths(G, grid.start, grid.end):
#     print(len(p))

ml = max([len(p) for p in nx.all_simple_paths(G, grid.start, grid.end)])
answer_a = ml - 1

