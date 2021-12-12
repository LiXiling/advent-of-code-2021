import os
import numpy as np

INPUT = os.path.join(os.path.dirname(__file__), "input.txt")

with open(INPUT) as f:
    lines = f.readlines()
lines = [list(l.rstrip()) for l in lines]

lines_arr = np.array(lines).astype(int)


def within_bounds(x, y, lower, upper):
    full = np.transpose(np.vstack((x, y)))
    r = [np.all(n >= lower) and np.all(n <= upper) for n in full]
    return np.where(np.invert(r))


def flash(octo_field, flash_count=0, flash_field=None):
    if flash_field is None:
        flash_field = np.ones_like(octo_field)

    flashing = np.where(octo_field > 9)
    n_flashing = flashing[0].size
    if n_flashing == 0:
        return flash_count, octopi

    flash_count += n_flashing
    octo_field[flashing] = 0
    flash_field[flashing] = 0

    # Generate all Neighbors
    for x_offset in range(-1, 2):
        for y_offset in range(-1, 2):
            x, y = flashing[0] + x_offset, flashing[1] + y_offset

            # Remove Indices Out of Bounds - Literal Edge cases
            illegal_indices = within_bounds(x, y, 0, 9)
            x = np.delete(x, illegal_indices)
            y = np.delete(y, illegal_indices)
            octo_field[x, y] += 1

    # Already flashed octopi stay 0
    octo_field *= flash_field
    return flash(octo_field, flash_count, flash_field)


# Part 1
octopi = lines_arr.copy()
sum = 0
for t in range(100):
    octopi += 1
    flash_count, octopi = flash(octopi)
    sum += flash_count
print(sum)


# Part 2
octopi = lines_arr.copy()
step = 0
while True:
    octopi += 1
    step += 1
    flash_count, octopi = flash(octopi)
    if flash_count == 100:
        break
print(step)
