from os import kill


def solve1(input_data):
    adapters = [int(i.strip()) for i in input_data.split()]
    adapters.sort()
    diffs = [j - i for i, j in zip(adapters[:-1], adapters[1:])]
    return (diffs.count(1) + 1) * (diffs.count(3) + 1)


def solve2(input_data):
    adapters = [int(i.strip()) for i in input_data.split()]
    
    adapters.sort()
    adapters.insert(0,0)
    offset_1 = [j - i for i, j in zip(adapters[:-1], adapters[2:])]
    singles = [i < 3 for i in offset_1] # can an individual element be removed?

    offset_2 = [j - i for i, j in zip(adapters[:-1], adapters[3:])]
    pairs = [i == 3 for i in offset_2] # can an element and the next one inline be removed? ie 2 in a row

    return singles, pairs

    # I think once I have identified the individual elements and the consecutive pairs that can be removed, 
    # that should be enough to solve it, but I can't figure it out. There is probably some math 
    # that I don't know that could come in handy here.
    

if __name__ == "__main__":
    from aocd.models import Puzzle
    test_data = """16
                   10
                   15
                   5
                   1
                   11
                   7
                   19
                   6
                   12
                   4"""

    larger_test_data = """
                        28
                        33
                        18
                        42
                        31
                        14
                        46
                        20
                        48
                        47
                        24
                        23
                        49
                        45
                        19
                        38
                        39
                        11
                        1
                        32
                        25
                        35
                        8
                        17
                        7
                        9
                        4
                        2
                        34
                        10
                        3"""

    assert solve1(test_data) == 35
    assert solve1(larger_test_data) == 220
    
    assert solve2(test_data) == 8
    assert solve2(longer_test_data) == 19208

    puz10 = Puzzle(2020, 10)
    data = puz10.input_data
    puz10.answer_a = solve1(data)
    # puz10.answer_b = solve2(data, 25)
