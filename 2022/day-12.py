import networkx as nx
import string


def parse(input_data):
    val_map = {k: v for k, v in zip(string.ascii_lowercase, range(26))}
    val_map['S'] = 0
    val_map['E'] = 25
    edges = dict()

    # Parse input into list of lists
    grid = [
        [step for step in list(line.strip())] for line in input_data.splitlines()
    ]

    # max rows and cols
    nr = len(grid)
    nc = len(grid[0])

    # for each node, find a list of all valid neighbors
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == "S":
                start = (r, c)
                h = 0
            elif col == 'E':
                end = (r, c)
                h = 26
            else:
                h = val_map[col]

            potential_neighbors = [(r+1, c), (r-1, c), (r, c-1), (r, c+1)]
            valid_neighbors = []
            for neighbor in potential_neighbors:
                # check if it's in bounds
                if neighbor[0] >= 0 and neighbor[0] < nr and neighbor[1] >= 0 and neighbor[1] < nc:
                    # check if step up is within one letter of elevation
                    if val_map[grid[neighbor[0]][neighbor[1]]] - h <= 1:
                        valid_neighbors.append(neighbor)
            edges[(r, c)] = valid_neighbors
    
    return edges, start, end


def solve1(input_data: str) -> int:
    edges, start, end = parse(input_data)
    # create a directed graph from the dict of edges
    graph = nx.DiGraph(edges)
    # use networkx to find the shortest path
    return(nx.shortest_path_length(graph, source=start, target=end))


if __name__ == '__main__':
    
    from aocd.models import Puzzle
    import networkx as nx

    sample_data = """Sabqponm
                    abcryxxl
                    accszExk
                    acctuvwj
                    abdefghi"""
    
    puzzle = Puzzle(2022, 12)
    assert solve1(sample_data) == 31

    answer_1 = solve1(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1
 
