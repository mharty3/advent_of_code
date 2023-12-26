import re
import json

def solve1(input_data):
    pattern = '-*\d+'
    m = re.findall(pattern, input_data)
    return sum([int(d) for d in m])


def recursive_unpacker(input, pre=None):
    # modified from https://stackoverflow.com/a/12507546
    pre = pre[:] if pre else []
    if isinstance(input, dict) and 'red' not in input.values():
        for key, value in input.items():
            if isinstance(value, dict):
                for d in recursive_unpacker(value, pre + [key]):
                    yield d
            elif isinstance(value, list) or isinstance(value, tuple):
                for v in value:
                    for d in recursive_unpacker(v, pre + [key]):
                        yield d
            else:
                yield pre + [key, value]
    elif isinstance(input, list):
        for value in input:
            for d in recursive_unpacker(value, pre):
                yield d
    else:
        yield pre + [input]


def solve2(input_data):
    inputs = json.loads(input_data)
    total = 0
    for i in recursive_unpacker(inputs):
        if not 'red' in str(i):
            for j in i:
                if isinstance(j, int):
                    total += j
    return total


if __name__ == '__main__':
    from aocd.models import Puzzle

    puzzle = Puzzle(2015, 12)
    input_data = puzzle.input_data
    answer_1 = solve1(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve2(input_data)
    print(answer_2)
    puzzle.answer_b = answer_2 


