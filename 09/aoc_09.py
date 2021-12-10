import numpy as np
import os

from numpy.lib.arraypad import pad

INPUT = os.path.join(os.path.dirname(__file__), "input.txt")

with open(INPUT) as f:
    lines = f.readlines()

lines = [list(map(lambda x: int(x), line.rstrip())) for line in lines]
heightmap = np.array(lines)


# Part 1
window = np.array(
    [
        [10, 1, 10],
        [1, 1, 1],
        [10, 1, 10]
    ]
)

padded_heightmap = np.pad(
    heightmap, (1, 1), "constant", constant_values=(9, 9))

risk_sum = 0

basin_coordinates = []
debug_field = np.zeros_like(padded_heightmap)
for i in range(1, padded_heightmap.shape[0] - 1):
    for j in range(1, padded_heightmap.shape[1] - 1):
        sub_map = padded_heightmap[i-1:i+2, j-1:j+2]

        if np.argmin(np.multiply(sub_map, window)) == 4:
            risk_sum += padded_heightmap[i, j] + 1
            basin_coordinates.append([i, j])

print(risk_sum)


# Part 2:
def explore_basin(coords, explored):
    i, j = coords
    x = padded_heightmap[i, j]
    if x >= 9 or coords in explored:
        return 0
    explored.append(coords)
    return 1 + explore_basin([i-1, j], explored) + explore_basin([i+1, j], explored) + explore_basin([i, j-1], explored) + explore_basin([i, j+1], explored)


basin_sizes = list(map(lambda x: explore_basin(x, []), basin_coordinates))
basin_sizes = sorted(basin_sizes, reverse=True)
print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])
