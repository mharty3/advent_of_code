import itertools
import networkx as nx
from aocd.models import Puzzle
puzzle = Puzzle(2023, 25)
input_data = puzzle.input_data


def parse(input_data):
    d = dict()
    for line in input_data.splitlines():
        a, b = line.split(':')
        d[a] = b.split()
    return d


# input_data = test_data
d = parse(input_data)
g = nx.Graph(d)
k = 1
comp = nx.community.girvan_newman(g)

for communities in itertools.islice(comp, k):
    c = tuple(c for c in communities)

a = len(c[0]) * len(c[1])

answer_a = a