# --- Day 3: Squares With Three Sides ---
# https://adventofcode.com/2016/day/3

from typing import NamedTuple, List

class Triangle(NamedTuple):
    sides: List[int]

    def is_valid(self) -> bool:
        return self.sides[0] + self.sides[1] > self.sides[2]

    @staticmethod
    def from_line(line):
        sides = line.strip().split()
        sides = sorted([int(side) for side in sides])
        return Triangle(sides)

    
def solve1(input_data):
    lines = input_data.strip().split('\n')
    triangles = [Triangle.from_line(line) for line in lines]
    valids = [t.is_valid() for t in triangles]
    return sum(valids)


def solve2(input_data):
    l = input_data.split()[::3] + input_data.split()[1::3] + input_data.split()[2::3]
    l = [int(s) for s in l]
    triangles = []
    for i, side in enumerate(l):
        if i % 3 == 0:
            s1 = side
            s2 = l[i + 1]
            s3 = l[i + 2]
            sides = sorted([s1, s2, s3])
            triangles.append(Triangle(sides))
    return sum([t.is_valid() for t in triangles])

test_data = """101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603"""

if __name__ == '__main__':
    from aocd.models import Puzzle
    puzzle = Puzzle(2016, 3)
    answer_1 = solve1(puzzle.input_data)

    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve2(puzzle.input_data)
    puzzle.answer_b = answer_2
