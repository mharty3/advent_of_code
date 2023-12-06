from numpy import prod

def parse(input_data):
    data = []
    for line in input_data.splitlines():
        data.append([int(i) for i in line.split()[1:]])
    return list(zip(*data))


def parse2(input_data):
    data = []
    for line in input_data.splitlines():
        data.append([i for i in line.split()[1:]])
    return [int(''.join(l)) for l in data]


def count_valid_ways(duration, distance):
    count = 0
    for speed in range(duration):
        if speed * (duration - speed) > distance:
            count += 1
    return count


def solve1(input_data):
    data = parse(input_data)
    counts = []
    for duration, distance in data:
        counts.append(count_valid_ways(duration, distance))
    return prod(counts)


def solve2(input_data):
    data = parse2(input_data)
    return count_valid_ways(*data)


if __name__ == "__main__":
    from aocd.models import Puzzle
    import time

    puzzle = Puzzle(2023, 6)

    test_data = """Time:      7  15   30
Distance:  9  40  200"""

    assert solve1(test_data) == 288

    input_data = puzzle.input_data
    answer_1 = solve1(input_data)
    
    print(answer_1)
    puzzle.answer_a = answer_1

    assert solve2(test_data) == 71503
    
    start = time.time()
    answer_2 = solve2(puzzle.input_data)
    end = time.time()

    print((end-start)) # 2.9 seconds 🤯
    
    print(answer_2)
    puzzle.answer_b = answer_2
