import numpy as np
from aocd.models import Puzzle
puzzle = Puzzle(2023, 22)
input_data = puzzle.input_data

class Brick:
    def __init__(self, description_string):
        self.x1, self.y1, self.z1, self.x2, self.y2, self.z2 = [int(i) for i in description_string.replace('~', ',').split(',')]


        self.xmin, self.xmax = sorted([self.x1, self.x2])
        self.ymin, self.ymax = sorted([self.y1, self.y2])
        self.zmin, self.zmax = sorted([self.z1, self.z2])

        self.height = self.zmax - self.zmin + 1
    
    def __repr__(self):
        return f'Brick( xmin: {self.xmin}, xmax: {self.xmax}, ymin: {self.ymin}, ymax: {self.ymax}, zmin: {self.zmin}, zmax: {self.zmax})'

# dict with id: Brick object
bricks = dict()
for i, desc in enumerate(input_data.splitlines()):
    bricks[i] = Brick(desc)

# generate two "map" arrays
# one is for the elevation of a brick for a xy coordinate
# the other is for the id of the top brick for a xy coordinate
max_x = max([b.x2 for b in bricks.values()])
max_y = max(b.y2 for b in bricks.values())

elevations = np.zeros((max_y+1, max_x+1))
top_brick = np.zeros_like(elevations)
top_brick[:,:] = -1

# sort bricks by zmin
bricks = {k: v for k, v in sorted(bricks.items(), key=lambda x: x[1].zmin)}

supports = dict() # brick: bricks supporting it
for i, brick in bricks.items():
    # index into the map arrays for the values that are directly under the current brick
    elevation_footprint = elevations[brick.ymin:brick.ymax+1, brick.x1:brick.x2+1]
    top_brick_footprint = top_brick[brick.ymin:brick.ymax+1, brick.x1:brick.x2+1]

    base = elevation_footprint.max() # z value that the brick will sit on
    supporting_bricks = set(top_brick_footprint[elevation_footprint == base]) # bricks that will support the current brick

    # update the map arrays with the values that result from dropping the current brick
    elevations[brick.ymin:brick.ymax+1, brick.x1:brick.x2+1] = base + brick.height
    top_brick[brick.ymin:brick.ymax+1, brick.x1:brick.x2+1] = i

    # update supports dict to indicate the bricks that brick i is supported by
    supports[i] = supporting_bricks


# set of bricks that are supporting other bricks 
all_supporting_bricks = set.union(*supports.values())

removable_bricks = set()
critical_bricks = set()
for k, v in supports.items():
    if k not in all_supporting_bricks: # if brick k is not supporting any other bricks it can be removed
        removable_bricks.add(k)
    if len(v) > 1: # if brick k is supporting more than one brick, the supporting bricks can be removed
        for brick in v:
            removable_bricks.add(brick)
    if len(v) == 1: # if brick k is supported by exactly one brick, that brick can never be removed
        critical_bricks.add(list(v)[0])


# final answer are the candidates for removal minus the critical bricks
removable_bricks = removable_bricks.difference(critical_bricks)
answer_a = len(removable_bricks)



# lots of unsuccessful attempts to solve part 2 below
import networkx as nx
import matplotlib.pyplot as plt
G = nx.DiGraph(supports)
# nx.draw(G, with_labels=True)
# plt.show()
# 487 too high
# 33 not right
# 410 too high



# nx.set_node_attributes(G, 0, 'n_of_bricks_that_will_fall_if_removed')
# for layer in reversed(list(nx.bfs_layers(nx.reverse_view(G), -1))):
#     for n in layer:
#         predecessors = list(G.predecessors(n))
#         print(f'{n} has predecessors {predecessors}')
#         if len(predecessors) == 0:
#             print(f'{n} is on top')
#             nx.set_node_attributes(G, {n: 1}, 'n_of_bricks_that_will_fall_if_removed')
#         for predecessor in predecessors:
#             supporters = list(G.neighbors(predecessor))
#             # if len(supporters) == 1:
#                 # print(f'if {n} is removed, {predecessors} will fall')
#             nx.set_node_attributes(G, {n: G.nodes[predecessor]['n_of_bricks_that_will_fall_if_removed'] + 1}, 'n_of_bricks_that_will_fall_if_removed')

# for n in removable_bricks:
#     nx.set_node_attributes(G, {n: 0}, 'n_of_bricks_that_will_fall_if_removed')



# answer = sum(G.nodes[n]['n_of_bricks_that_will_fall_if_removed'] for n in G.nodes) - G.nodes[-1]['n_of_bricks_that_will_fall_if_removed']




# nx.set_node_attributes(G, set(), 'all_predecessors')
bricks = {k: v for k, v in sorted(bricks.items(), key=lambda x: -1 * x[1].zmax)}
for n in bricks:
    print(n)
    predecessors = list(G.predecessors(n))
    print(predecessors)
    if len(predecessors) == 0:
        nx.set_node_attributes(G, set([n]), 'all_predecessors')
    else:
        for predecessor in predecessors:
            G.nodes[n]['all_predecessors'] = G.nodes[n].get('all_predecessors', set()).union(G.nodes[predecessor]['all_predecessors']).union(set([predecessor]))


for n in removable_bricks:
    nx.set_node_attributes(G, {n: set()}, 'all_predecessors')


# for n in G.nodes:
#     print(n, G.nodes[n]['all_predecessors'])

total = 0
for n in bricks:
    if n not in removable_bricks:
        total += len(nx.ancestors(G, n))

print(total)














# 3731 too low
# 82167 wrong