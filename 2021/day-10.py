# --- Day 10: Syntax Scoring ---
# https://adventofcode.com/2021/day/10

import re
from statistics import median


def remove_closed_sets(line):
    pattern = r"{}|\(\)|\[\]|<>|\s"
    if not re.search(pattern, line):
        return line
    else:
        line = re.sub(pattern, "", line)
        return remove_closed_sets(line)


def solve1(input_data):
    closing_brackets = "[}\]\)>]"
    scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
    score = 0
    for line in input_data.splitlines():
        if match := re.search(closing_brackets, remove_closed_sets(line)):
            score += scores[match[0]]
    return score


def score2(closers):
    score = 0
    scores = {")": 1, "]": 2, "}": 3, ">": 4}

    for c in closers:
        score *= 5
        score += scores[c]
    return score


def solve2(input_data):
    closing_brackets = "[}\]\)>]"
    pairs = {"{": "}", "[": "]", "(": ")", "<": ">"}
    scores = []
    for line in input_data.splitlines():
        openers = remove_closed_sets(line)
        if re.search(closing_brackets, openers):
            continue
        closers = [pairs[opener] for opener in list(openers)[::-1]]

        scores.append(score2(closers))

    return median(scores)


if __name__ == "__main__":
    from aocd.models import Puzzle

    test_data = """[({(<(())[]>[[{[]{<()<>>
    [(()[<>])]({[<{<<[]>>(
    {([(<{}[<>[]}>{[]{[(<()>
    (((({<>}<{<{<>}{[]{[]{}
    [[<[([]))<([[{}[[()]]]
    [{[{({}]{}}([{[{{{}}([]
    {<[[]]>}<{[{[{[]{()[[[]
    [<(<(<(<{}))><([]([]()
    <{([([[(<>()){}]>(<<{{
    <{([{{}}[<[[[<>{}]]]>[]]"""

    assert solve1(test_data) == 26397
    assert solve2(test_data) == 288957
    puzzle = Puzzle(2021, 10)

    answer_1 = solve1(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve2(puzzle.input_data)
    print(answer_2)
    puzzle.answer_b = answer_2
