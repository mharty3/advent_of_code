from itertools import combinations


def parse(input_data):
    stream = input_data.strip().split("\n")
    return [int(s.strip()) for s in stream]


def solve1(input_data, preamble_size):
    stream = parse(input_data)
    for index, number in enumerate(stream):
        if index > preamble_size:
            cs = combinations(stream[index - preamble_size : index], 2)
            if number not in set(map(sum, cs)):
                return number


def solve2(input_data, preamble_size):
    invalid_number = solve1(input_data, preamble_size)
    stream = parse(input_data)

    for run_length in range(2, len(stream)):
        for i, _ in enumerate(stream):
            run = stream[i : i + run_length]
            if sum(run) == invalid_number:
                return sum([min(run), max(run)])


if __name__ == "__main__":
    from aocd.models import Puzzle

    test_data = """35
    20
    15
    25
    47
    40
    62
    55
    65
    95
    102
    117
    150
    182
    127
    219
    299
    277
    309
    576
    """

    assert solve1(test_data, 5) == 127
    assert solve2(test_data, 5) == 62

    puz9 = Puzzle(2020, 9)
    data = puz9.input_data
    puz9.answer_a = solve1(data, 25)
    puz9.answer_b = solve2(data, 25)
