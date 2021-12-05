import numpy as np
import os

INPUT = os.path.join(os.path.dirname(__file__), "input.txt")

with open(INPUT) as f:
    lines = f.readlines()

# Remove trailing Whitespace and split into chars
lines = [list(line.rstrip()) for line in lines]

lines_arr = np.array(lines)
lines_arr = lines_arr.astype(int)

num_entries = lines_arr.shape[0]
bit_counter = np.sum(lines_arr, axis=0)
print(num_entries)
print(bit_counter)


# Part 1
gamma = np.zeros_like(bit_counter)
gamma[np.where(bit_counter > num_entries / 2.0)] = 1

# "Bitflip" with integers
epsilon = np.abs(gamma - 1)
print(gamma)
print(epsilon)


def binary_2_decim(arr):
    arr_rev = np.flip(arr)
    exponents = np.nonzero(arr_rev)
    return np.sum(np.power(2, exponents))


gamma_decim = binary_2_decim(gamma)
epsilon_decim = binary_2_decim(epsilon)
print(gamma_decim, epsilon_decim)
print(gamma_decim * epsilon_decim)

# Part 2


def recursive_oxy_filter(arr, idx, co2=False):
    oxy_candidates = np.copy(arr)
    num_candidates = oxy_candidates.shape[0]
    oxy_bit_counter = np.sum(oxy_candidates, axis=0)

    oxy_mask = np.zeros_like(oxy_bit_counter)
    oxy_mask[np.where(oxy_bit_counter >= num_candidates / 2.0)] = 1

    if co2:
        # "Bitflip" with integers
        oxy_mask = np.abs(oxy_mask - 1)

    oxy_candidates = oxy_candidates[oxy_candidates[:, idx] == oxy_mask[idx]]
    if oxy_candidates.shape[0] > 1:
        return recursive_oxy_filter(oxy_candidates, idx=idx+1, co2=co2)
    return oxy_candidates


oxy = binary_2_decim(recursive_oxy_filter(lines_arr, 0)[0])
co2 = binary_2_decim(recursive_oxy_filter(lines_arr, 0, co2=True)[0])
print(oxy, co2, oxy*co2)
