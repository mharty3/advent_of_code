from typing import List, Tuple


def parse(input_data: str) -> List[Tuple[str, int]]:
    lines = input_data.strip().split('\n')
    course = [line.split() for line in lines]
    course = [(direction, int(dist)) for direction, dist in course]
    return course


def underway(x, z, instruction):
    if instruction[0] == 'forward':
        x += instruction[1]

    elif instruction[0] == 'up':
        z -= instruction[1]

    elif instruction[0] == 'down':
        z += instruction[1]

    return x, z


def underway_2(x, z, aim, instruction):
    if instruction[0] == 'forward':
        x += instruction[1]
        z += aim * instruction[1]

    elif instruction[0] == 'up':
        aim -= instruction[1]

    elif instruction[0] == 'down':
        aim += instruction[1]

    return x, z, aim


def solve1(input_data):
    x = 0
    z = 0
    for instruction in parse(input_data):
        x, z = underway(x, z, instruction)
    return x * z


def solve2(input_data):
    x = 0
    z = 0
    aim = 0
    for instruction in parse(input_data):
        x, z, aim = underway_2(x, z, aim, instruction)
        
    return x * z

    
if __name__ == '__main__': 

    test_data = """forward 5
    down 5
    forward 8
    up 3
    down 8
    forward 2"""

    assert solve1(test_data) == 150
    assert solve2(test_data) == 900

    from aocd.models import Puzzle
    puzzle = Puzzle(2021, 2)

    answer_1 = solve1(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve2(puzzle.input_data)
    puzzle.answer_b = answer_2



