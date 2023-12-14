import numpy as np
from aocd.models import Puzzle
puzzle = Puzzle(2023, 13)


def parse(input_data):
    data = []
    for map_ in input_data.split('\n\n'):
        data.append([list(row) for row in map_.splitlines()])

    return data


def reflect(row, smudges=0):
    non_matches_count = []
    for i, _ in enumerate(row):
        left = row[i-1::-1]
        right = row[i:]

        smudges = len([(l, r) for l, r in zip(left, right) if l != r])
        non_matches_count.append(smudges)

    return non_matches_count


def score_map(map_, smudges=0):
    a = []
    for row in map_:
        a.append(reflect(row))
    A = np.array(a)

    if np.any(A.sum(axis=0)==smudges):
        c = (A.sum(axis=0)==smudges).nonzero()[0][0]
        return c

    else:
        a = []
        for row in zip(*map_):
            a.append(reflect(row))
        A = np.array(a)
        r = (A.sum(axis=0)==smudges).nonzero()[0][0]
        return r * 100


def solve(input_data, smudges=0):
    return sum([score_map(m, smudges) for m in parse(input_data)])


input_data = puzzle.input_data
puzzle.answer_a = solve(input_data)
puzzle.answer_b = solve(input_data, smudges=1)
