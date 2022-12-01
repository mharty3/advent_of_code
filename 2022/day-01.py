# https://adventofcode.com/2022/day/1

def parse(input_data):
    calorie_lists = input_data.strip().split('\n\n')
    return [
                [int(c) for c in cal_list.split('\n')] 
                    for cal_list in calorie_lists
            ]


def solve1(input_data):
    # how much is the elf with the most carrying
    calories = parse(input_data)
    return max([sum(l) for l in calories])


def solve2(input_data):
    # how much are the top three elves carrying together
    calories = parse(input_data)
    return sum(sorted([sum(l) for l in calories])[-3:])

if __name__ == '__main__':

    test_data = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""
    
    assert solve1(test_data) == 24000
    assert solve2(test_data) == 45000

    from aocd.models import Puzzle
    puzzle = Puzzle(2022, 1)
    answer_1 = solve1(puzzle.input_data)

    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve2(puzzle.input_data)
    puzzle.answer_b = answer_2





