import numpy as np
import os

INPUT = os.path.join(os.path.dirname(__file__), "input.txt")

with open(INPUT) as f:
    lines = f.readlines()
lines = [l.rstrip().split(" ") for l in lines]
lines_str_arr = np.array(lines)

# Remove arrow sign
lines_str_arr = np.delete(lines_str_arr, 1, axis=1)

# Cast to Int
lines_str_arr = np.expand_dims(lines_str_arr, axis=-1)
lines_coords = np.apply_along_axis(
    lambda x: [int(y) for y in x[0].split(',')], -1, lines_str_arr)

print(lines_coords.shape)

# Part 1
# Filter for Horizontal Lines
vert = lines_coords[lines_coords[:, 0, 0] == lines_coords[:, 1, 0]]
horz = lines_coords[lines_coords[:, 0, 1] == lines_coords[:, 1, 1]]

# valid lines probably unnecessary
valid_lines = np.vstack((horz, vert))
print(horz.shape, vert.shape, valid_lines.shape)

# create field map
max_x = np.max(valid_lines[:, :, 0]) + 1
max_y = np.max(valid_lines[:, :, 1]) + 1
field = np.zeros((max_x, max_y))
print(field.shape)

# iterate through horizontal and vertical lines. can probably be merged somehow
for line in horz:
    sort_idx = sorted([line[0, 0], line[1, 0]])
    for p in np.arange(sort_idx[0], sort_idx[1] + 1):
        field[line[0, 1], p] += 1

for line in vert:
    sort_idx = sorted([line[0, 1], line[1, 1]])
    for p in np.arange(sort_idx[0], sort_idx[1] + 1):
        field[p, line[0, 0]] += 1

print(field[field >= 2].size)

# Part 2
# get diagonal lines - orthogonal lines are still known
diag = lines_coords[lines_coords[:, 0, 0] != lines_coords[:, 1, 0]]
diag = diag[diag[:, 0, 1] != diag[:, 1, 1]]

for line in diag:
    x_idx = [line[0, 0], line[1, 0]]
    y_idx = [line[0, 1], line[1, 1]]

    # Handle lines in "reverse" order
    x_coords = np.arange(x_idx[0], x_idx[1] + 1)
    if np.diff(x_idx) < 0:
        x_coords  = np.flip(np.arange(x_idx[1], x_idx[0] + 1))

    y_coords = np.arange(y_idx[0], y_idx[1] + 1)
    if np.diff(y_idx) < 0:
        y_coords = np.flip(np.arange(y_idx[1], y_idx[0] + 1))

    for x, y in zip(x_coords, y_coords):
        field[y, x] += 1
print(field[field >= 2].size)