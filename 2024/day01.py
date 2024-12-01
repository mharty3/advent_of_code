from collections import Counter

def parse(input_data):
    left_list = list()
    right_list = list()

    for line in input_data.splitlines():
        i1, i2 = line.split()
        left_list.append(int(i1))
        right_list.append(int(i2))

    return left_list, right_list


def solve1(input_data):
    left_list, right_list = parse(input_data)
    left_list.sort()
    right_list.sort()
    
    sum = 0
    for l, r in zip(left_list, right_list):
        sum += abs(l - r)
    
    return sum


def solve2(input_data):
    left_list, right_list = parse(input_data)
    c = Counter(right_list)
    
    similarity_score = 0
    for i in left_list:
        similarity_score += c[i] * i
    
    return similarity_score


if __name__ == '__main__':
    from aocd.models import Puzzle

    puzzle = Puzzle(2024, 1)
    input_data = puzzle.input_data

    answer_1 = solve1(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve2(input_data)
    
    print(answer_2)
    puzzle.answer_b = answer_2