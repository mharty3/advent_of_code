from math import prod, factorial
from itertools import product

from aocd.models import Puzzle
from copy import deepcopy

puzzle = Puzzle(2024, 7)
input_data = puzzle.input_data

test_data = """190: 1 10 1 19
3267: 81 40 27
83: 1 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

def parse(input_data):
    results = []
    operands = []
    for line in input_data.splitlines():
        result, ops = line.split(': ')
        results.append(int(result))
        operands.append([int(o) for o in ops.split()])
    return results, operands

def is_valid(result, operands):
    
    n = len(operands) - 1
    operator_options = list(product(['+', '*'], repeat=n))
    # print(result)
    # print(operator_options)

    for option in operator_options:

        running_total = operands[0]
        for operator, operand in zip(option, operands[1:]):
            if operator == '*':
                running_total = running_total * operand
            elif operator == '+':
                running_total = running_total + operand
            
        if running_total == result:
            return True
    
    return False


def solve1(input_data):

    results, operands = parse(input_data)

    total_valid_results = 0
    for result, operands in zip(results, operands):
        if is_valid(result, operands):
            total_valid_results += result

    return total_valid_results        
