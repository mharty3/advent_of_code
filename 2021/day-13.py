# --- Day 13: Transparent Origami ---
# https://adventofcode.com/2021/day/13

import re


def parse(input_data):
    points, instructions = input_data.split("\n\n")
    points = [list(map(int, point.split(","))) for point in points.splitlines()]

    instructions = [
        instruction.split()[-1].split("=") for instruction in instructions.splitlines()
    ]
    instructions = [(direction, int(n)) for direction, n in instructions]

    return points, instructions


def fold(point, instruction):
    if instruction[0] == "y":
        axis_num = 1
    else:
        axis_num = 0

    if point[axis_num] > instruction[1]:
        overage = point[axis_num] - instruction[1]
        point[axis_num] = instruction[1] - overage

    return point


def fold_points(points, instruction):
    new_points = []
    for point in points:
        new_point = fold(point, instruction)
        if new_point not in new_points:
            new_points.append(new_point)
    return new_points


def solve1(input_data):
    points, instructions = parse(input_data)
    new_points = fold_points(points, instructions[0])
    return len(new_points)


def fold_part_2(input_data):
    points, instructions = parse(input_data)
    new_points = points
    for instruction in instructions:
        new_points = fold_points(new_points, instruction)
    return new_points


def plot_points(points):
    xs, ys = zip(*points)

    xmax = max(xs)
    ymax = max(ys)

    for y in range(ymax + 1):
        for x in range(xmax + 1):
            if [x, y] in points:
                print("#", end="")
            else:
                print(" ", end="")
        print("\n", end="")


def solve2(input_data):
    points = fold_part_2(input_data)
    return plot_points(points)


if __name__ == "__main__":
    from aocd.models import Puzzle

    test_data = """6,10
    0,14
    9,10
    0,3
    10,4
    4,11
    6,0
    6,12
    4,1
    0,13
    10,12
    3,4
    3,0
    8,4
    1,10
    2,14
    8,10
    9,0

    fold along y=7
    fold along x=5"""

    assert solve1(test_data) == 17

    puzzle = Puzzle(2021, 13)

    answer_1 = solve1(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1

    solve2(puzzle.input_data)
    puzzle.answer_b = "BLKJRBAG"

"""
###  #    #  #   ## ###  ###   ##   ## 
#  # #    # #     # #  # #  # #  # #  #
###  #    ##      # #  # ###  #  # #   
#  # #    # #     # ###  #  # #### # ##
#  # #    # #  #  # # #  #  # #  # #  #
###  #### #  #  ##  #  # ###  #  #  ###
"""
