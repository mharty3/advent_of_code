# --- Day 3: Binary Diagnostic ---
# https://adventofcode.com/2021/day/3

import re
from collections import Counter


def solve1(input_data):
    bit_size = len(input_data.strip().split("\n")[0])
    chars = re.sub(r"\s", "", input_data)  # remove all whitespace

    gamma_rate = ""
    for i in range(bit_size):  # get most common value in each bit
        column = chars[i::bit_size]
        gamma_rate += Counter(column).most_common()[0][0]

    gamma = int(gamma_rate, base=2)  # convert from binary
    # unsigned bitwise logical not. see: https://realpython.com/python-bitwise-operators/
    epsilon = ~gamma & int("1" * bit_size, 2)

    return gamma * epsilon


def common_bit(numbers, bit_location, most_common=True):
    bit_size = len(numbers[0])
    chars = "".join(numbers)

    column = chars[bit_location::bit_size]
    c = Counter(column)

    if c["1"] == c["0"]:  # account for ties
        if most_common:
            return "1"
        else:
            return "0"
    else:
        if most_common:
            return c.most_common()[0][0]
        else:
            return c.most_common()[1][0]


def air_quality(input_data, oxygen=True):
    numbers = [n.strip() for n in input_data.strip().split("\n")]
    bit_location = 0
    while len(numbers) > 1:
        most_common = common_bit(numbers, bit_location, oxygen)
        numbers = [number for number in numbers if number[bit_location] == most_common]
        bit_location += 1

    return int(numbers[0], base=2)


def solve2(input_data):
    return air_quality(input_data, oxygen=True) * air_quality(input_data, oxygen=False)


if __name__ == "__main__":
    from aocd.models import Puzzle

    puzzle = Puzzle(2021, 3)

    test_data = """
                00100
                11110
                10110
                10111
                10101
                01111
                00111
                11100
                10000
                11001
                00010
                01010
                """

    assert solve1(test_data) == 198

    answer_1 = solve1(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve2(puzzle.input_data)
    print(answer_2)
    puzzle.answer_b = answer_2
