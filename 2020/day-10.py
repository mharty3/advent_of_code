from itertools import chain, combinations


def solve1(input_data):
    adapters = [int(i.strip()) for i in input_data.split()]
    adapters.sort()
    diffs = [j - i for i, j in zip(adapters[:-1], adapters[1:])]
    return (diffs.count(1) + 1) * (diffs.count(3) + 1)


def powerset(iterable):
    """powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    Copied from the Itertools Recipes
    https://docs.python.org/3/library/itertools.html#itertools-recipes"""

    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def valid_arrangement(arrangement):
    counter = 0
    arrangement = list(arrangement)
    for index, item in enumerate(arrangement):
        if item - arrangement[index - 1] == 1:
            counter += 1
            if counter == 2:
                return False
        else:
            counter = 0
    return True


def solve2(input_data):
    """Test data passes, but runs forever on the real input"""

    adapters = [int(i.strip()) for i in input_data.split()]
    adapters.sort()
    adapters.insert(0, 0)
    compare_forward_and_back_one = [j - i for i, j in zip(adapters[:-1], adapters[2:])]

    # can an individual element be removed?
    singles = [i < 3 for i in compare_forward_and_back_one]
    indices_where_true = [i for i, v in enumerate(singles) if v]

    # find all possible combinations based on the single elements
    # creates tuples with values indicating the index of the removed item
    ps = powerset(indices_where_true)

    # remove the combinations that don't work because you took out three in a row
    # this is slooooow because I have to iterate entirely over every valid combo
    valids = filter(valid_arrangement, ps)
    return sum(1 for _ in valids)  # count them up


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

    additional_test_data = """
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
    assert solve1(additional_test_data) == 220

    assert valid_arrangement((1, 2, 3)) == False
    assert valid_arrangement((1, 2)) == True

    assert solve2(test_data) == 8
    assert solve2(additional_test_data) == 19208

    puz10 = Puzzle(2020, 10)
    data = puz10.input_data
    puz10.answer_a = solve1(data)
    # puz10.answer_b = solve2(data)
