import matplotlib.pyplot as plt
import os
import numpy as np


INPUT = os.path.join(os.path.dirname(__file__), "input.txt")

with open(INPUT) as f:
    lines = f.readlines()


coordinates = []
folds = []
divider = False
for line in lines:
    l = line.rstrip()
    if len(l) == 0:
        divider = True
        continue
    if divider:
        axis = l.split("=")[0][-1]
        offset = int(l.split("=")[1])
        folds.append((axis, offset))
        continue
    coordinates.append([int(x) for x in l.split(",")])

coordinates = np.array(coordinates)

paper_dims = (np.max(coordinates[:, 1] + 1),
              np.max(coordinates[:, 0]) + 1)
paper = np.zeros(paper_dims)
print(paper.shape)

paper[coordinates[:, 1], coordinates[:, 0]] = 1
print(paper)
print()


def x_fold(p, offset):
    static_p = p[:, :offset].copy()
    fold_over = p[:, offset+1:].copy()

    for column in range(fold_over.shape[1]):
        static_p[:, - column - 1] += fold_over[:, column]
    return static_p


def y_fold(p, offset):
    static_p = p[:offset, :].copy()
    fold_over = p[offset+1:, :].copy()

    for row in range(fold_over.shape[0]):
        static_p[-row - 1, :] += fold_over[row, :]
    return static_p


for f in folds:
    if f[0] == "x":
        paper = x_fold(paper, f[1])
    else:
        paper = y_fold(paper, f[1])
    print(paper)
print(np.count_nonzero(paper))

paper[paper >= 1] = 1

plt.imshow(paper)
plt.show()
