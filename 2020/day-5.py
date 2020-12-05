import numpy as np


def parse(input_data):
    lines = input_data.strip().split('\n')
    chars_to_swap = {'B': '1',
                     'F': '0',
                     'R': '1',
                     'L': '0'}
    seats = [l.strip().translate(str.maketrans(chars_to_swap)) for l in lines]
    return seats


def decode_row_col(seat):
    row = int(seat[:7], 2)
    col = int(seat[7:], 2)
    seat_id = row * 8 + col
    
    return row, col, seat_id


def seat_array(input_data):
    seats = parse(input_data)
    return np.array([decode_row_col(seat) for seat in seats])


def solve1(input_data):
    return np.max(seat_array(input_data), axis=0)[2]    


def solve2(input_data):
    ids = seat_array(input_data)[:,2]
    
    seats = range(ids.min(), ids.max())
    for seat in seats:
        if seat not in seat_array(input_data)[:,2]:
            return seat

if __name__ == "__main__":
    from aocd.models import Puzzle

    test_data = """BFFFBBFRRR
    FFFBBBFRRR
    BBFFBBFRLL
    """

    assert parse(test_data)[0] == '1000110111'
    assert decode_row_col('1000110111') == (70, 7, 567)
    assert solve1(test_data) == 820

    puz5 = Puzzle(2020, 5)
    data = puz5.input_data
    puz5.answer_a = solve1(data)
    puz5.answer_b = solve2(data)