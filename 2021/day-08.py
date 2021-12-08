# --- Day 8: Seven Segment Search ---
# https://adventofcode.com/2021/day/8


def solve1(input_data):
    count = 0
    for line in input_data.split('\n'):
        signal, output = line.split(' | ')
        count += len([segments for segments in output.split()
                if len(segments) in [2, 4, 3, 7]])
    return count


def solve2(input_data):
    data = []
    total = 0
    for line in input_data.split('\n'):
        signal, output = line.split(' | ')
        output = output.split()
        
        signal = {''.join(sorted(s)): '' for s in signal.split()}
        solved = {}
        
        sigs = list(signal.keys())
        for key in sigs:
            if len(key) == 2:
                signal[key] = 1
                solved[1] = key
            if len(key) == 4:
                signal[key] = 4
                solved[4] = key
            if len(key) == 3:
                signal[key] = 7
                solved[7] = key
            if len(key) == 7:
                signal[key] = 8
                solved[8] = key

        signal['BD'] = set(solved[4]).difference(set(solved[1])) 


        sigs = list(signal.keys())
        
        for key in sigs:
            if len(key) == 5:
                if set(solved[1]).issubset(set(key)):
                    signal[key] = 3
                    solved[3] = key
                elif set(signal['BD']).issubset(set(key)):
                    signal[key] = 5
                    solved['5'] = key
                else:
                    signal[key] = 2
                    solved[2] = key

            if len(key) == 6:
                if set(solved[4]).issubset(set(key)):
                    signal[key] = 9
                    solved[9] = key
                elif set(solved[1]).issubset(set(key)):
                    signal[key] = 0
                    solved[0] = key
                else:
                    signal[key] = 6
                    solved[6] = key
            

        assert len(solved.keys()) == 10

        display = int(''.join([str(signal[''.join (sorted(o))]) for o in output]))

        total += display

    return total


if __name__ == "__main__":
    from aocd.models import Puzzle

    puzzle = Puzzle(2021, 8)

    test_data = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
    edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
    fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
    fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
    aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
    fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
    dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
    bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
    egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
    gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

    assert solve1(test_data) == 26
    assert solve2(test_data) == 61229

    answer_1 = solve1(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve2(puzzle.input_data)
    print(answer_2)
    puzzle.answer_b = answer_2
