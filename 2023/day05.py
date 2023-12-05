
from aocd.models import Puzzle

puzzle = Puzzle(2023, 5)


input_data = puzzle.input_data

def process_single_map(seed, map_spec):
    for dest, start, length in map_spec:
        delta = dest - start
        if seed in range(start, start+length):
            return seed + delta
    return seed


blocks = input_data.split('\n\n')
seeds = [int(seed) for seed in blocks[0].split()[1:]]
map_specs = blocks[1:]

maps = []

for map_spec in map_specs:
    map_data_rows = [map_row.split() for map_row in map_spec.split(':\n')[1].split('\n')]
    map_data = [[int(val) for val in row] for row in map_data_rows]
    maps.append(map_data)


final_vals = []
for seed in seeds:
    seed_val = seed
    for m in maps:
        seed_val = process_single_map(seed_val, m)
    final_vals.append(seed_val)

print(min(final_vals))
