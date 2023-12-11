import itertools

import geopandas as gpd
import matplotlib.pyplot as plt
import networkx as nx
from shapely import Point, Polygon


connections = {
    '|': [(-1, 0), (1, 0)],
    '-': [(0, -1), (0, 1)],
    'L': [(-1, 0), (0, 1)],
    'J': [(-1, 0), (0, -1)],
    '7': [(0, -1), (1, 0)],
    'F': [(0, 1), (1, 0)],
}


def find_cycle(input_data):
    network = dict() # node: [connected_neighbor_nodes]
    edges = [] # list of all edges [(n0, n1), (n3, n4) ...]

    for r, row in enumerate(input_data.splitlines()):
        for c, val in enumerate(row.strip()):
            
            if val == 'S':
                start = (r, c)
                network[start] = []
            
            elif val != '.':
                offsets = connections[val]
                connected_nodes = [(r+offset[0], c+offset[1]) for offset in offsets] 
                network[(r, c)] = connected_nodes
                
                for node in connected_nodes:
                    edges.append(((r,c), node))

    # find what nodes are connected to S
    for node, neighbors in network.items():
        if start in neighbors:
            network[start].append(node)
            edges.append((start, node))


    G = nx.MultiGraph(edges)
    # filter out "one-way connections"
    two_way_edges = [(n1, n2) for n1, n2, k in G.edges(keys=True) if k == 1]
    G_mutual = nx.MultiGraph(two_way_edges)

    return nx.find_cycle(G_mutual, start)
    

def solve1(input_data):
    return len(find_cycle(input_data)) / 2


def solve2(input_data):

    polygon = Polygon([p[0] for p in find_cycle(input_data)])
    polygon_gdf = gpd.GeoDataFrame({'geometry': [polygon]})

    nrows = len(input_data.splitlines())
    ncols = len(input_data.splitlines()[0])
    pts = itertools.product(range(nrows), range(ncols))
    fp = [Point(p) for p in pts if p not in polygon.exterior.coords]
    
    pts_gdf = (gpd.GeoDataFrame({'geometry':fp})
                 .assign(within_polygon = lambda df: df['geometry'].within(polygon))
              )

    return pts_gdf.within_polygon.sum(), pts_gdf, polygon_gdf


if __name__ == "__main__":
    from aocd.models import Puzzle
    puzzle = Puzzle(2023, 10)

    answer_1 = solve1(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2, pts, poly = solve2(puzzle.input_data)
    print(answer_2)
    puzzle.answer_b = answer_2
