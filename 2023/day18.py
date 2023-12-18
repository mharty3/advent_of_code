from aocd.models import Puzzle
import numpy as np
from shapely import Polygon

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


def parse(input_data):
   return [(row[0], int(row[1]), row[2]) for row in [row.split() for row in input_data.splitlines()]]


def parse1(input_data):
   return [(int(r[1]), DIRECTIONS[r[0]]) for r in parse(input_data)]


def parse2(input_data):
   return [(int(r[2:7], 16), DIRECTIONS2[r[-2]]) for _, _, r in parse(input_data)]
   

def solve(input_data, part):
   if part == 1:
      data = parse1(input_data)
   elif part == 2:
      data = parse2(input_data)

   # construct list of boundary pts
   hole_boundary_pts = []
   current_loc = np.array((0,0))
   for line in data:
      current_loc = current_loc + line[0] * line[1]
      hole_boundary_pts.append(current_loc)
   
   # create a polygon, buffer by .5 for center pt to corner pt
   p = Polygon(hole_boundary_pts).buffer(.5, join_style='mitre', mitre_limit=2)
   
   # calculate area
   return int(p.area)