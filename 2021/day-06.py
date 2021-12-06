# --- Day 6: Lanternfish ---
# https://adventofcode.com/2021/day/6

from collections import Counter


def parse(input):
    return Counter(int(n) for n in input.split(","))


def age_population(population, days):
    prev_pop = population
    for _ in range(days):
        new_pop = Counter({k - 1: v for k, v in prev_pop.items() if k > 0})
        new_pop[6] += prev_pop[0]
        new_pop[8] += prev_pop[0]
        prev_pop = new_pop

    return new_pop


def solve(input, days):
    new_pop = age_population(parse(input), days)
    return sum(new_pop.values())


if __name__ == "__main__":
    from aocd.models import Puzzle

    test_data = "3,4,3,1,2"
    assert solve(test_data, 80) == 5934
    assert solve(test_data, 256) == 26984457539

    puzzle = Puzzle(2021, 6)

    answer_1 = solve(puzzle.input_data, 80)
    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve(puzzle.input_data, 256)
    print(answer_2)
    puzzle.answer_b = answer_2
