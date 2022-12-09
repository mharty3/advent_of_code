
def parse(input_data):
    return [[int(tree) for tree in row] for row in input_data.splitlines()]


def solve1(input_data):
    forest = parse(input_data)
    forest_t = [list(i) for i in zip(*forest)]
    count = 2 * len(forest) + 2 * (len(forest[0]) - 2)

    for i, row in enumerate(forest[1:-1], start=1):
        for j, tree in enumerate(row[1:-1], start=1):
            look_left = forest[i][:j]
            look_right = forest[i][j + 1:]
            look_up = forest_t[j][:i]
            look_down = forest_t[j][i + 1:]

            if (tree > max(look_left) 
                  or tree > max(look_right)
                  or tree > max(look_up) 
                  or tree > max(look_down)
                  ):

                count += 1
    return count


def tree_viz_count(view, height):
    count = 0
    for tree in view:
        count += 1
        if tree >= height:
            return count 
    return count


def solve2(input_data):
    forest = parse(input_data)
    forest_t = [list(i) for i in zip(*forest)]
    scenic_scores = []

    for i, row in enumerate(forest):
        for j, tree in enumerate(row):
            look_left = forest[i][:j]
            look_right = forest[i][j + 1:]
            look_up = forest_t[j][:i]
            look_down = forest_t[j][i + 1:]

            left_count = tree_viz_count(reversed(look_left), tree)
            right_count = tree_viz_count(look_right, tree)
            up_count = tree_viz_count(reversed(look_up), tree)
            down_count = tree_viz_count(look_down, tree)

            score = left_count * right_count * up_count * down_count

            scenic_scores.append(score)

    return max(scenic_scores)


if __name__ == '__main__':
    test_data = """30373
25512
65332
33549
35390"""

    assert solve1(test_data) == 21
    assert solve2(test_data) == 8


    from aocd.models import Puzzle
    puzzle = Puzzle(2022, 8)

    answer_1 = solve1(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve2(puzzle.input_data)
    print(answer_2)
    puzzle.answer_b = answer_2


