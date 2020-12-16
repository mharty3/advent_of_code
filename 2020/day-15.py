
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



assert solve1('0,3,6') == 436
assert solve1('1,3,2') == 1
assert solve1('1,2,3') == 27
assert solve1('2,3,1') == 78

