from collections import Counter

def get_password_and_criteria(val):
    vals = val.split(' ')
    arg1, arg2 = vals[0].split('-')
    char = vals[1][0]
    password = vals[2]
    return int(arg1), int(arg2), char, password


def check_sled_password(val):
    min_, max_, char, password = get_password_and_criteria(val)
    char_count = Counter(password)[char]
    return (char_count <= max_) and (char_count >= min_)


def check_toboggan_password(val):
    arg1, arg2, char, password = get_password_and_criteria(val)
    return (password[arg1 - 1] == char) ^ (password[arg2 - 1] == char) # ^ is logical XOR


def solve_sled(input_vals):
    return len([v for v in input_vals if check_sled_password(v)])


def solve_toboggan(input_vals):
    return len([v for v in input_vals if check_toboggan_password(v)])

if __name__ == "__main__":
    from aocd.models import Puzzle
    puz = Puzzle(2020, 2)

    test_vals = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']

    assert get_password_and_criteria(test_vals[0]) == (1, 3, 'a', 'abcde')
    assert get_password_and_criteria(test_vals[1]) == (1, 3, 'b', 'cdefg')
    assert get_password_and_criteria(test_vals[2]) == (2, 9, 'c', 'ccccccccc')

    assert check_sled_password(test_vals[0]) == True
    assert check_sled_password(test_vals[1]) == False
    assert check_sled_password(test_vals[2]) == True

    assert check_toboggan_password(test_vals[0]) == True
    assert check_toboggan_password(test_vals[1]) == False
    assert check_toboggan_password(test_vals[2]) == False
        
    assert solve_sled(test_vals) == 2
    assert solve_toboggan(test_vals) == 1

    input_vals = puz.input_data.split('\n')

    puz.answer_a = solve_sled(input_vals)
    puz.answer_b = solve_toboggan(input_vals)