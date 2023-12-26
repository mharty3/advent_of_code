def solve1(input_data:str) -> int:
    return input_data.count('(') - input_data.count(')')

def solve2(input_data:str) -> int:
    floor = 0
    for i, step in enumerate(input_data):
        if step == '(':
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            return i + 1





if __name__ == '__main__':
    assert solve1('(())') == 0
    assert solve1('()()') == 0
    assert solve1('(((') == 3
    assert solve1('(()(()(') == 3



    from aocd.models import Puzzle
    puzzle = Puzzle(2015, 1)
    answer_1 = solve1(puzzle.input_data)
    puzzle.answer_a = answer_1

    puzzle.answer_b = solve2(puzzle.input_data)