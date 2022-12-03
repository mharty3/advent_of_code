import string

def parse(input_data):
    backpacks_raw = input_data.strip().splitlines()
    backpacks = []
    for backpack in backpacks_raw:
        backpack = backpack.strip()
        size = len(backpack)
        compartment_1 = backpack[:size//2]
        compartment_2 = backpack[size//2:]
        backpacks.append((compartment_1, compartment_2))
    return backpacks


def priority(item):
    priorities = {k: v for (k, v) in zip(string.ascii_letters, range(1, 53))}
    return priorities[item]


def solve1(input_data):
    backpacks = parse(input_data)
    return sum( [priority((set(c1) & set(c2)).pop()) for (c1, c2) in backpacks])


def solve2(input_data):
    backpacks = parse(input_data)
    backpacks = [c1 + c2 for (c1 , c2) in backpacks] # recombine compartments
    total = 0
    for i, bp in enumerate(backpacks[::3]):
        i = 3 * i
        bp_2 = backpacks[i + 1]
        bp_3 = backpacks[i + 2]
        badge = set(bp) & set(bp_2) & set(bp_3)
        total += priority(badge.pop()) 
    return total



if __name__ == '__main__':

    test_data = """vJrwpWtwJgWrhcsFMMfFFhFp
    jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
    PmmdzqPrVvPwwTWBwg
    wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
    ttgJtRGJQctTZtZT
    CrZsJsPPZsGzwwsLwLmpwMDw
    """

    assert solve1(test_data) == 157
    assert solve2(test_data) == 70

    from aocd.models import Puzzle
    puzzle = Puzzle(2022, 3)
    answer_1 = solve1(puzzle.input_data)

    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve2(puzzle.input_data)
    puzzle.answer_b = answer_2
    print(answer_2)





