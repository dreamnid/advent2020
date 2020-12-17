#!/usr/bin/env python3
from collections import defaultdict
import copy
from functools import partial, reduce
import itertools
import math
from operator import mul
import os
import re
from time import time
from typing import Any, Dict, List, Set, Tuple, Union

from humanize import intcomma

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

# Number of dimensions
DIM = 4

input = [line for line in get_file_contents(INPUT_FILE)[0]]
size = len(input)

def create_nth_dimension_array(size: int, dim=2, initial=False):
    return reduce(lambda x, y: [copy.deepcopy(x) if isinstance(x, list) else x for i in range(size)], range(dim), initial)

def print_grid_4d(grid):
    for i in range(size):
        for j in range(size):
            print(f'z={j}, w={i}')
            for k in range(size):
                for l in range(size):
                    print('#' if grid[i][j][k][l] else '.', end='')
                print()
            print()
            print()

grid = create_nth_dimension_array(size, DIM)

for i, row in enumerate(input):
    for j, val in enumerate(row):
        grid[1][1][i][j] = val == '#'

#print_grid(grid)

def get_adjacent(input, *args, **kwargs) -> List[Any]:
    if 'idx' in kwargs:
        idx = kwargs['idx']
    else:
        idx = []

    res = []
    for i in range(-1, 2):
        if not (0 <= args[len(idx)] + i < size):
            continue

        cur_idx = idx + [i]
        if len(cur_idx) < DIM:
            res.extend(get_adjacent(input, *args, **{'idx': cur_idx}))
        else:
            if all((el == 0 for el in cur_idx)):
                # only want adjacent elements, not itself
                continue

            res.append(reduce(lambda x, y: x[args[y] + cur_idx[y]], range(DIM), input))
            pass
            #res.append(input[row+i][col+j][dep+k][four+l])
    return res

for cycle in range(6):
    print(f'\nCycle {cycle+1}')
    size += 2
    enlarge_grid = create_nth_dimension_array(size, DIM)
    new_grid = copy.deepcopy(enlarge_grid)
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

# Reduce unflattens the list
print(sum(reduce(lambda x, y: itertools.chain.from_iterable(x), range(DIM - 1), grid)))