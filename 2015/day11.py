from string import ascii_lowercase

def numberToBase(n, b):
    # https://stackoverflow.com/a/28666223
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


def increment(input_string):
    lu = '0123456789' + ascii_lowercase[:16]

    encoder = {ord(k): v for k, v in zip(ascii_lowercase, lu)}

    encoded = input_string.translate(encoder)
    int_value = int(encoded, 26) + 1

    decoded = numberToBase(int_value, 26)

    forbidden = [8, 11, 14]

    for i, num in enumerate(decoded):
        if num in forbidden:
            decoded[i] = num + 1
            for j, _ in enumerate(decoded[i+1:]):
                decoded[j+i+1] = 0


    l = [ascii_lowercase[v] for v in decoded]
    return ''.join(l).rjust(8, 'a')


def contains_run(input_string):
    for i, char in enumerate(input_string[:-2]):
        sequence = char + input_string[i+1] + input_string[i+2]
        if sequence in ascii_lowercase:
            return True
    return False


def non_overlapping_double_count(input_string):
    count = 0
    inds = set()
    for i, (l, ll) in enumerate(zip(input_string[:-1], input_string[1:])):
        if (l == ll) and i-1 not in inds:
            count += 1
            inds.add(i)
    return count

def is_valid_pwd(pwd):
    return (contains_run(pwd) and 
            (non_overlapping_double_count(pwd) == 2) and 
            (not (('i' in pwd) or ('o' in pwd) or ('l' in pwd)))
    )

def solve1(pwd):
    while not is_valid_pwd(pwd):
        pwd = increment(pwd)
        # print(pwd)
    return pwd


if __name__ == '__main__':
    from aocd.models import Puzzle

    puzzle = Puzzle(2015, 11)
    input_data = puzzle.input_data
    answer_1 = solve1(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve1(increment(answer_1))
    print(answer_2)
    puzzle.answer_b = answer_2 

