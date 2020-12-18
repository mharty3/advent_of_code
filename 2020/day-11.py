def add_wall(Z):
    # add a wall around the border
    # to make it easier to count neighbors
    for z in Z:
        z.insert(0, "|")
        z.append("|")
    Z.insert(0, ["-" for _ in Z[0]])
    Z.append(["-" for _ in Z[0]])
    return Z


def parse(input_data):
    Z = [list(line.strip()) for line in input_data.split("\n")]
    return add_wall(Z)


def count_neighbors(y, x, Z, search="#"):
    # account for added wall
    x += 1
    y += 1

    above = Z[y - 1][x - 1 : x + 2]
    bottom = Z[y + 1][x - 1 : x + 2]
    left = Z[y][x - 1]
    right = Z[y][x + 1]
    return sum([seat.count(search) for seat in [above, left, right, bottom]])


def line_of_sight_search(y, x, Z, y_increment, x_increment, search="#"):
    seat = "."
    while seat == ".":
        y += y_increment
        x += x_increment
        seat = Z[y][x]
        if seat == search:
            return 1
    return 0


def count_visible_neighbors(y, x, Z, search="#"):
    # account for added wall
    x += 1
    y += 1

    neighbor_count = 0
    directions = [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (-1, -1), (1, 1)]
    for y_inc, x_inc in directions:
        neighbor_count += line_of_sight_search(y, x, Z, y_inc, x_inc, search)
    return neighbor_count


def count_neighbors_matrix(Z, method="adjacent"):
    neighbors_Z = []
    for y, row in enumerate(Z[1:-1]):
        new_row = []
        for x, val in enumerate(row[1:-1]):
            if val in ["L", "#"]:
                if method == "adjacent":
                    new_row.append(count_neighbors(y, x, Z))
                elif method == "line of sight":
                    new_row.append(count_visible_neighbors(y, x, Z))
                else:
                    raise ValueError
            else:
                new_row.append(".")
        neighbors_Z.append(new_row)
    return add_wall(neighbors_Z)


def iteration(Z, method="adjacent"):
    if method == "adjacent":
        max_neighbors = 4
    elif method == "line of sight":
        max_neighbors = 5
    else:
        raise ValueError

    neighbor_count_matrix = count_neighbors_matrix(Z, method)
    new_Z = []
    change_count = 0
    for y, row in enumerate(zip(Z, neighbor_count_matrix)):
        new_row = []
        for x, (seat, count) in enumerate(zip(*row)):
            if seat == "L" and count == 0:
                new_row.append("#")
                change_count += 1
            elif seat == "#" and count >= max_neighbors:
                new_row.append("L")
                change_count += 1
            else:
                new_row.append(seat)
        new_Z.append(new_row)
    return new_Z, change_count


def run(Z, method="adjacent"):
    change_count = 1
    while change_count:
        Z, change_count = iteration(Z, method)
    return Z


def solve1(input_data):
    Z = parse(input_data)
    Z = run(Z)
    return sum([row.count("#") for row in Z])


def solve2(input_data):
    Z = parse(input_data)
    Z = run(Z, "line of sight")
    return sum([row.count("#") for row in Z])


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

    assert count_neighbors(0, 0, Z, search="L") == 2
    assert count_neighbors(1, 0, Z, search="L") == 3
    assert count_neighbors(9, 9, Z, search="L") == 2
    assert count_neighbors(1, 9, Z, search="L") == 3

    assert count_visible_neighbors(0, 0, Z, search="L") == 3

    assert solve1(test_data) == 37
    assert solve2(test_data) == 26

    puz11 = Puzzle(2020, 11)
    data = puz11.input_data
    puz11.answer_a = solve1(data)
    puz11.answer_b = solve2(data)
