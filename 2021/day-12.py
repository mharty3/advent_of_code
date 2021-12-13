from typing import DefaultDict, TypeVar, Dict, List
from collections import Counter, deque, defaultdict

Location = TypeVar("Location")


def parse(input_data: str) -> Dict[Location, List[Location]]:
    edges = dict()

    for line in input_data.splitlines():
        node1, node2 = line.strip().split("-")
        if node1 in edges:
            edges[node1].append(node2)
        else:
            edges[node1] = [node2]

        if node2 in edges:
            edges[node2].append(node1)
        else:
            edges[node2] = [node1]

    edges = {
        k: [v for v in vals if v != "start"] for k, vals in edges.items() if k != "end"
    }
    return edges


class SimpleGraph:
    def __init__(self, edges):
        self.edges: Dict[Location, List[Location]] = edges

    def neighbors(self, id: Location) -> List[Location]:
        return self.edges.get(id, [])


def bfs(graph):
    """Use breadth first search to find all valid paths through the caves
    Resources:
    https://www.redblobgames.com/pathfinding/a-star/implementation.html
    https://www.geeksforgeeks.org/print-paths-given-source-destination-using-bfs/
    """
    valid_paths = []
    queue = deque()
    queue.append(["start"])

    while queue:
        current_path = queue.popleft()

        if current_path[-1] == "end":
            valid_paths.append(current_path)

        for next in graph.neighbors(current_path[-1]):
            if next not in current_path or next.isupper():
                new_path = current_path.copy()
                new_path.append(next)
                queue.append(new_path)

    return valid_paths


def bfs2(graph):
    """This works but is very slow and memory intensive for the real data"""
    valid_paths = []
    queue = deque()
    queue.append(["start"])

    while queue:
        current_path = queue.popleft()

        if current_path[-1] == "end" and current_path not in valid_paths:
            valid_paths.append(current_path)

        for next in graph.neighbors(current_path[-1]):
            # count how many of each lowercase value there are
            lowers = [loc for loc in current_path if loc.islower()]
            c = Counter(lowers)
            no_doubles = c.most_common()[0][1] == 1

            if no_doubles or next not in current_path or next.isupper():
                new_path = current_path.copy()
                new_path.append(next)
                queue.append(new_path)

    return len(valid_paths)


def solve1(input_data):
    graph = SimpleGraph(parse(input_data))
    return len(bfs(graph))


def solve2(input_data):
    graph = SimpleGraph(parse(input_data))
    paths = bfs2(graph)
    return paths


if __name__ == "__main__":
    from aocd.models import Puzzle

    test_data = """start-A
    start-b
    A-c
    A-b
    b-d
    A-end
    b-end"""

    test_data2 = """dc-end
    HN-start
    start-kj
    dc-start
    dc-HN
    LN-dc
    HN-end
    kj-sa
    kj-HN
    kj-dc"""

    test_data3 = """fs-end
    he-DX
    fs-he
    start-DX
    pj-DX
    end-zg
    zg-sl
    zg-pj
    pj-he
    RW-he
    fs-DX
    pj-RW
    zg-RW
    start-pj
    he-WI
    zg-he
    pj-fs
    start-RW"""

    assert solve1(test_data) == 10
    assert solve1(test_data2) == 19
    assert solve1(test_data3) == 226

    assert solve2(test_data) == 36

    p = solve2(test_data2)
    assert solve2(test_data2) == 103
    assert solve2(test_data3) == 3509

    puzzle = Puzzle(2021, 12)

    answer_1 = solve1(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve2(puzzle.input_data)
    print(answer_2)
    puzzle.answer_b = answer_2
