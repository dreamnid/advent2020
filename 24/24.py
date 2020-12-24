#!/usr/bin/env python3
from collections import defaultdict
from copy import deepcopy
from functools import partial, reduce
from itertools import chain, cycle, takewhile
import math
from operator import mul
import os
import pprint
import re
from time import time
from typing import Dict, List, Set, Tuple, Union

# Fix path so we can do a relative import: https://stackoverflow.com/a/27876800
if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

        # Relative imports here
        from util import *

INPUT_FILE='24-input.txt'
#INPUT_FILE='24a-example.txt'

input = [line for line in get_file_contents(INPUT_FILE)[0]]
#input = ['nwwswee']

def print_grid(grid, x_size=None, y_size=None):
    init = set(grid.keys()).pop()
    min_x = init[0]
    max_x = init[0]
    min_y = init[1]
    max_y = init[1]

    for pos in grid.keys():
        if pos[0] < min_x:
            min_x = pos[0]
        if pos[0] > max_x:
            max_x = pos[0]
        if pos[1] < min_y:
            min_y = pos[1]
        if pos[1] > max_y:
            max_y = pos[1]

    if x_size:
        tmp = int(x_size / 2)
        min_x = -tmp
        max_x = tmp
    if y_size:
        tmp = int(y_size / 2)
        min_y = -tmp
        max_y = tmp

    for row in range(max_y, min_y-1, -1):
        for col in range(min_x, max_x+1):
            if row % 2 == 1 and col == min_x:
                print(' ', end='')
            if row == 0 and col == 0:
                print('\033[1mZ\033[0m' if grid[(col, row)] else 'z', end=' ')
            else:
                print('\033[1mB\033[0m' if grid[(col, row)] else 'w', end=' ')

        print()

start_a = time()
grid = defaultdict(bool)

# Parse inputs to determine which tiles were flipped
for line in input:
    point = [0, 0]
    while True:
        if not line:
            break
        char2 = line[0:2]
        char1 = line[0]
        found = False
        # "odd-r" horizontal layout - shoves odd rows to the right
        # Ref: https://www.redblobgames.com/grids/hexagons/#coordinates-offset
        if char2 == 'ne':
            if point[1] % 2 == 0:
                point[0] += 0
                point[1] += 1
            else:
                point[0] += 1
                point[1] += 1
            found = True
        elif char2 == 'se':
            if point[1] % 2 == 0:
                point[0] += 0
                point[1] -= 1
            else:
                point[0] += 1
                point[1] -= 1
            found = True
        elif char2 == 'sw':
            if point[1] % 2 == 0:
                point[0] -= 1
                point[1] -= 1
            else:
                point[0] -= 0
                point[1] -= 1
            found = True
        elif char2 == 'nw':
            if point[1] % 2 == 0:
                point[0] -= 1
                point[1] += 1
            else:
                point[0] -= 0
                point[1] += 1

            found = True
        if found:
            #print(line[:2], end=' ')
            line = line[2:]
            continue

        if char1 == 'e':
            point[0] += 1
        elif char1 == 'w':
            point[0] -= 1
        else:
            assert False, 'bad'
        #print(line[0], end=' ')
        line = line[1:]

    point_tuple = tuple(point)
    #print('   ', point_tuple)
    grid[point_tuple] = not grid[point_tuple]



def getAdjacentCoordinates(cur_node: Tuple[int, int]) -> List[Tuple[int, int]]:
    """
    Returns the coordinates for the adjacent tiles

    :param cur_node: the tuple containing the row index and column index
    :return: A list of row and col indices whose order is the following: NE (north-east node), SE, SW, NW, E, W
    """
    res = []
    if cur_node[1] % 2 == 0:
        # ne
        res.append((cur_node[0], cur_node[1]+1))
        # se
        res.append((cur_node[0], cur_node[1]-1))
        # sw
        res.append((cur_node[0]-1, cur_node[1]-1))
        # nw
        res.append((cur_node[0]-1, cur_node[1]+1))
    else:
        # ne
        res.append((cur_node[0]+1, cur_node[1]+1))
        # se
        res.append((cur_node[0]+1, cur_node[1]-1))
        # sw
        res.append((cur_node[0], cur_node[1]-1))
        # nw
        res.append((cur_node[0], cur_node[1]+1))

    # e
    res.append((cur_node[0]+1, cur_node[1]))
    # w
    res.append((cur_node[0]-1, cur_node[1]))

    return res


