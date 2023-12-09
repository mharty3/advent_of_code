from functools import reduce
from numpy import lcm


def parse(input_data):
    directions_raw, network_raw = input_data.split('\n\n')

    directions = [int(d) for d in (list(directions_raw
                                            .replace('L', '0')
                                            .replace('R', '1')))]
    
    network = {}
    for line in network_raw.splitlines():
        start, ends = line.replace('(', '').replace(')', '').split(' = ')
        network[start] = ends.split(', ')

    return directions, network


def solve1(input_data):
    directions, network = parse(input_data)
    current_node = 'AAA'
    
    i = 0
    while current_node != 'ZZZ':
        index = directions[i % len(directions)]
        current_node = network[current_node][index]
        i += 1
    return i


def solve2_bad(input_data):
    # I let this run while I worked. If I let it keep going, it would have finished in
    #  about a year and a half

    directions, network = parse(input_data)
    current_nodes = [n for n in network.keys() if n.endswith('A')]
    
    i = 0
    while len(current_nodes) != len([n for n in current_nodes if n.endswith('Z')]):
        index = directions[i % len(directions)]
        next_nodes = []
        for node in current_nodes:
            next_nodes.append(network[node][index])
        current_nodes = next_nodes
        i += 1
        if not i % 1_000_000:
            print(i)
    return i


def solve2(input_data):
    directions, network = parse(input_data)
    current_nodes = [n for n in network.keys() if n.endswith('A')]
    
    z_spacings = [] # cycle lengths for each starting node

    for node in current_nodes:
        current_node = node
        iz = [] # indices where a Z is reached from the node
        i = 0
        
        while len(iz) < 2: # assume spacing between the first 2 Z nodes is consistent for all (based on hints)
            index = directions[i % len(directions)]
            current_node = network[current_node][index]
            if current_node.endswith('Z'):
                iz.append(i)
            i += 1
        
        z_spacings.append(iz[1] - iz[0])
    
    return reduce(lcm, z_spacings) # functools!


if __name__ == "__main__":
    from aocd.models import Puzzle

    puzzle = Puzzle(2023, 8)

    test_data = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""


    test_data2 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

    answer_1 = solve1(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve2(puzzle.input_data)
    print(answer_2)
    puzzle.answer_b = answer_2


# 9_143_000_000
# 13_591_000_000
# 13_591_000_000
# 16_887_000_000

#19_185_263_738_117 * .5 / 16_887_000_000 / 365