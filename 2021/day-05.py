from collections import Counter
from typing import List, NamedTuple


class Line(NamedTuple):
    x1: int
    y1: int
    x2: int
    y2: int

    def is_horizontal(self):
        return self.y1 == self.y2

    def is_vertical(self):
        return self.x1 == self.x2

    def points_covered(self):
        if self.is_vertical():
            ys = range(min(self.y1, self.y2), max(self.y1, self.y2) + 1)
            x = self.x1
            return [(x, y) for y in ys]

        if self.is_horizontal():
            xs = range(min(self.x1, self.x2), max(self.x1, self.x2) + 1)
            y = self.y1
            return [(x, y) for x in xs]

        else:
            ys = range(min(self.y1, self.y2), max(self.y1, self.y2) + 1)
            if self.y1 > self.y2:
                ys = reversed(ys)
            xs = range(min(self.x1, self.x2), max(self.x1, self.x2) + 1)
            if self.x1 > self.x2:
                xs = reversed(xs)
            return [(x, y) for x, y in zip(xs, ys)]


def parse(input: str) -> List[Line]:
    coords = input.splitlines()
    coords = [coord.replace(" -> ", ",") for coord in coords]
    coords = [[int(c) for c in coord.split(",")] for coord in coords]
    lines = [Line(*coord) for coord in coords]

    return lines


def solve(input_data, part1=True):
    lines = parse(input_data)

    if part1:
        lines = [
            test_line
            for test_line in lines
            if test_line.is_horizontal() or test_line.is_vertical()
        ]

    pts_covered = []
    for line in lines:
        pts_covered.extend(line.points_covered())

    pt_counts = Counter(pts_covered)

    return sum([c >= 2 for c in pt_counts.values()])


if __name__ == "__main__":
    from aocd.models import Puzzle

    test_data = """0,9 -> 5,9
    8,0 -> 0,8
    9,4 -> 3,4
    2,2 -> 2,1
    7,0 -> 7,4
    6,4 -> 2,0
    0,9 -> 2,9
    3,4 -> 1,4
    0,0 -> 8,8
    5,5 -> 8,2"""

    assert solve(test_data) == 5
    assert solve(test_data, part1=False) == 12

    puzzle = Puzzle(2021, 5)

    answer_1 = solve(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve(puzzle.input_data, part1=False)
    puzzle.answer_b = answer_2
