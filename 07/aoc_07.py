import os
import numpy as np

INPUT = os.path.join(os.path.dirname(__file__), "input.txt")

with open(INPUT) as f:
    lines = f.readlines()
crab_coords = np.array([int(x) for x in lines[0].rstrip().split(",")])

# Part 1: Bruteforce
min_sum = np.Infinity
for i in range(np.min(crab_coords), np.max(crab_coords)):
    dist_sum = np.sum(np.abs(crab_coords - i))
    min_sum = min(min_sum, dist_sum)

print(min_sum)

# Part 2: Bruteforce
min_sum = np.Infinity
for i in range(np.min(crab_coords), np.max(crab_coords)):
    dist = np.abs(crab_coords - i)
    dist_sum = np.sum(dist * (dist + 1) / 2.0)
    min_sum = min(min_sum, dist_sum)

print(min_sum)
