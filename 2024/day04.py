def parse(input_data):
    lines = input_data.splitlines()
    dummy_row = ['.'] * (len(lines[0]) + 2)
    
    return [dummy_row] +\
           [['.'] + list(line) + ['.'] for line in lines] +\
           [dummy_row]

test_data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

input_data = test_data
grid = parse(input_data)
valid_word_starts = [] # r, c, prev_letter

next_letters = {'X': 'M',
                'M': 'A',
                'A': 'S'}

directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1)]

for r, row in enumerate(grid):
    for c, letter in enumerate(row):
        if letter == 'X':
            valid_word_starts.append((r, c, 'X'))

total = 0
# for r, c, prev_letter in valid_word_starts:
while valid_word_starts:
    r, c, prev_letter = valid_word_starts.pop()
    if prev_letter == 'S':
        total += 1
        continue
    for dr, dc in directions:
        nr = r + dr
        nc = c + dc
        if grid[nr][nc] == next_letters[prev_letter]:
            valid_word_starts.append((nr, nc, grid[nr][nc]))

print(total)
