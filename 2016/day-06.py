# --- Day 6: Signals and Noise ---
from typing import List
from collections import Counter

def parse(input_data: str) -> List[str]:
    rows = input_data.split('\n')
    columns = [list(i) for i in zip(*rows)]
    columns = [''.join(c) for c in columns]
    return columns


def solve1(input_data):
    columns = parse(input_data)
    commons = [Counter(c).most_common()[0][0] for c in columns]
    return ''.join(commons)


def solve2(input_data):
    columns = parse(input_data)
    commons = [Counter(c).most_common()[-1][0] for c in columns]
    return ''.join(commons)


test_data = """eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar"""

assert solve1(test_data) == 'easter'
assert solve2(test_data) == 'advent'

if __name__ == '__main__':
    from aocd.models import Puzzle
    puzzle = Puzzle(2016, 6)
    answer_1 = solve1(puzzle.input_data)

    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve2(puzzle.input_data)
    print(answer_2)
    puzzle.answer_b = answer_2