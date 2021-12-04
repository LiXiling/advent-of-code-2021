import numpy as np
import os

INPUT = os.path.join(os.path.dirname(__file__), "input.txt")

with open(INPUT) as f:
    lines = f.readlines()
lines = [l.rstrip() for l in lines]

# Parse Bingo Structure
sequence = [int(v) for v in lines[0].split(",")]
# second line is empty, boards begin in line 3
board_lines = lines[2:]

all_boards = []
single_board = []
for l in board_lines:
    # Check for emtpy divider line
    if not l:
        all_boards.append(single_board)
        single_board = []
        continue
    # normalize double space for single digit nums
    l= " ".join(l.split())
    single_board.append([int(v) for v in l.rstrip().split(" ")])

boards_arr = np.array(all_boards)
print(boards_arr.shape)

# Part 1
def check_winner(arr):
    # Find full row
    tmp_arr = np.copy(arr)
    row_check = np.sum(tmp_arr, axis=2)
    win_idx = np.where(row_check == 5)
    if win_idx[0].size > 0:
        return True, win_idx[0]

    # Find full column
    col_check = np.sum(tmp_arr, axis=1)
    win_idx = np.where(col_check == 5)
    if win_idx[0].size > 0:
        return True, win_idx[0]
    return False, -1

marker_arr = np.zeros_like(boards_arr)

# Play Bingo
for n in sequence:
    marker_arr[np.where(boards_arr == n)] = 1
    win, win_idx = check_winner(marker_arr)
    if not win:
        continue
    break

# Compute Score
win_board = boards_arr[win_idx]
win_marks = marker_arr[win_idx]
unmarked_sum = np.sum(win_board[win_marks == 0])
score = unmarked_sum * n
print(unmarked_sum, n, score)

# Part 2
# Reset Markers
marker_arr = np.zeros_like(boards_arr)

# Play Bingo
for n in sequence:
    marker_arr[np.where(boards_arr == n)] = 1
    win, win_idx = check_winner(marker_arr)
    if not win:
        continue
    # Remove Winning board until last one wins
    if boards_arr.shape[0] == 1:
        break
    boards_arr = np.delete(boards_arr, win_idx, axis=0)
    marker_arr = np.delete(marker_arr, win_idx, axis=0)

# Compute remaining winning score
win_board = boards_arr[0]
win_marks = marker_arr[0]
unmarked_sum = np.sum(win_board[win_marks == 0])
score = unmarked_sum * n
print(unmarked_sum, n, score)
