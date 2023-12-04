import re
import numpy as np

def parse(input_data):
    data = input_data.splitlines()
    data = ["." + row.strip() + "." for row in data]
    top_and_bottom_pad = "." * len(data[0])
    data.insert(0, top_and_bottom_pad)
    data.append(top_and_bottom_pad)

    return np.array([list(row) for row in data])


def is_valid_num(num, r, c, schematic):
    left = c - (len(num) + 1)
    right = c + 1
    up = r - 1
    down = r + 2
    neighbors = ''.join(schematic[up:down, left:right].ravel())
    return bool(re.search('[^\d\.]', neighbors))


def gear_ratio(r, c, schematic):
    neighbor_nums = []
    
    up = r - 1
    down = r + 2
    neighbor_rows = schematic[up:down]
    num = ''
    
    for row in neighbor_rows:
        for col, val in enumerate(row):

            if str(val).isnumeric():
                num += str(val)

            elif num and not str(val).isnumeric():
                start = col - len(num)
                end = col - 1

                if np.abs(start - c) <= 1 or np.abs(end - c) <= 1:
                    neighbor_nums.append(int(num))

                num = ''

    if len(neighbor_nums) == 2:
        return np.prod(neighbor_nums)
    
    else:
        return 0
    

def solve1(input_data):
    total = 0
    schematic = parse(input_data)
    num = ''

    for r, row in enumerate(schematic):
        for c, col in enumerate(row):
            if str(col).isnumeric():
                num += str(col)
            elif num and not str(col).isnumeric():
                if is_valid_num(num, r, c, schematic):
                    total += int(num)      
                num = ''

    return total


def solve2(input_data):
    schematic = parse(input_data)
    star_indices = np.transpose((schematic == '*').nonzero())
    return np.sum([gear_ratio(r, c, schematic) for r, c in star_indices])



if __name__ == "__main__":
    from aocd.models import Puzzle

    test_data = """467..114..
                   ...*......
                   ..35..633.
                   ......#...
                   617*......
                   .....+.58.
                   ..592.....
                   ......755.
                   ...$.*....
                   .664.598.."""


    assert solve1(test_data) == 4361
    assert solve2(test_data) == 467835

    puzzle = Puzzle(2023, 3)

    answer_1 = solve1(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve2(puzzle.input_data)
    print(answer_2)
    puzzle.answer_b = answer_2


