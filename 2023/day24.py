from aocd.models import Puzzle
puzzle = Puzzle(2023, 24)
input_data = puzzle.input_data

class Point:
    def __init__(self, position, velocity) -> None:
        self.position = position
        self.velocity = velocity

        self.x = position[0]
        self.y = position[1]
        self.z = position[2]

        self.vx = velocity[0]
        self.vy = velocity[1]
        self.vz = velocity[2]

    @staticmethod
    def parse(input_string):
        """ eg" `19, 13, 30 @ -2,  1, -2`  """

        p, v = input_string.split(' @ ')
        p = [int(i) for i in p.split(', ')]
        v = [int(i) for i in v.split(', ')]

        # print(p, v)

        return Point(p, v)

    def __repr__(self) -> str:
        return f'Point({self.position}, {self.velocity})'
    
    def position_at_time(self, t):
        x  = self.x + t * self.vx
        y = self.y + t * self.vy
        z = self.z + t * self.vz
        return (x, y)


    
    def intersect_xy(self, other) -> bool:

        self_x2 = self.x + self.vx
        self_y2 = self.y + self.vy

        other_x2 = other.x + other.vx
        other_y2 = other.y + other.vy

        den = (other_y2 - other.y) * (self_x2 - self.x) - (other_x2 - other.x) * (self_y2 - self.y)

        if den == 0:
            # print('parallel')
            return None

        ua = ((other_x2 - other.x) * (self.y - other.y) - (other_y2 - other.y) * (self.x - other.x)) / den
        ub = ((self_x2 - self.x) * (self.y - other.y) - (self_y2 - self.y) * (self.x - other.x)) / den

        x = self.x + ua * (self_x2 - self.x)
        y = self.y + ua * (self_y2 - self.y)

        if ((x < self.x and self.vx > 0) or 
           (x < other.x and other.vx > 0) or
           (x > self.x and self.vx < 0) or
           (x > other.x and other.vx < 0)):
                # print('intersetion is in past')
                return None

        return (x, y)


def parse(input_data):
    return [Point.parse(line) for line in input_data.splitlines()]        


test_data = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
"""
test_area = (200000000000000, 400000000000000)

# input_data = test_data

points = parse(input_data)

from itertools import combinations

total = 0
for pair in combinations(points, 2):
    # print(pair)
    intersect = pair[0].intersect_xy(pair[1])
    if (intersect and ((test_area[0] <= intersect[0] <= test_area[1] and 
        test_area[0] <= intersect[1] <= test_area[1]))):
        total += 1

    
print(total)
# 11995