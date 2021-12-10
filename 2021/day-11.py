# --- Day 11: Dumbo Octopus ---
# https://adventofcode.com/2021/day/11

from typing import Iterator, Tuple
from itertools import product


class Octopuses:
    def __init__(self, input_data: str) -> None:
        self.energy_map = [
            [int(val) for val in row.strip()] for row in input_data.splitlines()
        ]
        self.nr = len(self.energy_map)
        self.nc = len(self.energy_map[0])
        self.flash_count = 0

    def neighbors(self, r: int, c: int) -> Iterator[Tuple[int, int]]:
        for dr, dc in product([-1, 0, 1], [-1, 0, 1]):
            if (dr, dc) == (0, 0):
                continue
            if 0 <= r + dr < self.nr and 0 <= c + dc < self.nc:
                yield r + dr, c + dc

    def step(self):
        # increment all octopuses by one
        self.energy_map = [[val + 1 for val in row] for row in self.energy_map]

        # let them flash
        flashed = set()
        # while any octopuses are > 9
        while any([any([val > 9 for val in row]) for row in self.energy_map]):
            for r, c in product(range(self.nr), range(self.nc)):
                if self.energy_map[r][c] > 9 and (r, c) not in flashed:
                    flashed.add((r, c))
                    self.energy_map[r][c] = 0
                    # increment the neighbors
                    for r_, c_ in self.neighbors(r, c):
                        self.energy_map[r_][c_] += 1

        # reset all octopuses that flashed to 0
        for r, c in flashed:
            self.energy_map[r][c] = 0

        # count flashes
        self.flash_count += len(flashed)

    def simultaneous_flash(self) -> bool:
        return all([all([val == 0 for val in row]) for row in self.energy_map])


def solve1(input_data):
    o = Octopuses(input_data)
    for i in range(100):
        o.step()
    return o.flash_count


def solve2(input_data):
    o = Octopuses(input_data)
    step_count = 0
    while not o.simultaneous_flash():
        o.step()
        step_count += 1
    return step_count


if __name__ == "__main__":
    from aocd.models import Puzzle

    test_data = """5483143223
    2745854711
    5264556173
    6141336146
    6357385478
    4167524645
    2176841721
    6882881134
    4846848554
    5283751526"""

    assert solve1(test_data) == 1656
    assert solve2(test_data) == 195
    puzzle = Puzzle(2021, 11)

    answer_1 = solve1(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve2(puzzle.input_data)
    print(answer_2)
    puzzle.answer_b = answer_2
