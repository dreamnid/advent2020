#!/usr/bin/env python3
from collections import defaultdict
from functools import partial, reduce
import math
from operator import mul
import os
import re
from time import time
from typing import Dict, List, Set, Tuple, Union

from humanize import intcomma
import copy

# Fix path so we can do a relative import: https://stackoverflow.com/a/27876800
if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

        # Relative imports here
        from util import *

INPUT_FILE='17-input.txt'
#INPUT_FILE='17a-example.txt'

input = [line for line in get_file_contents(INPUT_FILE)[0]]
size = len(input)

def print_grid(grid):
    for i in range(size):
        for j in range(size):
            print(f'z={j}, w={i}')
            for k in range(size):
                for l in range(size):
                    print('#' if grid[i][j][k][l] else '.', end='')
                print()
            print()
            print()

grid = [[[[False for i in range(size)] for i in range(size)] for i in range(size)] for i in range(size)]

for i, row in enumerate(input):
    for j, val in enumerate(row):
        grid[1][1][i][j] = val == '#'

#print_grid(grid)

def get_adjacent(input, row: int, col: int, dep: int, four: int):
    res = []
    for i in range(-1, 2):
        #print('i', i, row + i)
        if not (0 <= row + i < size):
            continue

        for j in range(-1, 2):
            #print('j', j, col + j)
            if not (0 <= col + j < size):
                continue

            for k in range(-1, 2):
                if not (0 <= dep + k < size):
                    continue

                for l in range(-1, 2):
                    if not (0 <= four + l < size):
                        continue

                    if i == j == k == l == 0:
                        # only want adjacent elements, not itself
                        continue

                    res.append(input[row+i][col+j][dep+k][four+l])
    return res

for cycle in range(6):
    print(f'\nCycle {cycle+1}')
    size += 2
    enlarge_grid = [[[[False for i in range(size)] for i in range(size)] for i in range(size)] for i in range(size)]
    new_grid = [[[[False for i in range(size)] for i in range(size)] for i in range(size)] for i in range(size)]
    for i in range(1, size-1):
        for j in range(1, size-1):
            for k in range(1, size-1):
                for l in range(1, size-1):
                    enlarge_grid[i][j][k][l] = grid[i-1][j-1][k-1][l-1]
                    new_grid[i][j][k][l] = grid[i-1][j-1][k-1][l-1]
    #print_grid(new_grid)
    #print('----')

    for i in range(size):
        for j in range(size):
            for k in range(size):
                for l in range(size):
                    num_active = sum(get_adjacent(enlarge_grid, i, j, k, l))
                    if enlarge_grid[i][j][k][l]:
                        new_grid[i][j][k][l] = 2 <= num_active <= 3
                    else:
                        new_grid[i][j][k][l] = num_active == 3
    grid = new_grid
    #print('--------')


#print_grid(grid)
import itertools


print(sum(list(itertools.chain.from_iterable(itertools.chain.from_iterable(itertools.chain.from_iterable(grid))))))

