#--- Day 2: Bathroom Security ---
from typing import List


def parse(input_data: str) -> List[List[str]]:
    lines = input_data.strip().split()
    directions = [list(line) for line in lines]
    return directions


def move1(x, y, direction):
    if direction == 'U':
        y -= 1
    elif direction == 'D':
        y += 1
    elif direction == 'L':
        x -= 1
    elif direction == 'R':
        x += 1

    if y < 0: y = 0
    if y > 2: y = 2
    if x < 0: x = 0
    if x > 2: x = 2

    return x, y

def move2(x, y, direction, keypad):
    last_x = x
    last_y = y

    if direction == 'U':
        y -= 1
    elif direction == 'D':
        y += 1
    elif direction == 'L':
        x -= 1
    elif direction == 'R':
        x += 1


    if keypad[x][y] == '-':
        return last_x, last_y
    else:
        return x, y


def solve1(input_data: str) -> str:
    keypad = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

    x = 1
    y = 1

    keycode = []
    for line in parse(input_data):
        for direction in line:
            x, y = move1(x, y, direction)
        keycode.append(str(keypad[y][x]))
    return ''.join(keycode)


def solve2(input_data):
    keypad = [['-', '-', '-', '-', '-', '-', '-'],
              ['-', '-', '-', '1', '-', '-', '-'],
              ['-', '-', '2', '3', '4', '-', '-'],
              ['-', '5', '6', '7', '8', '9', '-'],
              ['-', '-', 'A', 'B', 'C', '-', '-'],
              ['-', '-', '-', 'D', '-', '-', '-'],
              ['-', '-', '-', '-', '-', '-', '-']]

    x = 1
    y = 3

    keycode = []
    for line in parse(input_data):
        for direction in line:
            x, y = move2(x, y, direction, keypad)
        keycode.append(keypad[y][x])
    return ''.join(keycode)

test_data = """ULL
RRDDD
LURDL
UUUUD"""

assert solve1(test_data) == '1985'
assert solve2(test_data) == '5DB3'

if __name__ == '__main__':
    from aocd.models import Puzzle
    puzzle = Puzzle(2016, 2)
    answer_1 = solve1(puzzle.input_data)

    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve2(puzzle.input_data)
    puzzle.answer_b = answer_2
