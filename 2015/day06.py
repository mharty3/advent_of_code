import numpy as np
import re

def solve1(input):
    instructions = input.split('\n')

    lights = np.ndarray((1000, 1000))
    lights.fill(-1)

    for inst in instructions:
        lights = flash(lights, inst)
    
    return (lights == 1).sum()


def solve2(input):
    instructions = input.split('\n')

    lights = np.ndarray((1000, 1000))
    lights.fill(0)

    for inst in instructions:
        lights = dim(lights, inst)
    
    return lights.sum()

def flash(lights, instruction):
    pat = '\D*(\d+),(\d+) through (\d+),(\d+)'
    match = re.search(pat, instruction)

    c_start, r_start, c_end, r_end = [int(index) for index in match.groups()]
    target = lights[r_start:r_end + 1, c_start:c_end + 1]

    if 'on' in instruction:
        target[:,:] = 1
    if 'off' in instruction:
        target[:,:] = -1
    if 'toggle' in instruction:
        target[:,:] *= -1
    
    return lights


def dim(lights, instruction):
    pat = '\D*(\d+),(\d+) through (\d+),(\d+)'
    match = re.search(pat, instruction)

    c_start, r_start, c_end, r_end = [int(index) for index in match.groups()]
    target = lights[r_start:r_end + 1, c_start:c_end + 1]

    if 'on' in instruction:
        target[:,:] += 1
    if 'off' in instruction:
        target[:,:] -= 1
        target[target < 0] = 0
    if 'toggle' in instruction:
        target[:,:] += 2
    
    return lights


if __name__ == '__main__':

    from aocd.models import Puzzle
    
    puzzle = Puzzle(2015, 6)
    answer_1 = solve1(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve2(puzzle.input_data)
    print(answer_2)
    puzzle.answer_b = answer_2 