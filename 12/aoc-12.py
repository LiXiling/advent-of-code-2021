from copy import deepcopy
import os
import numpy as np

from collections import defaultdict

INPUT = os.path.join(os.path.dirname(__file__), "input.txt")

with open(INPUT) as f:
    lines = f.readlines()
lines = [l.rstrip().split("-") for l in lines]

cave_map = defaultdict(list)
for l in lines:
    cave_map[l[0]].append(l[1])
    cave_map[l[1]].append(l[0])


# Part 1
def explore(current_cave: str, visited_caves: list):
    if current_cave in visited_caves:
        return 0
    if current_cave == "end":
        return 1

    if current_cave.lower() == current_cave:
        visited_caves.append(current_cave)
    return sum(map(lambda x: explore(x, visited_caves.copy()), cave_map[current_cave]))


print(explore("start", []))

# Part 2


def explore_twice(current_cave: str, visited_counter: dict):
    if visited_counter[current_cave] >= 1 and 2 in visited_counter.values():
        return 0
    if current_cave == "end":
        return 1
    if current_cave == "start" and visited_counter[current_cave] > 0:
        return 0

    if current_cave.lower() == current_cave:
        visited_counter[current_cave] += 1
    return sum(map(lambda x: explore_twice(x, deepcopy(visited_counter)), cave_map[current_cave]))


print(explore_twice("start", defaultdict(int)))
