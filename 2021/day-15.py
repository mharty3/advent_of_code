# --- Day 15: Chiton ---
# https://adventofcode.com/2021/day/15


from typing import Tuple, Dict, List, Iterator, Optional
import heapq
from copy import deepcopy

# grid classes, priority queue, and dijkstra search come from
# https://www.redblobgames.com/pathfinding/a-star/implementation.html

GridLocation = Tuple[int, int]


class SquareGrid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def in_bounds(self, id: GridLocation) -> bool:
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def neighbors(self, id: GridLocation) -> Iterator[GridLocation]:
        (x, y) = id
        neighbors = [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]  # E W N S
        # see "Ugly paths" section for an explanation:
        if (x + y) % 2 == 0:
            neighbors.reverse()  # S N W E
        results = filter(self.in_bounds, neighbors)
        return results


class GridWithWeights(SquareGrid):
    def __init__(self, width: int, height: int, weights: Dict[GridLocation, float]):
        super().__init__(width, height)
        self.weights = weights

    def cost(self, from_node: GridLocation, to_node: GridLocation) -> float:
        return self.weights.get(to_node, 1)


class PriorityQueue:
    def __init__(self):
        self.elements: List[Tuple[float, T]] = []

    def empty(self) -> bool:
        return not self.elements

    def put(self, item: GridLocation, priority: float):
        heapq.heappush(self.elements, (priority, item))

    def get(self) -> GridLocation:
        return heapq.heappop(self.elements)[1]


def dijkstra_search(graph: GridWithWeights, start: GridLocation, goal: GridLocation):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from: Dict[GridLocation, Optional[GridLocation]] = {}
    cost_so_far: Dict[GridLocation, float] = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current: GridLocation = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far


def parse(input_data):
    grid = [
        [int(risk) for risk in list(line.strip())] for line in input_data.splitlines()
    ]
    ny = len(grid)
    nx = len(grid[0])

    weights = dict()
    for i in range(ny):
        for j in range(nx):
            weights[(j, i)] = grid[i][j]

    return grid, nx, ny, weights


def solve1(input_data):
    _, nx, ny, weights = parse(input_data)
    g = GridWithWeights(nx, ny, weights)
    came_from, cost_so_far = dijkstra_search(g, (0, 0), (nx - 1, ny - 1))
    return cost_so_far[(nx - 1, ny - 1)]


def construct_full_grid(input_data):
    """this one is a bit rough around the edges"""
    grid, nx, ny, weights = parse(input_data)
    full_grid = grid.copy()
    for i in range(4):
        for row in grid:
            full_grid.append(
                [
                    (val + (i + 1)) if (val + (i + 1)) <= 9 else (val + (i + 1)) - 9
                    for val in row
                ]
            )

    full_full_grid = deepcopy(full_grid)
    for i, row in enumerate(full_grid):
        for n in range(4):
            for col in row:
                full_full_grid[i].append(
                    (col + (n + 1)) if (col + (n + 1)) <= 9 else (col + (n + 1)) - 9
                )

    ffg_str = "\n".join(["".join(map(str, row)) for row in full_full_grid])
    return ffg_str


def solve2(input_data):
    return solve1(construct_full_grid(input_data))


if __name__ == "__main__":
    from aocd.models import Puzzle

    puzzle = Puzzle(2021, 15)

    test_data = """1163751742
    1381373672
    2136511328
    3694931569
    7463417111
    1319128137
    1359912421
    3125421639
    1293138521
    2311944581"""

    assert solve1(test_data) == 40
    assert solve2(test_data) == 315

    answer_1 = solve1(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve2(puzzle.input_data)
    print(answer_2)
    puzzle.answer_b = answer_2
