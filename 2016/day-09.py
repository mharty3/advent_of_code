# --- Day 9: Explosives in Cyberspace ---

def decompress(document):
    decompressed = ''
    i = 0
    while i < len(document):
        if document[i] == '(':
            idx = i + 1
            marker = ''
            while document[idx] != ')':
                marker += document[idx]
                idx += 1
            
            look_ahead, repeat_count = marker.split('x')
            
            sequence = ''
            for j in range(int(look_ahead)):
                j += 1
                sequence += document[idx + j]
            decompressed += sequence * int(repeat_count)
            
            i = idx + int(look_ahead) + 1
  
        else:
            decompressed += document[i]
            i += 1
    
    return decompressed


assert decompress('ADVENT') == 'ADVENT'
assert decompress('A(1x5)BC') == 'ABBBBBC'
assert decompress('(3x3)XYZ') == 'XYZXYZXYZ'
assert decompress('A(2x2)BCD(2x2)EFG') == 'ABCBCDEFEFG'
assert decompress('(6x1)(1x3)A') == '(1x3)A'
assert decompress('X(8x2)(3x3)ABCY') == 'X(3x3)ABC(3x3)ABCY'


def solve1(input_data):
    decompressed = decompress(input_data)
    return len(decompressed)

if __name__ == '__main__':
    from aocd.models import Puzzle
    puzzle = Puzzle(2016, 9)
    answer_1 = solve1(puzzle.input_data)

    print(answer_1)
    puzzle.answer_a = answer_1

    # solve2(puzzle.input_data)
    # # puzzle.answer_b = answer_2

