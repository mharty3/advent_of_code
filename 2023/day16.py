import numpy as np
from dataclasses import dataclass

from aocd.models import Puzzle
puzzle = Puzzle(2023, 16)
input_data = puzzle.input_data


@dataclass
class Ray:
    position: tuple
    direction: tuple

    def step(self):
        # vector add position and direction
        self.position = tuple([p + d for p, d in zip(self.position, self.direction)])



mirrors = {'/': {( 0,  1): (-1,  0), # moving to the right: leaves mirror going up
                 ( 0, -1): ( 1,  0), # moving left: leaves down
                 (-1,  0): ( 0,  1), 
                 ( 1,  0): ( 0, -1)
                },

         '\\': {( 0,  1): ( 1,  0),
                ( 0, -1): (-1,  0),
                (-1,  0): ( 0, -1),
                ( 1,  0): ( 0,  1)
                }     
          }    


grid = np.array([list(row) for row in input_data.splitlines()])


def count_energized_tiles(starting_ray=Ray(position=(0, 0), direction=(0, 1))):
    live_rays = [starting_ray]
    visited_states = []

    while live_rays:
        active_ray = live_rays.pop()

        # check in bounds
        if not ((0 <= active_ray.position[0] < grid.shape[0]) and 
                (0 <= active_ray.position[1] < grid.shape[1])): 
            continue

        grid_val = grid[active_ray.position]


        if grid_val in ['\\', '/']:
            active_ray.direction = mirrors[grid_val][active_ray.direction]

        elif grid_val == '|' and active_ray.direction[0] == 0:
            live_rays.append(Ray(position=active_ray.position, direction=(-1, 0)))
            live_rays.append(Ray(position=active_ray.position, direction=( 1, 0)))
            continue
        
        elif grid_val == '-' and active_ray.direction[1] == 0:
            live_rays.append(Ray(position=active_ray.position, direction=(0, -1)))
            live_rays.append(Ray(position=active_ray.position, direction=(0,  1)))
            continue
        

        if (active_ray.position, active_ray.direction) not in visited_states: 
            
            visited_states.append((active_ray.position, active_ray.direction))
            active_ray.step()
            live_rays.append(active_ray)

    return len(set([p for  p, d in visited_states]))


def solve2():
    borders = []
    for r in range(grid.shape[0]):
        borders.append(Ray(position=(r, 0), direction=(0, 1)))
        borders.append(Ray(position=(r, -1), direction=(0,-1)))

    for c in range(grid.shape[1]):
        borders.append(Ray(position=(0, c), direction=(1, 0))) 
        borders.append(Ray(position=(-1, c), direction=(-1, 0)))
    
    return max([count_energized_tiles(ray) for ray in borders])


puzzle.answer_a = count_energized_tiles()
puzzle.answer_b = solve2()