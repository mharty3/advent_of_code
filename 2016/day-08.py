
import numpy as np
from typing import NamedTuple, Optional

from numpy.core.defchararray import startswith


def rect(a: int, b: int, screen):
    screen[:b, :a] = 1
    return screen


def rotate_column(x, shift, screen):
    screen[:, x] = np.roll(screen[:, x], shift)
    return screen


def rotate_row(y, shift, screen):
    screen[y, :] = np.roll(screen[y, :], shift)
    return screen


# tests
test_screen = np.zeros((3,7))

screen = rect(3, 2, test_screen)
print(screen)
print('-------------------')

screen = rotate_column(1, 1, screen)
print(screen)
print('-------------------')

screen = rotate_row(0, 4, screen)
print(screen)


class Instruction(NamedTuple):
    inst_type: str 
    a: Optional[int] = None
    b: Optional[int] = None
    idx: Optional[int] = None
    shift: Optional[int] = None

    @staticmethod
    def from_line(line:str):
        if line.startswith('rect'):
            a, b = line.split()[-1].split('x')
            return Instruction(inst_type='rect', a=int(a), b=int(b))
        
        elif line.startswith('rotate row'):
            y = line.split('y=')[1].split()[0]
            shift = line.split()[-1]
            return Instruction(inst_type='rotate_row', idx=int(y), shift=int(shift))

        elif line.startswith('rotate column'):
            x = line.split('x=')[1].split()[0]
            shift = line.split()[-1]
            return Instruction(inst_type='rotate_col', idx=int(x), shift=int(shift))
            

def solve1(input_data):
    instructions = [Instruction.from_line(line) for line in input_data.split('\n')]
    screen = np.zeros((6, 50))
    for instruction in instructions:
        if instruction.inst_type == 'rect':
            screen = rect(instruction.a, instruction.b, screen)
        elif instruction.inst_type == 'rotate_row':
            screen = rotate_row(instruction.idx, instruction.shift, screen)
        elif instruction.inst_type == 'rotate_col':
            screen = rotate_column(instruction.idx, instruction.shift, screen)
    return screen, int(screen.sum())

def solve2(input_data):
    screen = solve1(input_data)[0]
    for row in screen:
        for col in row:
            if col:
                print( ' # ', end='')
            else:
                print('   ', end='')
        print()

if __name__ == '__main__':
    from aocd.models import Puzzle
    puzzle = Puzzle(2016, 8)
    answer_1 = solve1(puzzle.input_data)

    print(answer_1[1])
    puzzle.answer_a = answer_1[1]

    solve2(puzzle.input_data)

# answer part 2

 #  #  #  #        #  #           #  #        #  #  #           #  #        #  #  #        #        #     #           #     #  #           #  #       
 #              #        #     #        #     #        #     #        #     #        #     #        #     #           #  #        #     #        #    
 #  #  #        #        #     #        #     #        #     #              #        #     #  #  #  #        #     #     #        #     #        #    
 #              #        #     #  #  #  #     #  #  #        #     #  #     #  #  #        #        #           #        #  #  #  #     #        #    
 #              #        #     #        #     #     #        #        #     #              #        #           #        #        #     #        #    
 #  #  #  #        #  #        #        #     #        #        #  #  #     #              #        #           #        #        #        #  #     
