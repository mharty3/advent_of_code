
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

# pt2
# run the maps in reverse. start with the "location value" and work backwards to the seed value
# start at location zero, and work up until the first valid seed value is found, it is the answer
maps2 = list(reversed(maps))

def process_single_map2(seed, map_spec):
    for start, dest, length in map_spec:
        delta = dest - start
        if seed in range(start, start+length):
            return seed + delta
    return seed



import itertools
seed_ranges = []
seed_pairs = list(itertools.pairwise(seeds))
for start, length in seed_pairs[::2]:
    seed_ranges.append(range(start, start + length))

def solve2():
    for i in range(1_000_000_000_000):
        val = i
        for m in maps2:
            val = process_single_map2(val, m)
        for r in seed_ranges:
            if val in r:
                return i

import time
start = time.time()
print(solve2())
print(time.time() - start)


test_data = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""



# input_data = test_data
# maps = [sorted(m, key= lambda m: m[1]) for m in maps]



# # 82, 84, 84, 77, 45, 46, 46
# pandas solution with plot to try to figure out a clever way to solve pt two. never figured anything out
ms = []
for map_ in maps:
    m = []
    for range_ in map_:
        dest, start, length = range_
        m.append([start, start+length, dest - start])
    ms.append(m)




import pandas as pd
seeds_all = list()

df = pd.DataFrame(data=seeds_all, columns=['seeds'])
df = df.assign(soil=lambda df: df.seeds.map(lambda s: process_single_map(s, maps[0])),
               fert=lambda df: df.soil.map(lambda s: process_single_map(s, maps[1])),
               water=lambda df: df.fert.map(lambda s: process_single_map(s, maps[2])),
               light=lambda df: df.water.map(lambda s: process_single_map(s, maps[3])),
               temp=lambda df: df.light.map(lambda s: process_single_map(s, maps[4])),
               humidity=lambda df: df.temp.map(lambda s: process_single_map(s, maps[5])),
               location=lambda df: df.humidity.map(lambda s: process_single_map(s, maps[6])),
               )

print(df.location.min())

import matplotlib.pyplot as plt
df.T.plot(legend=False)
plt.show()