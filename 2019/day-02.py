"""
Int Code
https://adventofcode.com/2019/day/2
"""

class Computer():
    def __init__(self, memory, noun, verb):
        self.memory = memory
        self.memory[1] = noun
        self.memory[2] = verb
        self.address = 0


    def add(self):
        address_1 = self.memory[self.address + 1]
        address_2 = self.memory[self.address + 2]
        address_to_update = self.memory[self.address + 3]
        self.memory[address_to_update] = self.memory[address_1] + self.memory[address_2]
    

    def multiply(self):
        address_1 = self.memory[self.address + 1]
        address_2 = self.memory[self.address + 2]
        address_to_update = self.memory[self.address + 3]
        print(address_to_update)
        self.memory[address_to_update] = self.memory[address_1] * self.memory[address_2]
    

    def run(self):
        while self.memory[self.address] != 99:
            op_code = self.memory[self.address]
            if op_code == 1:
               self.add()
            if op_code == 2:
                self.multiply()
            self.address += 4
        return self.memory[0]

    
c = Computer([2, 3, 0, 3, 99], 3, 0)
c.run()

def parse(input_data):
    return [int(val) for val in input_data.split(',')]

def solve1(input_data):
    memory = parse(input_data)
    c = Computer(memory, 12, 2)
    return c.run()

def solve2(input_data):
    memory = parse(input_data)
    for noun in range(500):
        for verb in range(500):
            print(noun, verb)
            c = Computer(memory, noun, verb)
            output = c.run()
            print(output)
            if output == 19690720:
                return noun, verb
    raise ValueError


if __name__ == '__main__':
    from aocd.models import Puzzle
    puzzle = Puzzle(2019, 2)
    answer_1 = solve1(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve2(puzzle.input_data)
    print(answer_2)
    # puzzle.answer_b = answer_2
