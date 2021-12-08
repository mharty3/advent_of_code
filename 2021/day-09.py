# --- Day 9: Smoke Basin ---
# https://adventofcode.com/2021/day/9

import numpy as np
from scipy.ndimage.measurements import label


def parse(input_data):
    # return list of list of integers
    # adding a pad of nines around the edges
    data = input_data.split("\n")
    data = ["9" + row.strip() + "9" for row in data]
    top_and_bottom_pad = "9" * len(data[0])
    data.insert(0, top_and_bottom_pad)
    data.append(top_and_bottom_pad)
    return [list(map(int, list(row))) for row in data]


def solve1(input_data):
    data = parse(input_data)
    lows = []
    # iterate rows and columns ignoring the pad
    for i, row in enumerate(data[1:-1], start=1):
        for j, val in enumerate(row[1:-1], start=1):
            # look up, down, left, right
            offsets = [
                data[i][j - 1],  # left
                data[i][j + 1],  # right
                data[i - 1][j],  # down
                data[i + 1][j],  # up
            ]
            if val < min(offsets):
                lows.append(val)

    return sum(lows) + len(lows)


def solve2(input_data):
    """use scipy.ndimage"""

    data_array = np.array(parse(input_data))

    # boundaries of objects must be 0 for scipy label
    # convert 0 in data to -1 and 9 to 0
    data_array[data_array == 0] = -1
    data_array[data_array == 9] = 0

    labels, _ = label(data_array)

    _, counts = np.unique(labels, return_counts=True)
    counts[1:].sort()

    return counts[-3:].prod()


if __name__ == "__main__":
    from aocd.models import Puzzle

    test_data = """2199943210
    3987894921
    9856789892
    8767896789
    9899965678"""

    assert solve1(test_data) == 15
    assert solve2(test_data) == 1134
    puzzle = Puzzle(2021, 9)

    answer_1 = solve1(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve2(puzzle.input_data)
    print(answer_2)
    puzzle.answer_b = answer_2
