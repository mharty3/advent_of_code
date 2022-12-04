def parse(input_data):
    assignments_raw = input_data.strip().splitlines()
    assignments = [a.replace('-', ',').split(',') for a in assignments_raw]

    return [[int(val) for val in a] for a in assignments]

    

def is_full_overlap(assignment):
    elf_1 = set(range(assignment[0], assignment[1] + 1))
    elf_2 = set(range(assignment[2], assignment[3] + 1))

    return elf_1.issubset(elf_2) or elf_2.issubset(elf_1)


def is_partial_overlap(assignment):
    elf_1 = set(range(assignment[0], assignment[1] + 1))
    elf_2 = set(range(assignment[2], assignment[3] + 1))

    return len(elf_1 & elf_2) != 0


def solve1(input_data):
    assignments = parse(input_data)
    return len([a for a in assignments if is_full_overlap(a)])

    
def solve2(input_data):
    assignments = parse(input_data)
    return len([a for a in assignments if is_partial_overlap(a)])


if __name__ == '__main__':

    test_data = """2-4,6-8
    2-3,4-5
    5-7,7-9
    2-8,3-7
    6-6,4-6
    2-6,4-8"""


    assert solve1(test_data) == 2
    assert solve2(test_data) == 4

    from aocd.models import Puzzle
    puzzle = Puzzle(2022, 4)
    answer_1 = solve1(puzzle.input_data)

    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve2(puzzle.input_data)
    puzzle.answer_b = answer_2

