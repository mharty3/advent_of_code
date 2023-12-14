import numpy as np
from aocd.models import Puzzle
puzzle = Puzzle(2023, 14)


def solve1(input_data):
    data = list(zip(*[list(r) for r in input_data.splitlines()]))
    rock_indices = []
    for col in data:
        next_open_space = 0
        for i, val in enumerate(col):
            if val == 'O':
                rock_indices.append(len(col) - next_open_space)
                next_open_space += 1
            elif val == '#':
                next_open_space = i + 1

    return sum(rock_indices)


input_data = puzzle.input_data
puzzle.answer_a = solve1(input_data)
# puzzle.answer_b = solve(input_data, smudges=1)
