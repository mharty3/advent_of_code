c = [14, 10, 127]

from collections import namedtuple
import re

Reindeer = namedtuple('reindeer', ['rate', 'moving_time', 'resting_time'])

def parse(input_data):
    deers = []
    pattern = '.* (\d+) .* (\d+) .* (\d+)'
    for r in input_data.split('\n'):
        match = re.search(pattern, r)
        deers.append(Reindeer(*[int(i) for i in match.groups()]))
    return deers


def dist(t, reindeer):
    cycle_duration = reindeer.moving_time + reindeer.resting_time
    base_dist = (t // cycle_duration) * reindeer.rate * reindeer.moving_time
    remainder = t % cycle_duration
    return base_dist + min(remainder, reindeer.moving_time) * reindeer.rate

def solve1(input_data, t=2503):
    deers = parse(input_data)
    return max([dist(t, deer) for deer in deers])

def solve2(input_data, t=2503):
    deers = parse(input_data)
    points = [0] * len(deers)
    dists = [0] * len(deers)
    for step in range(t):
        dists = [dist(step+1, deer) for deer in deers]
        max_dist = max(dists)
        for i, d in enumerate(dists):
            if d == max_dist:
                points[i] += 1
    return max(points)



if __name__ == '__main__':
    from aocd.models import Puzzle

    puzzle = Puzzle(2015, 14)
    input_data = puzzle.input_data
    answer_1 = solve1(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve2(input_data)
    print(answer_2)
    puzzle.answer_b = answer_2 