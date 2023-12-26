import numpy as np
import matplotlib.pyplot as plt
from itertools import pairwise

test_input = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

from aocd.models import Puzzle

puzzle = Puzzle(2022, 14)
# input_data = puzzle.input_data

input_data = test_input
lines = []
xs = []
ys = []
for line in input_data.splitlines():
    coords = []
    for coord in line.split(' -> '):
        x, y = coord.split(',')
        coords.append((int(x), int(y)))
        xs.append(int(x))
        ys.append(int(y))
    lines.append(coords)

scan = np.empty((max(ys)+3, max(xs)+3))
scan.fill(0)
scans = np.empty((1000, scan.shape[0], scan.shape[1]))

for line in lines:
    for (x1, y1), (x2, y2) in pairwise(line):
        if x1 == x2: # vertical
            top = min(y1, y2)
            bottom = min(y1, y2) + 1
            scan[y1:y2, x1] = -1
        elif y1 == y2: # horizontal
            left = min(x1, x2)
            right = max(x1, x2) + 1
            scan[y1, left:right] = -1

i = 0
while True:
    try:
        grain_rc = (0,500)
        while (   scan[grain_rc[0]+1, grain_rc[1]] == 0 
            or scan[grain_rc[0]+1, grain_rc[1]-1] == 0 
            or scan[grain_rc[0]+1, grain_rc[1]+1] == 0):
            if scan[grain_rc[0]+1, grain_rc[1]] == 0:
                grain_rc = (grain_rc[0]+1, grain_rc[1])
            elif scan[grain_rc[0]+1, grain_rc[1]-1] == 0:
                grain_rc = (grain_rc[0]+1, grain_rc[1]-1)
            elif scan[grain_rc[0]+1, grain_rc[1]+1] == 0:
                grain_rc = (grain_rc[0]+1, grain_rc[1]+1) 
        scan[grain_rc] = 1
        scans[i] = scan
        i += 1
    except IndexError:
        print(i)
        break

plt.imshow(scan)
plt.show()
plt.imshow(scans[i-1, :, :])
plt.show()

    # answer_1 = solve1(puzzle.input_data)
    # print(answer_1)
    # puzzle.answer_a = answer_1

    # answer_2 = solve2(input_data)
    # print(answer_2)
    # puzzle.answer_b = answer_2 

# 916 too high
# 915 too 

# print(scan)


import numpy as np
import matplotlib.pyplot as plt


class IndexTracker(object):
    def __init__(self, ax, X):
        self.ax = ax
        ax.set_title('use scroll wheel to navigate images')

        self.X = X
        self.slices, rows, cols = X.shape
        self.ind = self.slices//2

        self.im = ax.imshow(self.X[self.ind, :, :])
        self.update()

    def onscroll(self, event):
        print("%s %s" % (event.button, event.step))
        if event.button == 'up':
            self.ind = (self.ind + 1) % self.slices
        else:
            self.ind = (self.ind - 1) % self.slices
        self.update()

    def update(self):
        self.im.set_data(self.X[self.ind, :, :])
        self.ax.set_ylabel('slice %s' % self.ind)
        self.im.axes.figure.canvas.draw()


fig, ax = plt.subplots(1, 1)

X = scans[:, :, min(xs)-1:]

tracker = IndexTracker(ax, X)


fig.canvas.mpl_connect('scroll_event', tracker.onscroll)
plt.show()