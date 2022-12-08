import os
from pathlib import Path

from aocd.models import Puzzle
puzzle = Puzzle(2022, 7)
input_data = puzzle.input_data

os.chdir(Path(__file__).parent)
root = 'day-07_root'
os.system(f'mkdir {root}')
for inst in input_data.strip().replace('/', root).splitlines():
    if inst.startswith('$ cd'):
        os.chdir(inst.replace('$ cd ', ''))
    elif inst.startswith('dir'):
        os.system(f'mk{inst}')
    elif inst[0].isdigit():
        size, name = inst.split()
        os.system(f'echo {size} > {name}')

os.chdir(Path(__file__).parent)


dir_sizes = dict()
path = Path(root).parent
for p in path.rglob("*"):
     if p.is_dir():
        dir_size = []
        for sub_p in p.rglob("*"):
            if sub_p.is_file():
                with open(sub_p) as f:
                    dir_size.append(int(f.read()))
        dir_sizes[p] = sum(dir_size)

print(sum([s for s in dir_sizes.values() if s <= 100000]))


total_space = 70_000_000
needed_space = 30_000_000
used_space = dir_sizes[Path(root)]
unused_space = total_space - used_space
to_delete = needed_space - unused_space

print(min([dir for dir in dir_sizes.values() if dir > to_delete]))

