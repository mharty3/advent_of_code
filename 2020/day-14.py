from typing import NamedTuple, Sized


class Instruction(NamedTuple):
    command: str
    address: int
    value: str

    @staticmethod
    def from_line(line):
        parts = line.strip().split(" = ")
        subparts = parts[0].rstrip("]").split("[")
        command = subparts[0]
        try:
            address = subparts[1]
        except:
            address = None
        value = parts[1]
        return Instruction(command, address, value)


class Computer:
    def __init__(self, program) -> None:
        self.program = program
        self.memory = {}
        self.mask = ""

    def apply_mask_V1(self, value, mask):
        bits = bin(int(value))[2:].zfill(36)
        return "".join(
            [m if not m == "X" else b for b, m in zip(list(bits), list(mask))]
        )

    def initialize_V1(self):
        for instr in self.program:
            if instr.command == "mask":
                self.mask = instr.value
            elif instr.command == "mem":
                self.memory[instr.address] = self.apply_mask_V1(instr.value, self.mask)
            else:
                RuntimeError()


def solve1(input_data):
    program = [Instruction.from_line(line) for line in input_data.strip().split("\n")]
    computer = Computer(program)
    computer.initialize_V1()
    return sum(int(v, 2) for v in computer.memory.values())


if __name__ == "__main__":
    from aocd.models import Puzzle

    test_data = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
                mem[8] = 11
                mem[7] = 101
                mem[8] = 0"""

    assert solve1(test_data) == 165

    puz14 = Puzzle(2020, 14)
    data = puz14.input_data
    puz14.answer_a = solve1(data)
    # puz14.answer_b = solve2(data)
