# --- Day 4: Giant Squid ---
# https://adventofcode.com/2021/day/4


def parse(input):
    groups = input.split("\n\n")
    draws = [int(draw) for draw in groups[0].split(",")]
    boards = [[int(value) for value in board_text.split()] for board_text in groups[1:]]
    markers = [[0] * 25 for i, _ in enumerate(boards)]
    return draws, boards, markers


def bingo(board_markers):
    # check the rows
    for i in range(5):
        start = i * 5
        end = i * 5 + 5
        if sum(board_markers[start:end]) == 5:
            return True
    # check the columns
    for i in range(5):
        if sum(board_markers[i::5]) == 5:
            return True
    return False


def score(markers, board, draw):
    score = 0
    for marker, value in zip(markers, board):
        if not marker:
            score += value
    return score * draw


def solve1(input_data):
    draws, boards, markers = parse(input_data)
    for draw in draws:
        for i, board in enumerate(boards):
            if draw in board:
                idx = board.index(draw)
                markers[i][idx] = 1

            if bingo(markers[i]):
                return score(markers[i], board, draw)


def solve2(input_data):
    draws, boards, markers = parse(input_data)
    winning_boards = set()
    for draw in draws:
        for i, board in enumerate(boards):
            if i in winning_boards:
                continue
            if draw in board:
                idx = board.index(draw)
                markers[i][idx] = 1
            if bingo(markers[i]):
                winning_boards.add(i)
            if len(winning_boards) == len(boards):
                return score(markers[i], board, draw)


if __name__ == "__main__":
    from aocd.models import Puzzle

    test_input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

    22 13 17 11  0
    8  2 23  4 24
    21  9 14 16  7
    6 10  3 18  5
    1 12 20 15 19

    3 15  0  2 22
    9 18 13 17  5
    19  8  7 25 23
    20 11 10 24  4
    14 21 16 12  6

    14 21 17 24  4
    10 16 15  9 19
    18  8 23 26 20
    22 11 13  6  5
    2  0 12  3  7
    """

    assert not bingo(
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    )
    assert bingo(
        [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    )
    assert bingo(
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    )
    assert not bingo(
        [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    )

    assert solve1(test_input) == 4512
    assert solve2(test_input) == 1924

    puzzle = Puzzle(2021, 4)

    answer_1 = solve1(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve2(puzzle.input_data)
    print(answer_2)
    puzzle.answer_b = answer_2
