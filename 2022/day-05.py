import re

def parse(input_data):
    arrangement_raw, instructions_raw = input_data.split('\n\n') 

    # fill empty slots with '_'
    arrangement = re.sub('\[|\]| ', '', 
            arrangement_raw.replace('    ', '_'))

    # parse rows of crates into list of lists
    rows = []
    for line in arrangement.strip().splitlines()[:-1]:
        rows.append(list(line))

    # transpose list of lists (and reverse each resulting list)
    # https://stackoverflow.com/questions/6473679/transpose-list-of-lists
    stacks = [reversed(list(i)) for i in zip(*rows)]

    # filter out empty slots
    stacks = [[crate for crate in stack if crate != '_'] for stack in stacks]

    instructions = []
    for inst in instructions_raw.strip().splitlines():
        pattern = re.compile(r"(\d+),?") # https://stackoverflow.com/a/15143060
        instructions.append([int(i) for i in pattern.findall(inst)])

    return stacks, instructions


def solve1(input_data):
    stacks, instructions = parse(input_data)
    
    for count, origin, dest in instructions:
        for _ in range(count):
            stacks[dest - 1].append(stacks[origin-1].pop())

    top_crates =  ''.join([stack.pop() for stack in stacks])

    assert len(top_crates) == len(stacks)
    return top_crates


def solve2(input_data):
    stacks, instructions = parse(input_data)
    
    for count, origin, dest in instructions:
        substack = stacks[origin - 1][-count:]
        stacks[origin - 1] = stacks[origin - 1][:-count]
        stacks[dest - 1].extend(substack)

    top_crates =  ''.join([stack.pop() for stack in stacks])
    return top_crates

if __name__ == '__main__':

    test_data = """
    [D]    
[N] [C]    
[Z] [M] [P]
1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
    """

    assert solve1(test_data) == 'CMZ'
    assert solve2(test_data) == 'MCD'

    from aocd.models import Puzzle
    puzzle = Puzzle(2022, 5)
    answer_1 = solve1(puzzle.input_data)

    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve2(puzzle.input_data)
    puzzle.answer_b = answer_2
    print(answer_2)
    