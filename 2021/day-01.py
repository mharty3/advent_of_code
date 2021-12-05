# --- Day 1: Sonar Sweep ---
# https://adventofcode.com/2021/day/1

def parse(input_data):
    sonar = [int(s) for s in input_data.split('\n')]
    return sonar


def solve1(input_data):
    sonar = parse(input_data)
    deltas = [x - x_prev for x, x_prev in zip(sonar[1:], sonar)]
    return sum([d > 0 for d in deltas])


def solve2(input_data):
    sonar = parse(input_data)
    rolling_window = [sum(window) for window in zip(sonar, sonar[1:], sonar[2:])]
    deltas = [x - x_next for x, x_next in zip(rolling_window[1:], rolling_window[:-1])]
    return sum([d > 0 for d in deltas])


if __name__ == '__main__':

    test_data = """199
200
208
210
200
207
240
269
260
263"""

    assert solve1(test_data) == 7
    assert solve2(test_data) == 5

    from aocd.models import Puzzle
    puzzle = Puzzle(2021, 1)
    answer_1 = solve1(puzzle.input_data)

    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve2(puzzle.input_data)
    puzzle.answer_b = answer_2

