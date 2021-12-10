import os
import numpy as np

INPUT = os.path.join(os.path.dirname(__file__), "input.txt")

with open(INPUT) as f:
    lines = f.readlines()
lines = [l.rstrip() for l in lines]


close_mapping = {
    ")": ("(", 3),
    "]": ("[", 57),
    "}": ("{", 1197),
    ">": ("<", 25137),
}

# Part 1
illegal_chars = []
missing_chars = []
for l in lines:
    corrupt = False
    stack = []
    for symbol in l:
        if symbol in [x[0] for x in close_mapping.values()]:
            stack.append(symbol)
            continue
        if len(stack) == 0:
            illegal_chars.append(symbol)
            corrupt = True
            break
        to_close = stack.pop()
        if close_mapping[symbol][0] != to_close:
            illegal_chars.append(symbol)
            corrupt = True
            break
    if corrupt:
        continue
    missing_chars.append(stack)

print(sum([close_mapping[c][1] for c in illegal_chars]))

# Part 2:
missing_scores = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}
scores = []
for incomplete_line in missing_chars:
    rev = reversed(incomplete_line)
    score = 0
    for c in rev:
        score = score * 5 + missing_scores[c]
    scores.append(score)

# Use Numpy because why not
print(np.median(scores))
