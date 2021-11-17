from typing import NamedTuple, Tuple, List



def manhattan_dist(a: Tuple, b: Tuple=(0,0)) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def parse(puzzle_input: str) -> List[Tuple[str, int]]:
    instructions = puzzle_input.strip().split(', ')
    instructions_parsed = list()
    for inst in instructions:
        turn = inst[0]
        step = int(inst[1:])
        instructions_parsed.append((turn, step))
    return instructions_parsed


def turn(direction_facing: int, direction_to_turn: str) -> int:
    if direction_to_turn == 'L':
        return (direction_facing - 90) % 360
    elif direction_to_turn == 'R':
        return (direction_facing + 90) % 360


def step(position: Tuple[int, int], direction_facing: int, step: int) -> Tuple[int, int]:
    if direction_facing == 0:
        return position[0], position[1] + step, 
    elif direction_facing == 90:
        return position[0] + step, position[1]
    elif direction_facing == 180:
        return position[0], position[1] - step
    elif direction_facing == 270:
        return position[0] - step, position[1]


def solve1(puzzle_input):
    instructions = parse(puzzle_input)
    direction_facing = 0
    position = (0, 0)
    for inst_turn, inst_step in instructions:
        direction_facing = turn(direction_facing, inst_turn)
        position = step(position, direction_facing, inst_step)
    return manhattan_dist(position)


def solve2(puzzle_input):
    instructions = parse(puzzle_input)
    direction_facing = 0
    position = (0, 0)
    positions_visited = {(0,0)}
    for inst_turn, inst_step in instructions:
        direction_facing = turn(direction_facing, inst_turn)
        for i in range(inst_step):
            position = step(position, direction_facing, 1)
            if position in positions_visited:
                return manhattan_dist(position)
            else:
                positions_visited.add(position)

assert solve1('R2, L3') == 5
assert solve1('R2, R2, R2') == 2
assert solve1('R5, L5, R5, R3') == 12

assert solve2('R8, R4, R4, R8') == 4

if __name__ == '__main__':
    from aocd.models import Puzzle
    puzzle = Puzzle(2016, 1)
    answer_1 = solve1(puzzle.input_data)

    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve2(puzzle.input_data)
    puzzle.answer_b = answer_2

