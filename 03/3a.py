#!/usr/bin/env python3
import itertools

INPUT_FILE = '3-input.txt'
#INPUT_FILE = 'example-input.txt'

with open(INPUT_FILE) as fh:
    rows = [line.strip() for line in fh

col_idx = 0
trees = 0

# Move: Down 1 row, right 3
for row in rows:
    # for j in range(len(row)):
    #     if j == col_idx:
    #         if row[j] == '.':
    #             print('O', end='')
    #         else:
    #             print('X', end='')
    #     else:
    #         print(row[j], end='')
    # print('')

    if row[col_idx] == '#':
        trees += 1
    col_idx += 3
    col_idx %= len(row) 

print('Trees', trees)
    