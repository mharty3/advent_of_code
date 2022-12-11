def parse(input_data):
    instructions = []
    for inst in input_data.splitlines():
        instructions.append(inst.split())
    return instructions


def run_computer(input_data):
    register = [1]

    program = parse(input_data)
    for inst in program:
        if inst[0] == 'noop':
            register.append(register[-1])
        if inst[0] == 'addx':
            register.append(register[-1])
            register.append(register[-1] + int(inst[1]))
    
    return register


def solve1(input_data):
    r = run_computer(input_data)
    total = 0
    for i in range(6):
        cycle = (20 + 40 * i) - 1
        print(i, cycle, r[cycle] , r[cycle] * cycle + 1)
        total += r[cycle] * (cycle + 1)
    return total


def display_monitor(register):
    screen = []
    for i, x in enumerate(register):

        if i % 40 in [x -1, x, x+1]:
            screen.append('#')
        else:
            screen.append('.')
        if (i+1) % 40 == 0 and (i+1) != 0:
            screen.append('\n')
            
    return ''.join(screen)
    
    


if __name__ == '__main__':


    test_data_1 = """noop
addx 3
addx -5
"""

    test_data_2 = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

    assert solve1(test_data_2) == 13140


    from aocd.models import Puzzle
    puzzle = Puzzle(2022, 10)

    answer_1 = solve1(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1

    print(display_monitor(puzzle.input_data))

#     ###..####.###...##..####.####...##.###..
#     #..#....#.#..#.#..#....#.#.......#.#..#.
#     #..#...#..###..#......#..###.....#.###..
#     ###...#...#..#.#.##..#...#.......#.#..#.
#     #....#....#..#.#..#.#....#....#..#.#..#.
#     #....####.###...###.####.####..##..###..
#     
#     PZBGZEJB
