
def parse(input_data):
    translated = (input_data.replace('A', 'rock')
                        .replace('B', 'paper')
                        .replace('C', 'scissors')
                        .replace('X', 'rock')
                        .replace('Y', 'paper')
                        .replace('Z', 'scissors')
                    )
    return [game.split() for game in translated.splitlines()]


def game(p1, p2):
    """ return the points awarded for the second player"""

    if p2 == 'rock':
        choice_pts = 1
    elif p2 == 'paper':
        choice_pts = 2
    elif p2 == 'scissors':
        choice_pts = 3
    else:
        raise ValueError

    if p1 == p2:
        return 3 + choice_pts

    if p1 == 'rock' and p2 == 'paper':
        return 6 + choice_pts
    
    if p1 == 'rock' and p2 == 'scissors':
        return 0 + choice_pts

    if p1 == 'paper' and p2 == 'scissors':
        return 6 + choice_pts
    
    if p1 == 'paper' and p2 == 'rock':
        return 0 + choice_pts

    if p1 == 'scissors' and p2 == 'rock':
        return 6 + choice_pts

    if p1 == 'scissors' and p2 == 'paper':
        return 0 + choice_pts

def solve1(input_data):
    parsed = parse(input_data)
    return sum([game(*plays) for plays in parsed])


if __name__ == '__main__':

    test_data = """A Y
B X
C Z
"""
    
    assert solve1(test_data) == 15
    # assert solve2(test_data) == 45000

    from aocd.models import Puzzle
    puzzle = Puzzle(2022, 2)
    answer_1 = solve1(puzzle.input_data)

    print(answer_1)
    puzzle.answer_a = answer_1

    # answer_2 = solve2(puzzle.input_data)
    # puzzle.answer_b = answer_2





