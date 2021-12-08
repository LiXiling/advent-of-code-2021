import os
import numpy as np

INPUT = os.path.join(os.path.dirname(__file__), "input.txt")

with open(INPUT) as f:
    lines = f.readlines()
lines = [l.rstrip().split(" | ") for l in lines]
lines_arr = np.array(lines)

# Part 1:
output = lines_arr[:, 1]
output = np.array([x.split(" ") for x in output])
my_len = np.vectorize(len)
output_lengths = my_len(output)
n_segments, counts = np.unique(output_lengths, return_counts=True)
n_unique = np.sum(counts[np.where(np.isin(n_segments, [2, 3, 4, 7]))])
print(n_unique)
