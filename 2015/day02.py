from typing import List
from itertools import combinations

def parse(input_data: str) -> List[List[int]]:
    return [sorted([int(d) for d in row.split('x')]) for row in input_data.split()]


def solve1(input_data):
    data = parse(input_data)
    total = 0
    for d in data:
        subtotal = d[0] * d[1]
        for c in combinations(d, 2):
            subtotal += 2 * c[0] * c[1]
        total += subtotal
    return total


def solve2(input_data):
    data = parse(input_data)
    total = 0
    for d in data:
        total += (d[0] * d[1] * d[2]) + (2 * d[0]) + (2 * d[1])
    return total




if __name__ == '__main__':

    from aocd.models import Puzzle
    
    puzzle = Puzzle(2015, 2)
    answer_1 = solve1(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve2
    print(answer_2)
    puzzle.answer_b = answer_2 
    