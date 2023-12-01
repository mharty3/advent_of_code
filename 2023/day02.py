
from numpy import prod

def parse(input_data) -> dict[int, list[dict[str, int]]]:
    games = dict()
    for game in input_data.splitlines():
        id = int(game.split(':')[0].split()[1])
        draw_list = list()
        for draws in game.split(': ')[1].split('; '):
            c = dict()
            for draw in draws.split(', '):
                count, color = draw.split()
                c[color] = int(count)
            draw_list.append(c)
        games[id] = draw_list

    return games


def is_valid_game(game, bag):
    for draw in game:
        for color, count in draw.items():
            if count > bag.get(color, 0):
                return False
    return True


def solve1(input_data):
    games = parse(input_data)
    bag = {'red': 12, 'green': 13, 'blue': 14}
    total = 0
    for id, game in games.items():
        if is_valid_game(game, bag):
            total += id
    return total


def solve2(input_data):
    games = parse(input_data)

    total = 0
    for id, game in games.items():
        required_cubes = dict()
        for draw in game:
            for color, count in draw.items():
                if color not in required_cubes:
                    required_cubes[color] = count
                else:
                    if required_cubes[color] < count:
                        required_cubes[color] = count
        total += prod(list(required_cubes.values()))
    return total

    
if __name__ == '__main__':
    from aocd.models import Puzzle

    puzzle = Puzzle(2023, 2)
    input_data = puzzle.input_data
    answer_1 = solve1(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve2(input_data)
    
    print(answer_2)
    puzzle.answer_b = answer_2
