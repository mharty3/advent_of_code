import numpy as np
from aocd.models import Puzzle
puzzle = Puzzle(2023, 15)
input_data = puzzle.input_data


def reindeer_hash(input_str):
    cv = 0
    for val in input_str:
        cv += ord(val)
        cv *= 17
        cv %= 256
    return cv


def solve1(input_data):
    return sum([reindeer_hash(val) for val in input_data.replace('\n', '').split(',')])


def parse(input_data):
    instructions = []
    for raw_inst in input_data.replace('\n', '').split(','):
        inst = dict()
        if '-' in raw_inst:
            inst['label'] = raw_inst[:-1]
            inst['focal_length'] = None
        else:
           label, length = raw_inst.split('=')
           inst['label'] = label
           inst['focal_length'] = int(length)
        inst['box'] = reindeer_hash(inst['label'])
        instructions.append(inst)
    return instructions


def solve2(input_data):
    instructions = parse(input_data)

    boxes = {k:[] for k in range(256)}

    for instruction in instructions:

        if instruction['focal_length']: # op is =
            lenses = []
            box = instruction['box']
            replaced_a_lens = False
            for lens in boxes[box]:
                if lens['label'] == instruction['label']:
                    lenses.append(instruction)
                    replaced_a_lens = True
                else:
                    lenses.append(lens)
                
            if not replaced_a_lens:
                lenses.append(instruction)
            
            boxes[box] = lenses
        
        else: # op is -
            lenses = []
            box = instruction['box']
            for lens in boxes[box]:
                if lens['label'] == instruction['label']:
                    continue
                else:
                    lenses.append(lens)
            boxes[box] = lenses


    total = 0
    for box, lenses in boxes.items():
        for i, lens in enumerate(lenses):
            total += (box+1) * (i+1) * lens['focal_length']

    return total

print(solve1(input_data))
print(solve2(input_data))