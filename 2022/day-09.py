from math import copysign

def parse(input_data):
    dir_map = {'R': (1, 0), 
               'L': (-1, 0),
               'U': (0, 1),
               'D': (0, -1)}

    instructions = []
    for move in input_data.splitlines():
        direction, steps = move.split()
        inst = [dir_map[direction]] * int(steps)
        instructions.extend(inst)

    return instructions


def move_knot(knot_loc, inst):
    return (knot_loc[0] + inst[0], knot_loc[1] + inst[1])


def head_to_tail_dist(head, tail):
    return (head[0] - tail[0], head[1] - tail[1])


def solve1(input_data):
    head = (0, 0)
    tail = (0, 0)    
    tail_locations = list()
    
    instructions = parse(input_data)

    for inst in instructions:
        head = move_knot(head, inst)
        dist = head_to_tail_dist(head, tail)

        if abs(dist[0]) <= 1 and abs(dist[1]) <= 1: # head and tail are touching
            tail_locations.append(tail)
            print(head, dist, tail)
            continue

        elif dist[0] == 0: # H and T in the same col
            tail_inst = (0, int(copysign(1, dist[1])))
            tail = move_knot(tail, tail_inst)
            
        elif dist[1] == 0: # H and T in same row
            tail_inst = (int(copysign(1, dist[0])), 0)
            tail = move_knot(tail, inst)

        elif abs(dist[0]) > 0 and abs(dist[1]) > 0:
            tail_inst = (int(copysign(1, dist[0])), int(copysign(1, dist[1])))
            tail = move_knot(tail, tail_inst)
        
        tail_locations.append(tail)
    
    return len(set(tail_locations))


def calculate_knot_instruction(head, tail):

    dist = head_to_tail_dist(head, tail)

    if abs(dist[0]) <= 1 and abs(dist[1]) <= 1: # head and tail are touching
        tail_inst = (0, 0)

    elif dist[0] == 0: # H and T in the same col
        tail_inst = (0, int(copysign(1, dist[1])))
        
    elif dist[1] == 0: # H and T in same row
        tail_inst = (int(copysign(1, dist[0])), 0)

    elif abs(dist[0]) > 0 and abs(dist[1]) > 0:
        tail_inst = (int(copysign(1, dist[0])), int(copysign(1, dist[1])))
    
    else:
        raise ValueError

    return tail_inst


def solve2(input_data):
    instructions = parse(input_data)
    knots = {k: v for k, v in zip(range(0,10), [(0,0)] * 10)}
    tail_locs = []

    for inst in instructions:
        # move head
        knots[0] = move_knot(knots[0], inst)
        # for each knot in the rope update it based on the previous knot location
        for knot in range(1, 10):
            tail_inst = calculate_knot_instruction(knots[knot - 1], knots[knot])
            knots[knot] = move_knot(knots[knot], tail_inst)
        tail_locs.append(knots[9])
    return len(set(tail_locs))
 


if __name__ == '__main__':
    test_data = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""

    test_data_2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

    assert solve1(test_data) == 13
    assert solve2(test_data) == 1
    assert solve2(test_data_2) == 36


    from aocd.models import Puzzle
    puzzle = Puzzle(2022, 9)

    answer_1 = solve1(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve2(puzzle.input_data)
    print(answer_2)
    puzzle.answer_b = answer_2


