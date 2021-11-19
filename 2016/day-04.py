# --- Day 4: Security Through Obscurity ---

from typing import NamedTuple
from collections import Counter
import string

class Room(NamedTuple):
    name: str
    sector_id: int
    checksum: str

    @staticmethod
    def from_line(line):
        line = line.replace(']', '')
        split1 = line.strip().split('[')
        split2 = split1[0].split('-')
        name = '-'.join(split2[:-1])
        sector_id = int(split2[-1])
        checksum = split1[-1]

        return Room(name, sector_id, checksum)

    def is_real(self) -> bool:
        c = Counter(sorted(self.name.replace('-', '')))
        common_letters_and_counts = c.most_common(5)
        common_letters = [letter for letter, count in common_letters_and_counts]
        return ''.join(common_letters) == self.checksum
    
    def shift_cypher(self, letter, shift):
        idx = string.ascii_lowercase.index(letter)
        new_idx = (idx + shift) % 26 
        return string.ascii_lowercase[new_idx]

    def decode(self):
        s = []
        for l in self.name:
            if l == '-':
                new_l = ' '
            else:
                new_l = self.shift_cypher(l, self.sector_id)
            s.append(new_l)
        return ''.join(s) 
        

def solve1(input_data):
    lines = input_data.split('\n')
    rooms = [Room.from_line(line) for line in lines]
    valid_sector_ids = [r.sector_id for r in rooms if r.is_real()]
    return sum(valid_sector_ids)

def solve2(input_data):
    lines = input_data.split('\n')
    rooms = [Room.from_line(line) for line in lines]
    room_names = [(r.decode(), r.sector_id) for r in rooms if r.is_real()]
    for rn in room_names:
        print(rn)

test_data = """aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]"""

assert solve1(test_data) == 1514
solve2(test_data)

if __name__ == '__main__':
    from aocd.models import Puzzle
    puzzle = Puzzle(2016, 4)
    answer_1 = solve1(puzzle.input_data)

    print(answer_1)
    puzzle.answer_a = answer_1

    solve2(puzzle.input_data)
    # puzzle.answer_b = answer_2
