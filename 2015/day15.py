test_data = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"""

import re
import numpy as np

properties = []

data = test_data
for ingredient in data.splitlines():
   pattern = '-*\d+'
   m = re.findall(pattern, ingredient)
   properties.append([int(p) for p in m])


def score(x, y):
    property_matrix = np.array(properties)
    amount_matrix = np.array([x, y])
    prod = amount_matrix @ property_matrix
    return -np.prod(prod[:-1])

