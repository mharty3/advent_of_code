
from collections import namedtuple




def solve1(input_data):
    visited=set((0,0))
    location = (0,0)
    for direction in input_data:
        if direction == '>':
            location = (location[0] + 1, location[1])
        if direction == '<':
            location = (location[0] - 1, location[1])
        if direction == '^':
            location = (location[0], location[1] + 1)
        if direction == 'v':
            location = (location[0], location[1] - 1)
        visited.add(location)
    return len(visited)


def solve2(input_data):
    location = (0,0)
    visited=set()
    visited.add(location)
    for direction in input_data[::2]:
        if direction == '>':
            location = (location[0] + 1, location[1])
        if direction == '<':
            location = (location[0] - 1, location[1])
        if direction == '^':
            location = (location[0], location[1] + 1)
        if direction == 'v':
            location = (location[0], location[1] - 1)
        visited.add(location)

    location = (0,0)
    for direction in input_data[1::2]:
        if direction == '>':
            location = (location[0] + 1, location[1])
        if direction == '<':
            location = (location[0] - 1, location[1])
        if direction == '^':
            location = (location[0], location[1] + 1)
        if direction == 'v':
            location = (location[0], location[1] - 1)
        visited.add(location)
    return len(visited)




        


if __name__ == '__main__':

    from aocd.models import Puzzle
    
    puzzle = Puzzle(2015, 3)
    answer_1 = solve1(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1


    answer_2 = solve2(puzzle.input_data)
    print(answer_2)
    puzzle.answer_b = answer_2 