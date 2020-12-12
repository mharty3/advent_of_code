from math import sin, cos, radians


class Ferry:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.bearing = 0  # ship is facing east
        self.CARDINAL_DIRECTIONS = {"N": 90, "E": 0, "S": 180, "W": 270}

    def rotate(self, direction, angle):
        # ccw is positive
        if direction == "L":
            self.bearing += angle
        elif direction == "R":
            self.bearing -= angle
        self.bearing = self.bearing % 360

    def move(self, bearing, distance):
        self.x += round(cos(radians(bearing))) * distance
        self.y += round(sin(radians(bearing))) * distance

    def execute_instruction(self, instruction):
        action, value = instruction[0], int(instruction[1:])
        if action in "LR":
            self.rotate(action, value)
        elif action == "F":
            self.move(self.bearing, value)
        elif action in "NSEW":
            bearing = self.CARDINAL_DIRECTIONS[action]
            self.move(bearing, value)


def solve1(input_data):
    f = Ferry()
    for inst in input_data.split("\n"):
        f.execute_instruction(inst.strip())
    return abs(f.x) + abs(f.y)


if __name__ == "__main__":
    from aocd.models import Puzzle

    test_data = """F10
                   N3
                   F7
                   R90
                   F11"""

    assert solve1(test_data) == 25

    puz12 = Puzzle(2020, 12)
    data = puz12.input_data
    puz12.answer_a = solve1(data)
    # puz12.answer_b = solve2(data)
