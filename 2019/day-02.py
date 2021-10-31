"""
Int Code
https://adventofcode.com/2019/day/2
"""

class Computer():
    def __init__(self, program):
        self.program = program
        self.position = 0


    def add(self):
        pos_1 = self.program[self.position + 1]
        pos_2 = self.program[self.position + 2]
        pos_to_update = self.program[self.position + 3]
        self.program[pos_to_update] = self.program[pos_1] + self.program[pos_2]
    

    def multiply(self):
        pos_1 = self.program[self.position + 1]
        pos_2 = self.program[self.position + 2]
        pos_to_update = self.program[self.position + 3]
        self.program[pos_to_update] = self.program[pos_1] * self.program[pos_2]
    

    def run(self):
        while self.program[self.position] != 99:
            op_code = self.program[self.position]
            if op_code == 1:
               self.add()
            if op_code == 2:
                self.multiply()
            self.position += 4
        return self.program[0]

    
c = Computer([2, 3, 0, 3, 99])
c.run()

def parse(input_data):
    return [int(val) for val in input_data.split(',')]

def solve1(input_data):
    program = parse(input_data)
    program[1] = 12
    program[2] = 2
    c = Computer(program)
    return c.run()


if __name__ == '__main__':
    from aocd.models import Puzzle
    puzzle = Puzzle(2019, 2)
    answer_1 = solve1(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1

    # answer_2 = solve2(puzzle.input_data)
    # print(answer_2)
    # puzzle.answer_b = answer_2
