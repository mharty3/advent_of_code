from typing import List, Tuple

def parse(input_data: str) -> List[Tuple[str, int]]:
    lines = input_data.split("\n")
    commands = [line.strip().split(" ") for line in lines]
    return [tuple([command[0], int(command[1])]) for command in commands]


class GameBoy:
    def __init__(self, code: List[Tuple[str, int]]) -> None:
        self.accumulator = 0
        self.index = 0
        self.code = code
        self.command_counter = [0 for _ in self.code]
    
    def run(self) -> None:
        
        while 1: # not any([count > 1 for count in self.command_counter]):
            if self.command_counter[self.index]:
                return self.accumulator
            else:
                instr, arg = self.code[self.index]
                self.command_counter[self.index] += 1

                if instr == 'nop':
                    self.index += 1
                elif instr == 'acc':
                    self.index += 1
                    self.accumulator += arg
                elif instr == 'jmp':
                    self.index += arg
        
def solve1(input_data):
    code = parse(input_data)
    g = GameBoy(code)
    return g.run()

if __name__ == "__main__":
    from aocd.models import Puzzle

    test_data = """nop +0
                   acc +1
                   jmp +4
                   acc +3
                   jmp -3
                   acc -99
                   acc +1
                   jmp -4
                   acc +6"""

    code = parse(test_data)
    g = GameBoy(code)
    assert g.run() == 5

    puz8 = Puzzle(2020, 8)
    data = puz8.input_data
    puz8.answer_a = solve1(data)
    #puz8.answer_b = solve2(data)

