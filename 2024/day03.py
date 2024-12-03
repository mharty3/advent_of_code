import re

def solve1(input_data):
    pattern = 'mul\((\d+),(\d+)\)'
    match = re.findall(pattern, input_data)
    total = 0
    for i, j in match:
        total += int(i) * int(j)
    return total


def solve2(input_data):
    """
    I thought this would work, but I think I am stymied by overlaps or something
    ```
    pattern = "don't\(\)(.*)do\(\)"
    active_commands = re.sub(pattern, string=input_data, repl='')
    print(active_commands) 
    return solve1(re.sub(pattern, string=input_data, repl=''))
    ```
    """
    commands = input_data.split("don't()") # split into segments following "don't()"

    total = solve1(commands[0]) # do is on at the beginning
    for command in commands[1:]:
        # remove first part of command until the first "do()"
        do_commands = ''.join(command.split("do()")[1:])
        total += solve1(do_commands)
    return total

if __name__ == '__main__':
    from aocd.models import Puzzle

    puzzle = Puzzle(2024, 3)
    input_data = puzzle.input_data

    answer_1 = solve1(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve2(input_data)
    
    print(answer_2)
    puzzle.answer_b = answer_2