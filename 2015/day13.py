from itertools import permutations, pairwise


def parse(input):
    happinesses = dict()
    lines = input.split('\n')
    for line in lines:
        words = line.replace('.', '').split()
        person = words[0]
        neighbor = words[-1]
        direction = -1 if 'lose' in words else 1
        amount = words[3]

        if not happinesses.get(person):
            happinesses[person] = dict()

        happinesses[person][neighbor] = int(amount) * direction

    return happinesses


def tally_arrangement(arrangement, happinesses):
    pairs = list(pairwise(arrangement))
    pairs.append((arrangement[0], arrangement[-1]))

    total = 0
    for pair in pairs:
        total += happinesses[pair[0]].get(pair[1], 0)
        total += happinesses[pair[1]].get(pair[0], 0)

    return total


def solve1(input):
    happinesses = parse(input)
    totals = []
    for arrangement in permutations(happinesses.keys(), len(happinesses.keys())):
        totals.append(tally_arrangement(arrangement, happinesses))
    return max(totals)


def solve2(input):
    happinesses = parse(input)
    happinesses['me'] = dict()
    totals = []
    for arrangement in permutations(happinesses.keys(), len(happinesses.keys())):
        totals.append(tally_arrangement(arrangement, happinesses))
    return max(totals)


    

if __name__ == '__main__':
    from aocd.models import Puzzle

    puzzle = Puzzle(2023, 1)
    input_data = puzzle.input_data
    answer_1 = solve1(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve2(input_data)
    print(answer_2)
    puzzle.answer_b = answer_2 