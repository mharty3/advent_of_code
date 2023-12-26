from itertools import permutations
import networkx as nx


def parse(input_data):
    g = nx.Graph()
    for line in input_data.split('\n'):
        origin, _, dest, _, weight = line.split()
        weight = int(weight)
        g.add_edge(origin, dest, weight=weight)

    valid_paths = list()
    for path in permutations(g.nodes, len(g.nodes)):
        if (path in valid_paths) or (reversed(path) in valid_paths):
            continue
        else:
            valid_paths.append(path)

    return g, valid_paths


def solve1(input_data):
    g, valid_paths = parse(input_data)
    return min([nx.path_weight(g, p, 'weight') for p in valid_paths])


def solve2(input_data):
    g, valid_paths = parse(input_data)
    return max([nx.path_weight(g, p, 'weight') for p in valid_paths])


if __name__ == '__main__':
    from aocd.models import Puzzle

    puzzle = Puzzle(2015, 9)
    input_data = puzzle.input_data
    answer_1 = solve1(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve2(puzzle.input_data)
    print(answer_2)
    puzzle.answer_b = answer_2 
