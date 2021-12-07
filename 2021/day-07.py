from scipy.optimize import minimize_scalar


def parse(input_data):
    return [int(n) for n in input_data.split(",")]


def solve1(input_data):
    def sum_travel_distances(x):
        return sum([abs(n - x) for n in parse(input_data)])

    res = minimize_scalar(sum_travel_distances)
    return int(round(res["fun"]))


if __name__ == "__main__":
    from aocd.models import Puzzle

    test_data = "16,1,2,0,4,2,7,1,2,14"
    assert solve1(test_data) == 37

    puzzle = Puzzle(2021, 7)

    answer_1 = solve1(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1
