def parse(input_data):
    connections = dict()
    for connection in input_data.split('\n'):
        left, right = connection.split(' -> ')
        connections[right] = left
    return connections

def connect_wires(connections):

    while type(connections['a']) != int:
        for k, v in connections.items():
            try:
                if v.isnumeric():
                    connections[k] = int(v)
                if 'AND' in v:
                    parts = v.split()
                    if parts[0].isnumeric():
                        connections[k] = int(parts[0]) & connections[parts[2]]
                    else:
                        connections[k] = connections[parts[0]] & connections[parts[2]]
                if 'OR' in v:
                    parts = v.split()
                    if parts[0].isnumeric():
                        connections[k] = int(parts[0]) | connections[parts[2]]
                    else:
                        connections[k] = connections[parts[0]] | connections[parts[2]]
                if 'LSHIFT' in v:
                    parts = v.split()
                    connections[k] = connections[parts[0]] << int(parts[2])
                if 'RSHIFT' in v:
                    parts = v.split()
                    connections[k] = connections[parts[0]] >> int(parts[2])
                if 'NOT' in v:
                    parts = v.split()
                    connections[k] = ~connections[parts[1]] & 65535

                if connections.get(v):
                    connections[k] = connections[v]   
            except:
                continue

    return connections

def solve1(input_data):
    connections = parse(input_data)
    connections = connect_wires(connections)
    return connections['a']


def solve2(input_data):
    connections = parse(input_data)
    connections['b'] = solve1(input_data)
    connections = connect_wires(connections)
    return connections['a']

if __name__ == '__main__':
    from aocd.models import Puzzle

    puzzle = Puzzle(2015, 7)
    input_data = puzzle.input_data
    answer_1 = solve1(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve2(puzzle.input_data)
    print(answer_2)
    puzzle.answer_b = answer_2 