#!/usr/bin/env python3
from collections import defaultdict
import copy
from functools import partial, reduce
import math
import os
import pprint
import re
from typing import Dict, List, Set, Union

# Fix path so we can do a relative import: https://stackoverflow.com/a/27876800
if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

        # Relative imports here
        from util import *

INPUT_FILE='11-input.txt'
#INPUT_FILE='11a-example.txt'

input = [list(line) for line in get_file_contents(INPUT_FILE)[0]]

total_rows = len(input)
total_cols = len(input[0])

def get_adjacent(input, row: int, col: int):
    res = []
    for i in range(-1, 2):
        #print('i', i, row + i)
        if not (0 <= row + i < total_rows):
            continue

        for j in range(-1, 2):
            #print('j', j, col + j)
            if not (0 <= col + j < total_cols):
                continue

            if i == j == 0:
                # only want adjacent elements, not itself
                continue
            #print('i', i, 'j', j, row+i, col+j, input[row+i][col+j])
            res.append(input[row+i][col+j])
    return res

def find_first_non_empty(input: List[List[str]], row: int, col: int, row_mul: int, col_mul: int) -> Union[str, None]:
    """
    Find the first non floor neighbor (i.e. not a '.')

    row_mul and col_mul is used to specify the direction to search in.
    For example, if both row_mul and col_mul are 1, it will search down-right (diagonal)
    from the given row, col position

    :param input: The input to search
    :param row: The row index in input to search from
    :param col: The column index in input to search from
    :param row_mul: Either -1, 0, or 1
    :param col_mul: Either -1, 0, or 1
    :return:
    """
    max_dim = max(total_rows, total_cols)
    for i in range(1, max_dim):
        tmp_row = row + i*row_mul
        if 0 <= tmp_row < total_rows:
            tmp_col = col + i*col_mul
            if 0 <= tmp_col < total_cols:
                tmp_loc = input[tmp_row][tmp_col]
                if tmp_loc != '.':
                    return tmp_loc
            else:
                break
        else:
            break

def get_first_non_floor(input, row: int, col: int):
    """
    Find the first non floor neighbors from 8 directions: upper-left, up, upper-right, etc.
    """
    return [val for i in range(-1, 2) for j in range(-1, 2)
            if (not (i == j == 0)) and (val := find_first_non_empty(input, row, col, i, j)) is not None]

def process(input, finder_func, num_occupied_seats):
    round = 0
    has_changed = False
    result = copy.deepcopy(input)

    while True:
        old_input = copy.deepcopy(result)
        for i in range(total_rows):
            for j in range(total_cols):
                cur_seat = result[i][j]
                num_occupied_adj_seats = sum([seat == '#' for seat in finder_func(old_input, i, j)])
                if cur_seat == 'L' and num_occupied_adj_seats == 0:
                    result[i][j] = '#'
                    has_changed = True
                elif cur_seat == '#':
                    if num_occupied_adj_seats >= num_occupied_seats:
                        result[i][j] = 'L'
                        has_changed = True
        #print('round', round)
        #pprint.pprint(result)

        if not has_changed:
            break

        has_changed = False
        round += 1
    return result

print(sum([seat == '#' for row in process(input, get_adjacent, 4) for seat in row]))
print(sum([seat == '#' for row in process(input, get_first_non_floor, 5) for seat in row]))
#print(get_first_non_floor(input, 0, 0))


