from math import sin, cos, radians
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches

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


class Waypoint_Ferry():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.waypoint_x = 10
        self.waypoint_y = 1
        self.CARDINAL_DIRECTIONS = {"N": 90, "E": 0, "S": 180, "W": 270}

    def rotate(self, direction, angle):
        if direction == "R":
            angle *= -1
        x, y = self.waypoint_x, self.waypoint_y
        self.waypoint_x = x * round(cos(radians(angle))) - y * round(sin(radians(angle)))
        
        self.waypoint_y = x * round(sin(radians(angle))) + y * round(cos(radians(angle)))
        

    def move_waypoint(self, bearing, distance):
        self.waypoint_x += round(cos(radians(bearing))) * distance
        self.waypoint_y += round(sin(radians(bearing))) * distance

    def move_ferry(self, value):
        self.x += self.waypoint_x * value
        self.y += self.waypoint_y * value

    def execute_instruction(self, instruction):
        action, value = instruction[0], int(instruction[1:])
        if action in "LR":
            self.rotate(action, value)
        elif action == "F":
            self.move_ferry(value)
        elif action in "NSEW":
            bearing = self.CARDINAL_DIRECTIONS[action]
            self.move_waypoint(bearing, value)


    def plot(self, title):
        fig, ax = plt.subplots()
        arrow = mpatches.Arrow(self.x, self.y, self.waypoint_x, self.waypoint_y, width=5)
        ax.add_patch(arrow)
        ax.set_xlim(-50, 50)
        ax.set_ylim(-50, 50)
        ax.grid()
        ax.set_title(title)
        plt.show()




def solve1(input_data):
    f = Ferry()
    for inst in input_data.split("\n"):
        f.execute_instruction(inst.strip())
    return abs(f.x) + abs(f.y)


def solve2(input_data):
    f = Waypoint_Ferry()
    for inst in input_data.split("\n"):
        f.execute_instruction(inst.strip())
        f.plot(inst)

    return abs(f.x) + abs(f.y)


if __name__ == "__main__":
    from aocd.models import Puzzle

    test_data = """F10
                   N3
                   F7
                   R90
                   F11"""

    tonys_test_data = """F1
                        N1
                        E1
                        S1
                        W1
                        R90
                        F1
                        R180
                        F1
                        R270
                        F1
                        L90
                        F1
                        L180
                        F2
                        L270
                        F3"""

    assert solve1(test_data) == 25
    assert solve2(test_data) == 286
    assert solve2(tonys_test_data) == 42

    puz12 = Puzzle(2020, 12)
    data = puz12.input_data
    puz12.answer_a = solve1(data)
    # puz12.answer_b = solve2(data)
