import re

def solve1(input_data):
    values = []
    for c in input_data.splitlines():
        c = re.sub('\D', '', c)
        values.append(int(c[0] + c[-1]))
    return sum(values)


def solve2(input_data):
    """first try.
        this doesn't work because it doesn't go through the string in the right order
        'eightwo' becomes `eigh2` rather than `8wo`
        """
    text_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    trans_table = {k: str(v) for k, v in zip(text_digits, range(1, 10))}

    for k, v in trans_table.items():
        input_data = re.sub(f'{k}', str(v), input_data)
        print(k, v, '\n')
        print(input_data)

    return solve1(input_data)


def solve2_regex(input_data):
    """
    second try.
    this doesn't work with my original pattern but I don't know why.
    It works fine on test data ¯\_(ツ)_/¯

    update:
    after I solved the problem with `solve2_iter`, I found out that re.findall() does not 
    include overlaps. But with a 'lookahead expression', it will (https://stackoverflow.com/a/11430936)
    """

    pattern = '(one|two|three|four|five|six|seven|eight|nine|\d)'
    right_pattern = '(?=(one|two|three|four|five|six|seven|eight|nine|\d))'
    text_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    trans_table = {k: str(v) for k, v in zip(text_digits, range(1, 10))}

    total = 0
    for line in input_data.splitlines():
        match = re.findall(right_pattern, line)
        print(line, match)
        
        first_d = trans_table.get(match[0], match[0])
        second_d = trans_table.get(match[-1], match[-1])
        print(int(first_d + second_d))
        total += int(first_d + second_d)
        
    return total


def solve2_iter(input_data):
    """fine. I will try it this way"""
    calibration_values = []
    for line in input_data.splitlines():
        digits = []
        for i, v in enumerate(line):
            try:
                int(v)
                digits.append(v)
            except ValueError:
                pass

            if line[i:].startswith('one'):
                digits.append('1')
            
            elif line[i:].startswith('two'):
                digits.append('2')

            elif line[i:].startswith('three'):
                digits.append('3')

            elif line[i:].startswith('four'):
                digits.append('4')

            elif line[i:].startswith('five'):
                digits.append('5')

            elif line[i:].startswith('six'):
                digits.append('6')

            elif line[i:].startswith('seven'):
                digits.append('7')

            elif line[i:].startswith('eight'):
                digits.append('8')

            elif line[i:].startswith('nine'):
                digits.append('9')

        calibration_values.append(int(digits[0] + digits[-1]))

    return sum(calibration_values)


if __name__ == '__main__':
    from aocd.models import Puzzle

    test = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

    test2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""


    assert solve1(test) == 142  
    assert solve2_regex(test2) == 281
    assert solve2_iter(test2) == 281

    puzzle = Puzzle(2023, 1)
    input_data = puzzle.input_data
    answer_1 = solve1(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2_regex = solve2_regex(input_data)
    answer_2_iter = solve2_iter(input_data)
    assert answer_2_iter == answer_2_regex
    
    print(answer_2_regex)
    puzzle.answer_b = answer_2_regex