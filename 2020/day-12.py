class Ferry:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.bearing = 90  # ship is facing east
        self.cardinal_bearing = "E"
        self.CARDINAL_DIRECTIONS = {0: "N", 90: "E", 180: "S", 270: "W"}

    def rotate(self, direction, angle):
        if direction == "L":
            self.bearing -= angle
        elif direction == "R":
            self.bearing += angle
        self.bearing = self.bearing % 360
        self.cardinal_bearing = self.CARDINAL_DIRECTIONS[self.bearing]

    def move(self, direction, distance):
        directions = {"N": ("y", 1), "S": ("y", -1), "E": ("x", 1), "W": ("x", -1)}
        coord, factor = directions[direction]
        if coord == "y":
            self.y += factor * distance
        elif coord == "x":
            self.x += factor * distance

    def execute_instruction(self, instruction):
        action, value = instruction[0], int(instruction[1:])
        if action in "LR":
            self.rotate(action, value)
        elif action == "F":
            self.move(self.cardinal_bearing, value)
        elif action in "NSEW":
            self.move(action, value)


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
