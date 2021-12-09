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

# Part 2:
lookup_table = {
    "abcefg": "0",  # 6
    "cf": "1",  # 2
    "acdeg": "2",  # 5
    "acdfg": "3",  # 5
    "bcdf": "4",  # 4
    "abdfg": "5",  # 5
    "abdefg": "6",  # 6
    "acf": "7",  # 3
    "abcdefg": "8",  # 7
    "abcdfg": "9"  # 6
}

displays = lines_arr[:, 0]
displays = np.array([x.split(" ") for x in displays])
display_lengths = my_len(displays)


def translate(disp, trans_dict):
    trans_string = "".join(sorted([trans_dict[c] for c in disp]))
    translation = lookup_table[trans_string]
    return translation


sum = 0
for i in range(displays.shape[0]):
    cross_dict = {}

    display = displays[i]
    display_l = display_lengths[i]
    single_output = output[i]

    one_set = set(display[display_l == 2][0])
    seven_set = set(display[display_l == 3][0])
    four_set = set(display[display_l == 4][0])

    # Top Bar - Difference 7 and 1
    a = list(seven_set.difference(one_set))[0]
    cross_dict[a] = "a"

    # Bottom Bar
    ext_four = four_set.copy()
    ext_four.add(a)
    zero_six_nine = [set(x) for x in display[display_l == 6]]
    diffs = sorted([s.difference(ext_four) for s in zero_six_nine])
    g = diffs[0].pop()
    cross_dict[g] = "g"

    # Bottom Left
    e_set = diffs[1]
    e_set.remove(g)
    e = e_set.pop()
    cross_dict[e] = "e"

    # Top Right
    diffs = sorted([one_set.difference(s) for s in zero_six_nine])
    c = diffs[-1].pop()
    cross_dict[c] = "c"

    # Bottom Right
    f = one_set.difference(c).pop()
    cross_dict[f] = "f"

    # Top Left
    two_three_five = [set(x) for x in display[display_l == 5]]
    diffs = sorted([s.difference([a, c, e, f, g]) for s in zero_six_nine])
    b = diffs[0].pop()
    cross_dict[b] = "b"

    # Top Middle
    d_set = diffs[-1]
    d_set.remove(b)
    d = d_set.pop()
    cross_dict[d] = "d"

    t_func = np.vectorize(lambda x: translate(x, cross_dict))
    trans = int("".join(t_func(single_output)))
    sum += trans
print(sum)
