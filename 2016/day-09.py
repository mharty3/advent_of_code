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


# def decompressed_length(document):



assert decompress('ADVENT') == 'ADVENT' # 6
assert decompress('A(1x5)BC') == 'ABBBBBC' # 7  (n_non_markers + look_ahead*repeat) - look_ahead) = 3 + (1*5) - 1 = 7
assert decompress('(3x3)XYZ') == 'XYZXYZXYZ' # 9
assert decompress('A(2x2)BCD(2x2)EFG') == 'ABCBCDEFEFG' # 11
assert decompress('(6x1)(1x3)A') == '(1x3)A' # 6
assert decompress('X(8x2)(3x3)ABCY') == 'X(3x3)ABC(3x3)ABCY' # 18

#


def solve1(input_data):
    decompressed = decompress(input_data)
    return len(decompressed)

def sequence_contains_marker(sequence:str) -> bool:
    return '(' in sequence

def split_marker_sequence(sequence:str) -> Tuple[Tuple[int, int], str]:
    i = 0
    while i < len(sequence):
        idx = i + 1
        marker = ''
        while sequence[idx] != ')':
            marker += sequence[idx]
            idx += 1
        look_ahead, repeat_count = marker.split('x')
        return (int(look_ahead), int(repeat_count)), sequence[idx+1:]

def length(sequence:str) -> int:
    if sequence.startswith('('):
        marker, sequence = split_marker_sequence(sequence)
        if not sequence_contains_marker(sequence):
            return marker[1] * len(sequence)
        else:
            return marker[1] * length(sequence)


print('(20x12)(13x14)(7x10)(1x12)A')
print(length('(20x12)(13x14)(7x10)(1x12)A'))

# passing
assert length('(3x3)XYZ') == 9 # still becomes XYZXYZXYZ, as the decompressed section contains no markers.
assert length('(27x12)(20x12)(13x14)(7x10)(1x12)A') == 241920 # decompresses into a string of A repeated 241920 times.
# failing
assert length('X(8x2)(3x3)ABCY') == 20 # becomes XABCABCABCABCABCABCY, because the decompressed data from the (8x2) marker is then further decompressed, thus triggering the (3x3) marker twice for a total of six ABC sequences.
assert length('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN') == 445 # becomes 445 characters long.

if __name__ == '__main__':
    from aocd.models import Puzzle
    puzzle = Puzzle(2016, 9)
    answer_1 = solve1(puzzle.input_data)

    print(answer_1)
    puzzle.answer_a = answer_1

    # solve2(puzzle.input_data)
    # # puzzle.answer_b = answer_2



# some failed attempts below

# def text_to_tree(text):    
#     t = []
#     i = 0
#     non_compressed_count = 0
#     while i < len(text):
#         if text[i] == '(':
#             idx = i + 1
#             marker = ''
#             while text[idx] != ')':
#                 marker += text[idx]
#                 idx += 1
            
#             look_ahead, repeat_count = marker.split('x')

#             sequence = ''
#             for j in range(int(look_ahead)):
#                 j += 1
#                 sequence += text[idx + j]
#             t.append((int(repeat_count), sequence))
#             i = idx + int(look_ahead) + 1

#         else:
#             non_compressed_count += 1
#             i += 1

#     t.append((non_compressed_count, 1))
#     return t

# t = text_to_tree(document)

# # for i, node in enumerate(t):
# #     if type(node[1]) == str:
# #         t[i] = (node[0], text_to_tree(node[1]))