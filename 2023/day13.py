from aocd.models import Puzzle
puzzle = Puzzle(2023, 13)
input_data = puzzle.input_data


test1 = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#."""

test2 = """#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

def parse(input_data):
    data = []
    for map_ in input_data.split('\n\n'):
        data.append([list(row) for row in map_.splitlines()])

    return data


def single_line_reflections(row):
    reflections = set()
    for i, _ in enumerate(row):
        # if i < len(row) // 2:
        #     continue

        left = row[i-1::-1]
        right = row[i:]

        for l, r in zip(left, right):
            # print(l, r)
            if l != r:
                # print('breaking')
                break
        else:
            # print(left, right)
            # print(i)
            reflections.add(i)
    return reflections



def single_line_reflections(row, smudges=0):
    reflections = set()
    for i, _ in enumerate(row):

        left = row[i-1::-1]
        right = row[i:]

        if len([(l, r) for l, r in zip(left, right) if l != r]) == 0:
            reflections.add(i)

    return reflections


def score_map(map_,):
    v_reflections = []
    for row in map_:
        v_reflections.append(single_line_reflections(row))
    v_plane = set.intersection(*v_reflections)
    if v_plane:
        return min(v_plane)

    h_reflections = []
    for col in zip(*map_):
        h_reflections.append(single_line_reflections(col))
    h_plane = set.intersection(*h_reflections)
    if h_plane:
        return min(h_plane) * 100


def solve1(input_data):
    return sum([score_map(m) for m in parse(input_data) if score_map(m)])

