from collections import defaultdict
import os
import numpy as np


INPUT = os.path.join(os.path.dirname(__file__), "input.txt")

with open(INPUT) as f:
    lines = f.readlines()

polymer = lines[0].rstrip()
insertion_rules = {}

for l in lines[2:]:
    k, v = l.rstrip().split(" -> ")
    insertion_rules[k] = v


# Part 1:
def grow_polymer(p):
    new_p = ""
    for i in range(len(p)-1):
        pair = p[i:i+2]
        if pair in insertion_rules:
            new_p += pair[0] + insertion_rules[pair]
        else:
            new_p += pair[0]
    new_p += p[-1]
    return new_p


for i in range(10):
    polymer = grow_polymer(polymer)

polymer_arr = np.array(list(polymer))
symbols, counts = np.unique(polymer_arr, return_counts=True)
print(np.max(counts) - np.min(counts))


# Part 2 - gotta go big
polymer = lines[0].rstrip()
pair_counter = defaultdict(int)
for pair in zip(polymer, polymer[1:]):
    pair_counter["".join(pair)] += 1


def grow_polymer_dict(pair_c):
    new_pair_c = defaultdict(int)
    for pair, count in pair_c.items():
        if pair in insertion_rules:
            insert = insertion_rules[pair]
            new_pair_c[pair[0]+insert] += count
            new_pair_c[insert+pair[1]] += count
        else:
            new_pair_c[pair] += count
    return new_pair_c


def count_chars(pair_c):
    char_dict = defaultdict(int)
    for pair, count in pair_c.items():
        char_dict[pair[0]] += count
        char_dict[pair[1]] += count

    for char, count in char_dict.items():
        char_dict[char] = np.ceil(count / 2)
    return char_dict


for i in range(40):
    pair_counter = grow_polymer_dict(pair_counter)

char_counts = list(count_chars(pair_counter).values())

print(np.max(char_counts) - np.min(char_counts))
