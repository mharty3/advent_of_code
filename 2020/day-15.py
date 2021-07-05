
def solve1(input_data):
    sequence = [int(i) for i in input_data.strip().split(',')]
    seen = set(sequence[:-1])
    turn = 1
    while len(sequence) < 2020:
        last = sequence[-1]
        if last not in seen:
            sequence.append(0)
            current=0
            seen.add(last)
        else:
            diff = sequence[-2::-1].index(last) + 1
            sequence.append(diff)
    return sequence[-1]

def solve2(input_data):
    sequence = [int(i) for i in input_data.strip().split(',')]
    seen = set(sequence[:-1])
    last_index = {n: i+1 for (i,n) in enumerate(sequence)}
    turn = len(sequence)
    last = sequence[-1]
    while turn <= 10:
        if last not in seen:
            seen.add(last)
            diff = turn - last_index[last]
            last = 0
        else:
            last = diff
        last_index[last] = turn
        turn += 1
        print(turn, last)
    return last


def solve2(input_data):
    sequence = [int(i) for i in input_data.strip().split(',')]
    last_index = {n: i+1 for (i,n) in enumerate(sequence)}
    last = sequence[-1]
    turn = len(sequence) - 1
    
    while turn <= 2000:
        get = last_index.get(last)
        if get:
            last_index[last] = turn - get
        else:
            last_index[0] = turn
            last = 0





assert solve2('0,3,6') == 436
assert solve1('1,3,2') == 1
assert solve1('1,2,3') == 27
assert solve1('2,3,1') == 78

assert solve2('0,3,6') == 436