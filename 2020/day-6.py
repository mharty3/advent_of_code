from collections import Counter

def solve1(input_data):
    groups = input_data.split('\n\n')
    return sum([len(set(group).difference(set('\n'))) for group in groups])

def solve2(input_data):
    groups = input_data.split('\n\n')
    group_size = [len(g.split('\n')) for g in groups] # how many members in each group
    counters = [Counter(g.replace('\n', '')) for g in groups] # count of each non new line char in each group
    
    # for each group, find the number of times a char count equals the member count
    return sum([list(c.values()).count(gs) for gs, c in zip(group_size, counters)])

test_data = """abc

a
b
c

ab
ac

a
a
a
a

b"""

if __name__ == "__main__":
    from aocd.models import Puzzle

    assert solve1(test_data) == 11
    assert solve2(test_data) == 6
    
    puz6 = Puzzle(2020, 6)
    data = puz6.input_data
    puz6.answer_a = solve1(data)
    puz6.answer_b = solve2(data)