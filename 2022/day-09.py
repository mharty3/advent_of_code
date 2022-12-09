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
        # print(inst)
        head = move_knot(head, inst)
        dist = head_to_tail_dist(head, tail)
        # print(inst)

        if abs(dist[0]) <= 1 and abs(dist[1]) <= 1: # head and tail are touching
            tail_locations.append(tail)
            print(head, dist, tail)
            continue

        elif dist[0] == 0 or dist[1] == 0: # H and T in same column or row
            tail = move_knot(tail, inst)

        elif abs(dist[0]) > 0 and abs(dist[1]) > 0:
            tail_inst = (int(copysign(1, dist[0])), int(copysign(1, dist[1])))
            tail = move_knot(tail, tail_inst)
        

        print(head, dist, tail)
        tail_locations.append(tail)
    print(tail_locations)
    return len(set(tail_locations))


def move_knot(head, tail):


"""
(0, 0) # initial
# R 4
0, 0
1, 0
2, 0
3, 0


# U 4
3, 0
4, 1
4, 2
4, 3

# L 3
4, 3
3, 4
2, 4

# D 1



"""





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
    assert solve1(test_data) == 13
    # assert solve1(test_data) == 21
    # assert solve2(test_data) == 8


    from aocd.models import Puzzle
    puzzle = Puzzle(2022, 9)

    answer_1 = solve1(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1

    # answer_2 = solve2(puzzle.input_data)
    # print(answer_2)
    # puzzle.answer_b = answer_2


