#!/usr/bin/env python3
from functools import partial, reduce

INPUT_FILE = '3-input.txt'
#INPUT_FILE = 'example-input.txt'

rows = []
with open(INPUT_FILE) as fh:
    for line in fh:
        rows.append(line.strip())

def find_trees(rows, right, down=1) -> int:
    trees = 0

    row_idx = 0
    col_idx = 0
    for row_idx in range(0, len(rows), down):
        row = rows[row_idx]
        if False:
            for j in range(len(row)):
                if j == col_idx:
                    if row[j] == '.':
                        print('O', end='')
                    else:
                        print('X', end='')
                else:
                    print(row[j], end='')
            print('')

        if row[col_idx] == '#':
            trees += 1
        col_idx += right
        col_idx %= len(row) 

    return trees

find_trees_rows = partial(find_trees, rows)

desired = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]

res = reduce(lambda a, b: a*b, map(find_trees_rows, *zip(*desired)))
print(f'Res {res}')