def getAdjacentNodes(cur_node: Tuple[int, int], grid: Dict[Tuple[int, int], bool]) -> List[bool]:
    """
    Returns the adjacent tiles for the given tile

    :param cur_node: the tuple containing the row index and column index
    :return: A list of adjacent tiles whose order is the following: NE (north-east node), SE, SW, NW, E, W
    """
    return list(map(lambda x: grid[x], getAdjacentCoordinates(cur_node)))


print('part a:', sum([value for value in grid.values()]))
print('part a timing:', time() - start_a)
print()
start_b = time()

print('Initial grid')
print_grid(grid)
print('='*80)
# Start part b
for turn in range(100):
    new_grid = deepcopy(grid)
    potential_white = set()

    # since grid is a default dict, accessing previously un-accessed keys will cause the size of the dict to change so
    # need to make a copy first
    grid_copy = grid.copy()

    for pos, value in grid_copy.items():
        #print('pos', pos, 'val', value, 'num black adj', num_black)
        if value:
            adj_nodes = getAdjacentNodes(pos, grid)
            num_black = sum(adj_nodes)

            new_grid[pos] = not (num_black == 0 or num_black > 2)

            # Black hexagons next to each other means any white neighbor needs to be true
            if num_black > 0:
                adj_coords = getAdjacentCoordinates(pos)
                if adj_nodes[0]:
                    # black neighbor is ne, check nw and e
                    check_pos = adj_coords[3]
                    if not grid[check_pos]:
                        potential_white.add(check_pos)
                    check_pos = adj_coords[4]
                    if not grid[check_pos]:
                        potential_white.add(check_pos)
                if adj_nodes[1]:
                    # black neighbor is se, check e and sw
                    check_pos = adj_coords[4]
                    if not grid[check_pos]:
                        potential_white.add(check_pos)
                    check_pos = adj_coords[2]
                    if not grid[check_pos]:
                        potential_white.add(check_pos)
                if adj_nodes[2]:
                    # black neighbor is sw, check se, w
                    check_pos = adj_coords[1]
                    if not grid[check_pos]:
                        potential_white.add(check_pos)
                    check_pos = adj_coords[5]
                    if not grid[check_pos]:
                        potential_white.add(check_pos)
                if adj_nodes[3]:
                    # black neighbor is nw, check ne, w
                    check_pos = adj_coords[0]
                    if not grid[check_pos]:
                        potential_white.add(check_pos)
                    check_pos = adj_coords[5]
                    if not grid[check_pos]:
                        potential_white.add(check_pos)
                if adj_nodes[4]:
                    # black neighbor is e, check ne, se
                    check_pos = adj_coords[0]
                    if not grid[check_pos]:
                        potential_white.add(check_pos)
                    check_pos = adj_coords[1]
                    if not grid[check_pos]:
                        potential_white.add(check_pos)
                if adj_nodes[5]:
                    # black neighbor is w, check sw, nw
                    check_pos = adj_coords[2]
                    if not grid[check_pos]:
                        potential_white.add(check_pos)
                    check_pos = adj_coords[3]
                    if not grid[check_pos]:
                        potential_white.add(check_pos)


    # Go through our candidates of white -> black to make sure they actually only have 2 adjacent black nodes
    for pos in potential_white:
        new_grid[pos] = sum(getAdjacentNodes(pos, grid)) == 2

    # Now that we've visited all the black square and checked its neighbors, all the eligible white squares should be
    # be found.
    for pos, value in grid.copy().items():
        if not value:
            new_grid[pos] = sum(getAdjacentNodes(pos, grid)) == 2

    grid = new_grid

    # Since the graph can grow pretty big, only show the first few turns
    if turn < 8 and False:
        print('turn:', turn+1, sum([value for value in grid.values()]))
        print_grid(grid)
        print()
#pprint.pprint(grid)
print('*********')
print('part b:', sum([value for value in grid.values()]))
print('part b timing', time() - start_b)
