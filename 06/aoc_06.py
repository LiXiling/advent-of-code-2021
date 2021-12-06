import os
import numpy as np

INPUT = os.path.join(os.path.dirname(__file__), "input.txt")

with open(INPUT) as f:
    lines = f.readlines()
lines = [l.rstrip().split(",") for l in lines]
lines_arr = np.array(lines)

lines_arr = np.squeeze(lines_arr)

# Part 1 Naive Numpy Bruteforce
lanternfish = np.copy(lines_arr).astype(int)
for day in range(80):
    lanternfish -= 1
    n_newborns = lanternfish[lanternfish < 0].size
    lanternfish[lanternfish < 0] = 6
    lanternfish = np.append(lanternfish, np.ones(n_newborns) * 8)
print(lanternfish.size)

# Part 2
fast_fish, bins = np.histogram(lines_arr, bins=np.arange(0, 10))
for i in range(256):
    n_newborns = fast_fish[0]
    fast_fish = np.append(fast_fish[1:], n_newborns)
    fast_fish[6] += n_newborns

print(np.sum(fast_fish))
