# --- Day 10: Balance Bots ---
import re


def parse_instructions(input_data):
    assigns = []
    gives = {}
    lines = input_data.split('\n')
    assignment_pattern = '(\d+) goes to bot (\d+)'
    give_pattern = '(\d+) gives low to (.+) and high to (.+)'
    for line in lines:
        if match := re.search(assignment_pattern, line):
            value, bot = (int(d) for d in match.groups())
            assigns.append((bot, value))
        
        if match := re.search(give_pattern, line):
            give_bot, low_to, high_to = match.groups()
            gives[int(give_bot)] =  (low_to, high_to)
        
    return (assigns, gives)


def give_value(bots, bot, value):
    if bots.get(bot, None):
        bots[bot].append(value)
        bots[bot].sort()
    else:
        bots[bot] = [value]
    return bots


def check_for_full_bots(bots):
    fulls = []
    for key, value in bots.items():
       if len(value) == 2:
           fulls.append(key)
    return fulls


def execute_rules(bots, outputs, history, rules):
    fulls = check_for_full_bots(bots)
    for full in fulls:        
        history[tuple(bots[full])] = full
        for value, instruction in zip(bots[full], rules[full]):
            destination_type, destination_num = instruction.split()
            destination_num = int(destination_num)

            if destination_type == 'bot':
                bots = give_value(bots, destination_num, value)

            if destination_type == 'output':
                outputs = give_value(outputs, destination_num, value)
        bots[full] = []
    return bots, outputs, history


def run(input_data):
    assigns, gives = parse_instructions(input_data)

    bots = {}
    outputs = {}
    history = {}

    for bot, value in assigns:
        bots = give_value(bots, bot, value)

    fulls = check_for_full_bots(bots)
    while fulls:
        bots, outputs, history = execute_rules(bots, outputs, history, gives)
        fulls = check_for_full_bots(bots)

    return outputs, history

def solve1(input_data):
    _, history = run(puzzle.input_data)
    return history[(17, 61)]


def solve2(input_data):
    outputs, _ = run(input_data)
    return(outputs[0].pop() * outputs[1].pop() * outputs[2].pop())

instructions = """value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2"""

if __name__ == '__main__':
    from aocd.models import Puzzle
    puzzle = Puzzle(2016, 10)
    answer_1 = solve1(puzzle.input_data)

    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve2(puzzle.input_data)
    print(answer_2)
    puzzle.answer_b = answer_2