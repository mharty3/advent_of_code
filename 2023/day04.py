
def solve1(input_data):
    return sum([2**(score-1) for score in [[len(a.intersection(b)) for a, b in [[set(nums.split()) for nums in line.split(':')[1].split('|')]]][0] for line in input_data.splitlines()] if score > 0])


def cards_to_add(card, match_dict):
    return [card + 1 + i for i in range(match_dict[card])]


def solve2(input_data):
    matching_nums = [[len(a.intersection(b)) for a, b in [[set(nums.split()) for nums in line.split(':')[1].split('|')]]][0] for line in input_data.splitlines()]
    stack = [i + 1 for i, _ in enumerate(matching_nums)]
    match_dict =  {k: v for k, v in zip(stack, matching_nums)}
    card_count = 0

    while stack:
        up_card = stack.pop()
        stack.extend(cards_to_add(up_card, match_dict))
        card_count += 1
    
    return card_count


if __name__ == "__main__":
    from aocd.models import Puzzle

    puzzle = Puzzle(2023, 4)

    test_data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


    input_data = puzzle.input_data
    answer_1 = solve1(input_data)
    
    print(answer_1)
    puzzle.answer_a = answer_1

    assert solve2(test_data) == 30
    answer_2 = solve2(puzzle.input_data)
    print(answer_2)
    puzzle.answer_b = answer_2
