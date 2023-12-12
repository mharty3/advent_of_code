import numpy as np
from scipy.spatial import distance_matrix


def solve(input_data, n=2):
    data = input_data.splitlines()

    A = np.zeros((len(data), len(data[0])))
    for r, row in enumerate(data):
        for c, val in enumerate(row):
            if val == '#':
                A[r, c] = 1

    rows_to_add = (A.sum(axis=1) == 0).nonzero()[0]
    cols_to_add = ((A.sum(axis=0) == 0).nonzero())[0]

    pts = np.transpose(A.nonzero())
    expanded_points = []
    for r, c in pts:
        r += (n - 1) * len([x for x in rows_to_add if x < r]) # which is better?
        c += (n - 1) * len(list(filter(lambda x: x < c, cols_to_add))) # comprehension or filter?
        expanded_points.append((r, c))

    D = distance_matrix(expanded_points, expanded_points, p=1)
    return np.triu(D).sum()


if __name__ == "__main__":
    from aocd.models import Puzzle

    test_data = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""
    puzzle = Puzzle(2023, 11)
    assert solve(test_data) == 374

    answer_1 = solve(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve(puzzle.input_data, 1_000_000)
    assert answer_2 == 447744640566
    print(answer_2)
    puzzle.answer_b = answer_2

