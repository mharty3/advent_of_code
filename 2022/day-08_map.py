# %%
import numpy as np
import matplotlib.pyplot as plt
from aocd.models import Puzzle
puzzle = Puzzle(2022, 8)

def parse(input_data):
    return [[int(tree) for tree in row] for row in input_data.splitlines()]

a = np.array(parse(puzzle.input_data))
plt.imshow(a)
plt.colorbar()
plt.savefig('day-08_map.png')

# %%
