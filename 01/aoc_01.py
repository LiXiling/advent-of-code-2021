import numpy as np
import os

INPUT = os.path.join(os.path.dirname(__file__), "input.txt")

with open(INPUT) as f:
    lines = f.readlines()

# Remove trailing Whitespace and cast to int
lines = [int(line.rstrip()) for line in lines]

# Part 1 
# Take Difference between two successive elements. Count elements where difference > 0
lines_arr = np.array(lines)
diff = np.diff(lines_arr) 
print(diff[diff>0].shape)


# Part 2
# Same as Part 1 but with moving window sum
lines_arr = np.array(lines)
moving_window = np.ones((3,))

window_sum = np.convolve(lines_arr, moving_window, mode="valid")
diff = np.diff(window_sum) 
print(diff[diff>0].shape)
