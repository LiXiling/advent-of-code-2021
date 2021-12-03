import numpy as np
import os

INPUT = os.path.join(os.path.dirname(__file__), "input.txt")

with open(INPUT) as f:
    lines = f.readlines()

# Remove trailing Whitespace seperate submarine command from value
lines = [line.rstrip().split(" ") for line in lines]

# Part 1
hoz_pos = 0
depth = 0

for cmd, v in lines:
    v = int(v)

    if cmd[0] == "f":
        hoz_pos += v
    elif cmd[0] == "d":
        depth += v
    elif cmd[0] == "u":
        depth -= v

print(hoz_pos, depth, hoz_pos* depth)

# Part 2
# Code Duplication because I am lazy and it's a Hackathon

hoz_pos = 0
aim = 0
depth = 0

for cmd, v in lines:
    v = int(v)

    if cmd[0] == "f":
        hoz_pos += v
        depth += aim * v
    elif cmd[0] == "d":
        aim += v
    elif cmd[0] == "u":
        aim -= v

print(hoz_pos, aim, depth, hoz_pos* depth)