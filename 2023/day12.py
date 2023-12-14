from aocd.models import Puzzle
puzzle = Puzzle(2023, 12)
input_data = puzzle.input_data
from itertools import product


def parse(input_data):
    data = list()
    for line in input_data.splitlines():
        config, groups = line.split()
        data.append([list(config), [int(n) for n in groups.split(',')]])
    return data


def find_contiguous_blocks(config):
    blocks = []
    count = 0
    for val in config:
        if val == '.':
            if count != 0:
                blocks.append(count)
            count = 0
        if val == '#':
            count += 1
    if count:
        blocks.append(count)
    return blocks


def count_possibilities(config, blocks):
    c = '?'
    q_idx = [pos for pos, char in enumerate(config) if char == c]

    l = product(['.', '#'], repeat=len(q_idx))

    count = 0
    for option in l:
        filled_config = config.copy()
        for val, idx in zip(option, q_idx):
            filled_config[idx] = val
        if find_contiguous_blocks(filled_config) == blocks:
            count += 1
    return count


def solve1(input_data):
    total = 0
    data = parse(input_data)
    for config, blocks in data:
        total += count_possibilities(config, blocks)
    return total


def solve2(input_data):
    """nope"""
    pass
