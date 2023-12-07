# A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2
# e  d  c  b  a

from collections import Counter
import re


def score_hand(hand):
    """
    Create 6 digit base 15 number and convert to int

    first digit is based on hand type:
    5oak: 8
    4oak: 6
    FH  : 5
    3oak: 4
    2p  : 3
    1p  : 2
    hk  : 0
    """

    card_counts = Counter(hand)
    most_common_count = card_counts.most_common()[0][1]
    
    score = (most_common_count - 1) * 2
    if score == 4 and 2 in card_counts.values(): # full house
        score += 1
    elif score == 2 and card_counts.most_common()[1][1] == 2: # two pair
        score += 1

    return int(str(score) + hand, 15)


def solve1(input_data):
    trans_table = {ord('A'):'e', ord('K'):'d', ord('Q'):'c', ord('J'): 'b', ord('T'):'a'}
    input_data = input_data.translate(trans_table)
    
    players = [player.split() for player in input_data.splitlines()]
    players = [[score_hand(hand), int(bid)] for hand, bid in players]
    sorted_players = sorted(players, key=lambda p: p[0])
    
    total_winnings = 0
    for i, (score, bid) in enumerate(sorted_players):
        total_winnings += (i + 1) * bid

    return total_winnings



if __name__ == "__main__":
    from aocd.models import Puzzle

    puzzle = Puzzle(2023, 7)

    test_data = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

    assert solve1(test_data) == 6440

    input_data = puzzle.input_data
    answer_1 = solve1(input_data)
    
    print(answer_1)
    puzzle.answer_a = answer_1

    # assert solve2(test_data) == 71503
    
    # answer_2 = solve2(puzzle.input_data)
    # print(answer_2)
    # puzzle.answer_b = answer_2
