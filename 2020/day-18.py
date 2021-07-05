from os import umask


def eval(expression):
    if len(expression) <= 1:
        return int(expression[0].replace('(',''))
    else:
        right = grab_right(expression)
        len_right = len(right)
        op = expression[(len_right * -1) - 1]
        left = expression[:(len_right * -1) - 1]  
        
        if op == '+':
            return eval(left) + eval(right)
        elif op == '*':
            return eval(left) * eval(right)


def grab_right(expression):
    # expression = ' '.join(expression)
    right = expression[-1] 
    if ')' not in right:
        return right
    else:
        close_count = right.count(')')
        open_count = 0
        index = len(expression) - 2
        while open_count != close_count:
            prev = expression[index]
            right = ' '.join([prev, right])
            open_count += prev.count('(')
            close_count += prev.count(')')
            index -= 1
        
        if right == ' '.join(expression):
            return right.split(' ')[-1].replace(')', '')
        else:
            return right[1:-1].split(' ')

def solve1(input_data):
    return sum(eval(line.strip().split(' ')) for line in input_data.strip().split('\n'))


if __name__ == "__main__":
    from aocd.models import Puzzle
    
    test_1 = "1 + 2 * 3 + 4 * 5 + 6"
    test_2 = "1 + (2 * 3) + (4 * (5 + 6))"
    test_3 = "2 * 3 + (4 * 5)"
    test_4 = "5 + (8 * 3 + 9 + 3 * 4 * 3)"
    test_5 = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
    test_6 = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"

    exp1 = test_1.split(' ')
    assert eval(exp1) == 71

    exp2 = test_2.split(' ')
    assert eval(exp2) == 51

    exp3 = test_3.split(' ')
    assert eval(exp3) == 26

    exp4 = test_4.split(' ')
    assert eval(exp4) == 437

    exp5 = test_5.split(' ')
    assert eval(exp5) == 12240

    exp6 = test_6.split(' ')
    assert eval(exp6) == 13632

    puz18 = Puzzle(2020, 18)
    data = puz18.input_data
    puz18.answer_a = solve1(data)
    # puz18.answer_b = solve2(data)
