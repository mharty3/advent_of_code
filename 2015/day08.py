input = '"aaa\"aaa"'.replace('\\', '/')
len(input)

with open('2015/day08_test.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]





input = '"\x27"'


from aocd.models import Puzzle

puzzle = Puzzle(2015, 8)
input_data = puzzle.input_data#.replace('\\', '/')

lines = input_data.split()


def score(l):

    quote_count = l.count('\\"')
    hex_count = l.count('\\x')
    backslash_count = l.count('\\\\')
    double_bs_count = l.count('\\\\\\\\')
    print(quote_count, hex_count, backslash_count)
    return 2 + quote_count + 3*hex_count + backslash_count #- double_bs_count


running_score = 0
for l in lines:
    sub_score = score(l)
    print(l)
    print(sub_score)
    running_score += sub_score

print(running_score)