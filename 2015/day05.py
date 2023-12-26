from typing import List

def vowel_count(input: str) -> int:
    count = 0
    for v in 'aeiou':
        count += input.count(v)
    return count

def double_letter_count(input: str) -> int:
    count = 0
    for l, ll in zip(input[:-1], input[1:]):
        if l == ll:
            count += 1
    return count

def forbidden_string_count(input: str, 
                           forbidden_strings:List[str]=['ab', 'cd', 'pq', 'xy']) -> int:
    count = 0 
    for f in forbidden_strings:
        count += input.count(f)
    return count


def contains_non_overlapping_double(input: str) -> bool:
    for i, _ in enumerate(input):
        if input[i:i+2] in input[i+2:]:
            return True
    return False


def contains_repeat_with_a_space(input:str) -> bool:
    for a, b in zip(input[:-2], input[2:]):
        if a == b:
            return True
    return False


def solve1(input):
    count = 0
    for s in input.split():
        print(s)
        if (vowel_count(s) >= 3) and (double_letter_count(s) >= 1) and (forbidden_string_count(s)==0):
            print(s)
            count += 1
    return count


def solve2(input):
    count = 0 
    for s in input.split():
        if contains_non_overlapping_double(s) and contains_repeat_with_a_space(s):
            count += 1
    return count

if __name__ == '__main__':

    from aocd.models import Puzzle
    
    puzzle = Puzzle(2015, 5)
    answer_1 = solve1(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1

    assert contains_repeat_with_a_space('qjhvhtzxzqqjkmpb')
    assert contains_non_overlapping_double('qjhvhtzxzqqjkmpb')
    answer_2 = solve2(puzzle.input_data)
    print(answer_2)
    puzzle.answer_b = answer_2 
