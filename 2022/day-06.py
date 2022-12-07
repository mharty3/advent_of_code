from collections import deque

def first_data_loc(stream):
    for i, (bits) in enumerate( zip(stream,
                                    stream[1:],
                                    stream[2:],
                                    stream[3:]
                                    )):

        if len(set(bits)) == 4:
            return i + 4


def first_message_loc(stream, n=14):
    for i, _ in enumerate(stream):
        som = stream[i:i + n]
        if len(set(som)) == n:
            return i + n


def first_message_loc_deque(stream, n):
    test_bits = deque(stream[:n], maxlen=n)
    remaining_bits = deque(stream[n:])

    i = n
    while len(set(test_bits)) != n:
        test_bits.append(remaining_bits.popleft())
        i += 1
    return i


if __name__ == '__main__':

    assert first_data_loc('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5
    assert first_message_loc('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 19

    assert first_message_loc_deque('bvwbjplbgvbhsrlpgdmjqwftvncz', n=4) == 5
    assert first_message_loc('mjqjpqmgbljsphdztnvjfqwrcgsmlb', n=14) == 19

    from aocd.models import Puzzle
    puzzle = Puzzle(2022, 6)

    answer_1 = first_data_loc(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = first_message_loc(puzzle.input_data)
    print(answer_2)
    puzzle.answer_b = answer_2