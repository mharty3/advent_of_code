import numpy as np
from aocd.models import Puzzle
puzzle = Puzzle(2023, 18)
input_data = puzzle.input_data

DIRECTIONS = {'L': np.array((-1,  0)),
              'R': np.array(( 1,  0)),
              'U': np.array(( 0,  1)),
              'D': np.array(( 0, -1))
              }

DIRECTIONS2 = {'2': np.array((-1,  0)),
              '0': np.array(( 1,  0)),
              '3': np.array(( 0,  1)),
              '1': np.array(( 0, -1))
              }


# a = 1
# b = 0
# c = min_x
# d = 0
# e = -1
# f = max_y

def parse(input_data):
   return [(row[0], int(row[1]), row[2]) for row in [row.split() for row in input_data.splitlines()]]



test_data = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""



# input_data = test_data

current_loc = np.array((0,0))
hole_boundary_pts = []
for dir, count, _ in parse(input_data):
   move = DIRECTIONS[dir]
#    print(current_loc, move)
   for i in range(count):
      current_loc = current_loc + move
    #   print(current_loc)
      hole_boundary_pts.append(current_loc)

hole_boundary_pts = np.array(hole_boundary_pts)

min_x, min_y = hole_boundary_pts.min(axis=0)
max_x, max_y = hole_boundary_pts.max(axis=0)

map_ = np.zeros((max_y-min_y + 1, max_x-min_x + 1), bool)

map_[(hole_boundary_pts.T[1]-max_y)*-1, hole_boundary_pts.T[0]-min_x] = True



map_ = np.insert(map_, 0, False, axis=1)
map_ = np.insert(map_, 0, False, axis=0)
map_ = np.append(map_, np.zeros((map_.shape[0], 1), bool), axis=1)
map_ = np.append(map_, np.zeros((1 ,map_.shape[1]), bool), axis=0)

        

from scipy import ndimage

map_fill = ndimage.binary_fill_holes(map_)
print(map_fill.sum())


import matplotlib.pyplot as plt
# plt.imshow(map_)
# plt.show()

# total = 0  
# for row in map_:
#     first = 0
#     last = len(row)
#     for val in row:
#        if val:
#           break
#        first += 1
#     for val in row[::-1]:
#        if val:
#           break
#        last -= 1
#     print(first, last, last-first)
#     total += (last - first)

# 134064 too high

def parse2(input_data):
   data = [(int(r[2:7], 16), r[-2]) for _, _, r in parse(input_data)]

      
   return data

hole_boundary_pts
from shapely import Polygon

# plt.plot(*p.boundary.xy)
# plt.plot(*p2.boundary.xy)
# plt.show()

data2 = parse2(input_data)
current_loc = np.array((0,0))
hole_boundary_pts = []
for line in data2:
   current_loc = current_loc + line[0] * DIRECTIONS2[line[1]]
   hole_boundary_pts.append(current_loc)


p = Polygon(hole_boundary_pts)
p2 = p.buffer(.5, join_style='mitre', mitre_limit=2)


