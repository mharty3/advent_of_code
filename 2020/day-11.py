def add_ring_of_floor(Z):
    # add additional floor around the border
    # to make it easier to count neighbors
    for z in Z:
        z.insert(0, '.')
        z.append('.')
    Z.insert(0, ['.' for _ in Z[0]])
    Z.append(['.' for _ in Z[0]])
    return Z


def parse(input_data):
    Z = [list(line.strip()) for line in input_data.split('\n')]
    return add_ring_of_floor(Z)


def count_neighbors(y, x, Z, search='#'):
    # account for added floor
    x += 1
    y += 1

    above = Z[y-1][x-1:x+2]
    bottom = Z[y+1][x-1:x+2]
    left = Z[y][x-1]
    right = Z[y][x+1]
    return sum([seat.count(search) for seat in [above, left, right, bottom]])


def count_neighbors_matrix(Z):
    neighbors_Z = []
    for y, row in enumerate(Z[1:-1]):
        new_row = []
        for x, val in enumerate(row[1:-1]):
            if val in ['L', '#']:
                new_row.append(count_neighbors(y, x, Z))
            else:
                new_row.append('.')
        neighbors_Z.append(new_row)
    return add_ring_of_floor(neighbors_Z)

def iteration(Z):
    neighbor_count_matrix = count_neighbors_matrix(Z)
    new_Z = []
    change_count = 0
    for y, row in enumerate(zip(Z, neighbor_count_matrix)):
        new_row = []
        for x, (seat, count) in enumerate(zip(*row)):
            if seat == 'L' and count == 0:
                new_row.append('#')
                change_count += 1
            elif seat == '#' and count >= 4:
                new_row.append('L')
                change_count += 1
            else:
                new_row.append(seat)
        new_Z.append(new_row)
    return new_Z, change_count

def run(Z):
    change_count = 1
    while change_count:
        Z, change_count = iteration(Z)
    return(Z)


def solve1(input_data):
    Z = parse(input_data)
    Z = run(Z)
    return sum([row.count('#') for row in Z])


        


if __name__ == "__main__":
    from aocd.models import Puzzle

    test_data = """L.LL.LL.LL
                    LLLLLLL.LL
                    L.L.L..L..
                    LLLL.LL.LL
                    L.LL.LL.LL
                    L.LLLLL.LL
                    ..L.L.....
                    LLLLLLLLLL
                    L.LLLLLL.L
                    L.LLLLL.LL"""

    Z = parse(test_data)

    assert count_neighbors(0, 0, Z, search='L') == 2
    assert count_neighbors(1, 0, Z, search='L') == 3
    assert count_neighbors(9, 9, Z, search='L') == 2
    assert count_neighbors(1, 9, Z, search='L') == 3

    assert solve1(test_data) == 37

    puz11 = Puzzle(2020, 11)
    data = puz11.input_data
    puz11.answer_a = solve1(data)
    # puz11.answer_b = solve2(data)

