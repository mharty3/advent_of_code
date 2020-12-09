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
        self.original_code = (
            self.code.copy()
        )  # so we can reset self.code to original value if needed
        self.command_counter = [0 for _ in self.code]

    def run(self) -> Tuple[int, int]:
        # reset
        self.command_counter = [0 for _ in self.code]
        self.accumulator = 0
        self.index = 0

        while 1:
            if self.index == len(self.code):  # code has finished safely
                return self.accumulator, 0  # error code 0

            if self.command_counter[
                self.index
            ]:  # command at index has been run before. in inf loop
                return self.accumulator, 1  # error code 1

            else:  # run code
                instr, arg = self.code[self.index]
                self.command_counter[self.index] += 1

                if instr == "nop":
                    self.index += 1
                elif instr == "acc":
                    self.index += 1
                    self.accumulator += arg
                elif instr == "jmp":
                    self.index += arg

    def fix_corrupted_code(self) -> None:
        for idx, (instr, arg) in enumerate(self.code):
            self.code = self.original_code.copy()  # reset code
            error_code = 1 # code starts broken

            if instr == "nop":
                self.code[idx] = ("jmp", arg)
                _, error_code = self.run()

            elif instr == "jmp":
                self.code[idx] = ("nop", arg)
                _, error_code = self.run()

            if error_code == 0:  # code exits with no errors
                break  # code is fixed


def solve1(input_data: str) -> int:
    code = parse(input_data)
    g = GameBoy(code)
    return g.run()[0]


def solve2(input_data: str) -> int:
    code = parse(input_data)
    g = GameBoy(code)
    g.fix_corrupted_code()
    return g.run()[0]


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

    assert solve1(test_data) == 5
    assert solve2(test_data) == 8

    puz8 = Puzzle(2020, 8)
    data = puz8.input_data
    puz8.answer_a = solve1(data)
    puz8.answer_b = solve2(data)
