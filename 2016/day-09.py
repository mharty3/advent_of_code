# --- Day 9: Explosives in Cyberspace ---

from typing import Tuple

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


assert decompress('ADVENT') == 'ADVENT' # 6
assert decompress('A(1x5)BC') == 'ABBBBBC' # 7  (n_non_markers + look_ahead*repeat) - look_ahead) = 3 + (1*5) - 1 = 7
assert decompress('(3x3)XYZ') == 'XYZXYZXYZ' # 9
assert decompress('A(2x2)BCD(2x2)EFG') == 'ABCBCDEFEFG' # 11
assert decompress('(6x1)(1x3)A') == '(1x3)A' # 6
assert decompress('X(8x2)(3x3)ABCY') == 'X(3x3)ABC(3x3)ABCY' # 18


def solve1(input_data):
    decompressed = decompress(input_data)
    return len(decompressed)

def sequence_contains_marker(sequence:str) -> bool:
    return '(' in sequence

def split_marker_sequence(sequence:str) -> Tuple[Tuple[int, int], str, int]:
    """Returns tuple of 4 values:
        - first value of marker (look_ahead)
        - second value of marker (repeat count)
        - number of characters in the marker for advancing string index
    """
    i = 0
    while i < len(sequence):
        idx = i + 1
        marker = ''
        while sequence[idx] != ')':
            marker += sequence[idx]
            idx += 1
        look_ahead, repeat_count = marker.split('x')
        return (int(look_ahead), int(repeat_count)), sequence[idx+1:idx+1+int(look_ahead)], len(marker)+2


def length(sequence:str) -> int:
    i = 0
    out_of_marker = 0
    total = 0
    
    while i < len(sequence): # iterate along document
        if not sequence[i] == '(': # account for chars that don't need to be expanded
            out_of_marker += 1
            i += 1
        else: 
            marker, sub_sequence, len_marker = split_marker_sequence(sequence[i:])
            if not sequence_contains_marker(sub_sequence): # self contained marker sequence
                i += marker[0] + len_marker
                total +=  marker[1] * len(sub_sequence)
            else: # go deeper
                i += marker[0] + len_marker
                total += marker[1] * length(sub_sequence)
    
    return total + out_of_marker


# passing
assert length('(3x3)XYZ') == 9 # still becomes XYZXYZXYZ, as the decompressed section contains no markers.
assert length('(27x12)(20x12)(13x14)(7x10)(1x12)A') == 241920 # decompresses into a string of A repeated 241920 times.
assert length('X(8x2)(3x3)ABCY') == 20 # becomes XABCABCABCABCABCABCY, because the decompressed data from the (8x2) marker is then further decompressed, thus triggering the (3x3) marker twice for a total of six ABC sequences.
assert length('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN') == 445 # becomes 445 characters long.

if __name__ == '__main__':
    from aocd.models import Puzzle
    puzzle = Puzzle(2016, 9)
    answer_1 = solve1(puzzle.input_data)

    print(answer_1)
    puzzle.answer_a = answer_1

    puzzle.answer_b = length(puzzle.input_data)

