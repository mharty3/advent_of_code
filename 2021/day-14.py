# --- Day 14: Extended Polymerization ---
# https://adventofcode.com/2021/day/14

from collections import Counter


def parse(input_data):
    template, rules = input_data.split("\n\n")
    rules = [rule.strip().split(" -> ") for rule in rules.splitlines()]
    return template, rules


def count_adjacent_pairs(template):
    pairs = []
    for i, elem in enumerate(template[1:], start=1):
        pairs.append(template[i - 1] + elem)
    return Counter(pairs)


def insert(pair_counts, instructions):
    new_pairs = Counter()
    old_pairs = []
    for instruction in instructions:
        if instruction[0] in pair_counts:
            old_pairs.append(instruction[0])
            leading_new_pair = instruction[0][0] + instruction[1]
            trailing_new_pair = instruction[1] + instruction[0][1]
            new_pairs[leading_new_pair] += pair_counts[instruction[0]]
            new_pairs[trailing_new_pair] += pair_counts[instruction[0]]

    for pair in old_pairs:
        pair_counts[pair] = 0
    pair_counts += new_pairs

    return pair_counts


def iterate(input_data, n_steps):
    template, instructions = parse(input_data)
    pair_counts = count_adjacent_pairs(template)
    for i in range(n_steps):
        pair_counts = insert(pair_counts, instructions)
    return pair_counts


def solve(input_data, n):
    """This is not perfect, but it apparently gets with in 1 of the correct answer"""
    polymer_pair_counts = iterate(input_data, n)

    element_counter = dict()
    for k, v in polymer_pair_counts.items():
        for elem in list(k):
            if elem in element_counter:
                element_counter[elem] += v
            else:
                element_counter[elem] = v
    c = Counter(element_counter)
    mc = c.most_common()

    return round((mc[0][1] - mc[-1][1]) / 2)

# I tried the above approach first, but had trouble getting it to work
# so I implemented the brute force approach. But of course, it doesn't work 
# on part 2

def insert_brute_force(template, instructions):
    added = 0
    to_add = []
    for i, s in enumerate(template[1:], start=1):
        for (pair, elem) in instructions:
            if template[i - 1] + s == pair:
                added += 1
                to_add.append((i + added - 1, elem))

    l = list(template)
    for i, elem in to_add:
        l.insert(i, elem)

    return "".join(l)


def iterate_brute_force(input_data, n_steps):

    template, instructions = parse(input_data)
    for i in range(n_steps):

        template = insert_brute_force(template, instructions)
    return template


def solve_brute_force(input_data, n):
    polymer = iterate_brute_force(input_data, n)
    mc = Counter(polymer).most_common()
    return mc[0][1] - mc[-1][1]


if __name__ == "__main__":
    from aocd.models import Puzzle

    test_data = """NNCB

    CH -> B
    HH -> N
    CB -> H
    NH -> C
    HB -> C
    HC -> B
    HN -> C
    NN -> C
    BH -> H
    NC -> B
    NB -> B
    BN -> B
    BB -> N
    BC -> B
    CC -> N
    CN -> C"""

    assert iterate_brute_force(test_data, 1) == "NCNBCHB"
    assert iterate_brute_force(test_data, 2) == "NBCCNBBBCBHCB"

    assert iterate(test_data, 1) == count_adjacent_pairs("NCNBCHB")
    assert iterate(test_data, 2) == count_adjacent_pairs("NBCCNBBBCBHCB")
    assert iterate(test_data, 3) == count_adjacent_pairs("NBBBCNCCNBBNBNBBCHBHHBCHB")
    assert iterate(test_data, 4) == count_adjacent_pairs(
        "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"
    )

    assert solve(test_data, 10) == 1588
    assert solve_brute_force(test_data, 10) == 1588

    puzzle = Puzzle(2021, 14)

    answer_1 = solve(puzzle.input_data, 10)
    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve(puzzle.input_data, 40)
    print(answer_2)
    puzzle.answer_b = answer_2
