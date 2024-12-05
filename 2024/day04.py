def parse(input_data):
    lines = input_data.splitlines()
    dummy_row = ['.'] * (len(lines[0]) + 2)
    
    return [dummy_row] +\
           [['.'] + list(line) + ['.'] for line in lines] +\
           [dummy_row]


def solve1(input_data):
    grid = parse(input_data)
    valid_word_starts = [] # r, c, prev_letter, dr, dc

    next_letters = {'X': 'M',
                    'M': 'A',
                    'A': 'S'}

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]

    for r, row in enumerate(grid):
        for c, letter in enumerate(row):
            if letter == 'X':
                valid_word_starts.append((r, c, 'X', 0, 0))

    total = 0
    # for r, c, prev_letter in valid_word_starts:
    while valid_word_starts:
        r, c, prev_letter, dr, dc = valid_word_starts.pop()
        if prev_letter == 'S':
            total += 1
            continue

        elif prev_letter == 'X':
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if grid[nr][nc] == 'M':
                    valid_word_starts.append((nr, nc, 'M', dr, dc))
        else:
            nr = r + dr
            nc = c + dc
            if grid[nr][nc] == next_letters[prev_letter]:
                valid_word_starts.append((nr, nc, next_letters[prev_letter], dr, dc))

    
    return total

def solve2(input_data):
    grid = parse(input_data)
    total = 0

    x1 = [-1, -1, 1, 1]
    x2 = [1, -1, -1, 1]

    x_centers = []

    for r, row in enumerate(grid):
        for c, letter in enumerate(row):
            if letter == 'A':
                x_centers.append((r, c))
    
    for r, c in x_centers:
        i, j, k, l = x1
        leg1 = set([grid[r + i][c + j], grid[r + k][c + l]])

        i, j, k, l = x2
        leg2 = set([grid[r + i][c + j], grid[r + k][c + l]])

        leg = set(['M', 'S'])
        if leg == leg1 == leg2:
            total += 1
    return total

if __name__ == '__main__':
    from aocd.models import Puzzle

    puzzle = Puzzle(2024, 4)
    input_data = puzzle.input_data

    answer_1 = solve1(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve2(input_data)
    
    print(answer_2)
    puzzle.answer_b = answer_2