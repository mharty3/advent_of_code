def find_next_value(sequence, part=1):
    if len(set(sequence)) == 1:
        return sequence[0]
    
    else:
        diff = [ii - i for ii, i in zip(sequence[1:], sequence[:-1])]
        if part == 1:
            return sequence[-1] + find_next_value(diff)
        else:
            return sequence[0] - find_next_value(diff, 2)


def solve1(input_data, part=1):
    total = 0
    for line in input_data.splitlines():
        total += find_next_value([int(n) for n in line.split()], part)
    return total


if __name__ == "__main__":
    from aocd.models import Puzzle

    puzzle = Puzzle(2023, 9)

    answer_1 = solve1(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve1(puzzle.input_data, 2)
    print(answer_2)
    puzzle.answer_b = answer_2

