import numpy as np

def parse(input_data):
    rows = input_data.strip().split('\n')
    a = np.array([list(row) for row in rows])
    return np.where(a=='#', 1, 0)


def slant_path_indices(right_step, down_step, nrows, ncols):
    r = np.arange(0, nrows, down_step)
    c = np.arange(0, nrows*(right_step/down_step), right_step) % ncols
    return r, c.astype(int)
 
    
def solve(input_data, right_step, down_step):
    a = parse(input_data)
    inds = slant_path_indices(right_step, down_step, a.shape[0], a.shape[1])
    return a[inds].sum()


def solve_other_paths(input_data, other_paths):
    return np.product([solve(input_data, right_step, down_step) for right_step, down_step in other_paths])


if __name__ == "__main__":
    from aocd.models import Puzzle

    test_input = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""

    other_paths = [(1, 1),
                (3, 1),
                (5, 1),
                (7, 1),
                (1, 2)]

    assert solve(test_input, 3, 1) == 7
    assert solve(test_input, 1, 2) == 2
    assert solve_other_paths(test_input, other_paths) == 336

    puz3 = Puzzle(2020, 3)
    data = puz3.input_data
    puz3.answer_a = solve(data, 3, 1)
    puz3.answer_b = solve_other_paths(data, other_paths)