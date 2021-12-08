# --- Day 7: The Treachery of Whales ---
# https://adventofcode.com/2021/day/7

# I solved this with some hints to look at different measures of central tendencies
# To see my solution to part one using scipy.optimize.minimize scalar, check the file history


from statistics import mean, median


def parse(input_data):
    return [int(n) for n in input_data.split(",")]


def sum_travel_distances(x, input_data):
    return int(sum([abs(n - x) for n in parse(input_data)]))


def fuel_part2(x, input_data):
    dists = [abs(n - x) for n in parse(input_data)]
    fuels = [n + (n * (n - 1) / 2) for n in dists]
    return round(sum(fuels))


def solve1(input_data):
    x = median(parse(input_data))
    return sum_travel_distances(x, input_data)


def solve2(input_data):
    x = round(mean(parse(input_data)))
    search_area = [fuel_part2(n, input_data) for n in range(x - 5, x + 5) if x > 0]
    return min(search_area)


if __name__ == "__main__":
    from aocd.models import Puzzle

    test_data = "16,1,2,0,4,2,7,1,2,14"
    assert solve1(test_data) == 37
    assert solve2(test_data) == 168

    puzzle = Puzzle(2021, 7)

    answer_1 = solve1(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve2(puzzle.input_data)
    print(answer_2)
    puzzle.answer_b = answer_2
