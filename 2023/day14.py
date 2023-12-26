import numpy as np
from aocd.models import Puzzle
puzzle = Puzzle(2023, 14)


def solve1(input_data):
    data = list(zip(*[list(r) for r in input_data.splitlines()]))
    rock_indices = []
    for col in data:
        next_open_space = 0
        for i, val in enumerate(col):
            if val == 'O':
                rock_indices.append(len(col) - next_open_space)
                next_open_space += 1
            elif val == '#':
                next_open_space = i + 1

    return sum(rock_indices)


input_data = puzzle.input_data
puzzle.answer_a = solve1(input_data)


import matplotlib.pyplot as plt
# plt.imshow(A[0])
# plt.show()
# plt.imshow(A[1])
# plt.show()


def calc_load(A):
    bool_A = np.array(A) == 'O'
    return (A.shape[0] - bool_A.nonzero()[0]).sum()


def tilt_left(A):
    B = np.empty_like(A) # make copy of array A and fill it in with the new values
    for r, row in enumerate(A):
        next_open_space = 0 # keep track of the next space a rock could go in a row
        for c, val in enumerate(row):
            if val == 'O':
                B[r, next_open_space] = 'O' # put the rock in the space
                next_open_space += 1 
            elif val == '#':
                next_open_space = c + 1 # update next open space to the space after the wall
                B[r, c ] = '#'
    return B


def tilt_W(A):
    return tilt_left(A)

def tilt_E(A):
    # flip it, tilt left, flip it back
    return np.fliplr(tilt_left(np.fliplr(A)))

def tilt_N(A):
    # transpose (ie rotate ccw), tilt left, transpose back
    return tilt_left(A.T).T

def tilt_S(A):
    # tranpose, flip, tilt left, flip back, transpose back
    return np.fliplr(tilt_left(np.fliplr(A.T))).T

def spin_cycle(A):
    # do all the tilts
    return tilt_E(tilt_S(tilt_W(tilt_N(A))))


A = np.array([list(r) for r in input_data.splitlines()])

loads = []
for i in range(200):
    A = spin_cycle(A)
    loads.append(calc_load(A))
    print(calc_load(A))

plt.plot(loads)
plt.show()

# visually look at graph and pick out two successive peaks in the cycle
# 106, 96141
# 117, 96141
p = 117 - 106
answer = loads[106 + (1000000000 - 106) % p]

