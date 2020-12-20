#!/usr/bin/env python3
from collections import defaultdict
from copy import deepcopy
from functools import partial, reduce
import math
from operator import mul
import os
import pprint
import re
from time import time
from typing import Dict, List, Set, Tuple, Union

from humanize import intcomma

# Fix path so we can do a relative import: https://stackoverflow.com/a/27876800
if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

        # Relative imports here
        from util import *

INPUT_FILE='20-input.txt'
INPUT_FILE='20a-example.txt'

def rotate_cw(matrix: List[str]):
    """
    Rotates matrix clockwise

    Credit: https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
    """
    return [''.join(row) for row in zip(*matrix[::-1])]

def flip_y(matrix: List[str]):
    return matrix[::-1]

def flip_x(matrix: List[str]):
    return [row[::-1] for row in matrix]

tiles = dict()
tile_edges = defaultdict(list)

for tile in get_file_contents(INPUT_FILE):
    cur_tile = []
    tile_num = None

    for i, line in enumerate(tile):
        if i == 0:
            tile_num = int(line[5:-1])
        else:
            cur_tile.append(line)

    tile_size = len(cur_tile)
    first_row = cur_tile[0]
    last_row = cur_tile[-1]
    first_col = ''.join([row[0] for row in cur_tile])
    last_col = ''.join([row[-1] for row in cur_tile])

    # List elements: tile id, start_position in (row, col), increment in (row, col)

    tile_edges[first_row].append((tile_num, (0, 0), (0, 1)))
    tile_edges[first_row[::-1]].append((tile_num, (0, tile_size-1), (0, -1)))

    tile_edges[last_row].append((tile_num, (tile_size-1, 0), (0, 1)))
    tile_edges[last_row[::-1]].append((tile_num, (tile_size-1, tile_size-1), (0, -1)))

    tile_edges[first_col].append((tile_num, (0, 0), (1, 0)))
    tile_edges[first_col[::-1]].append((tile_num, (tile_size-1, 0), (-1, 0)))

    tile_edges[last_col].append((tile_num, (0, tile_size-1), (1, 0)))
    tile_edges[last_col[::-1]].append((tile_num, (tile_size-1, tile_size-1), (-1, 0)))
    tiles[tile_num] = cur_tile

tile_neigh = defaultdict(dict)

for tile_edge, cur_tiles in tile_edges.items():
    if len(cur_tiles) == 1:
        continue

    for idx, tile in enumerate(cur_tiles):
        tile_id = tile[0]
        pos = tile[1]
        incr = tile[2]
        # top (first row)
        if (pos == (0, 0) and incr == (0, 1)) or (pos == (0, tile_size-1) and incr == (0, -1)):
            tile_neigh[tile_id][0] = cur_tiles[idx-1][0]
        # right (last col)
        elif (pos == (0, tile_size-1) and incr == (1, 0)) or (pos == (tile_size-1, tile_size-1) and incr == (-1, 0)):
            tile_neigh[tile_id][1] = cur_tiles[idx-1][0]
        # bottom (last row)
        elif (pos == (tile_size-1, 0) and incr == (0, 1)) or (pos == (tile_size-1, tile_size-1) and incr == (0, -1)):
            tile_neigh[tile_id][2] = cur_tiles[idx-1][0]
        # left (first col)
        elif (pos == (0, 0) and incr == (1, 0)) or (pos == (tile_size-1, 0) and incr == (-1, 0)):
            tile_neigh[tile_id][3] = cur_tiles[idx-1][0]


res = [tile_id for tile_id, edges in tile_neigh.items() if len(edges) == 2]
print('Product of corner tiles: ', reduce(mul, res))

# Idea of how to make the image from the tiles: Build out each row of tiles
#
# For the first tile in the row:
#     For the first row, use the top left corner tile
#     Else, rotate the tile until it aligns with the tile above it
#   In either case, append the rows of each tile to the temp image buf
# For the remaining tiles in the row
#     # Compare current tile to the tile to the left. Rotate title as needed to align. Append its strings to the end of each row in the a temp image buf
# When there is no tile to the right, we're at the end of the row. Append rows of the temp image buf to the main image array

#pprint.pprint(tiles)
pprint.pprint(tile_neigh)

image = []
# Find top-left tile. This will the tile that has a bottom[2], and right neighbor [1]
#pprint.pprint(top_left)

tmp_img_buf = [''] * tile_size
cur_tile_id = 1951
#num_rotations = 1
#need_to_match = ''.join(row[-1] for row in tiles[cur_tile_id])
#need_to_match = ''.join(row[0] for row in tiles[cur_tile_id])
need_to_match = tiles[cur_tile_id][tile_size-1]
#need_to_match = tiles[cur_tile_id][0]
tile_pos = [[]]
tiles_used = set()

def matcher(tile, match):

    def a(flip_x_wanted, flip_y_wanted):
        tmp_tile = deepcopy(tile)

        if flip_x_wanted:
            tmp_tile = flip_x(tmp_tile)

        if flip_y_wanted:
            tmp_tile = flip_y(tmp_tile)

        for num_rotations in range(4):
            if num_rotations > 0:
                tmp_tile = rotate_cw(tmp_tile)

            # Match first column (left side)
            if ''.join([row[0] for row in tmp_tile]) == match:
                return num_rotations, flip_x_wanted, flip_y_wanted, tmp_tile

    res = a(False, False)
    if res:
        return res

    res = a(True, False)
    if res:
        return res

    res = a(False, True)
    if res:
        return res

    res = a(True, True)
    if res:
        return res

    return None

pprint.pprint(tiles[cur_tile_id])
while True:
    #cur_tile = reduce(lambda x, y: rotate_cw(x), range(num_rotations), tiles[cur_tile_id])
    answer = matcher(tiles[cur_tile_id], need_to_match)
    if not answer:
        assert False, 'Bad answer'

    cur_tile = answer[-1]
    num_rotations = answer[0]

    pprint.pprint(answer)


    if tmp_img_buf[0] == '':
        if image:
            # This is the first entry

            # Need to rotate three more time since match was on the left side and need to make it on top to align with row above
            for i in range(1):
                cur_tile = rotate_cw(cur_tile)
            num_rotations += 5
            num_rotations %= 4

        # save the bottom
        row_bottom = cur_tile[tile_size-1]

    pprint.pprint(cur_tile)
    print('num rot', num_rotations)

    tmp_img_buf = [row + cur_tile[idx] for idx, row in enumerate(tmp_img_buf)]
    tile_pos[-1].append(cur_tile_id)
    tiles_used.add(cur_tile_id)

    if answer[2]:
        right_idx = 2 if num_rotations == 0 else num_rotations - 1
    else:
        right_idx = 1 if num_rotations == 0 else num_rotations - 1
    # 0 rotations = idx = 1
    # 1 rotation = idx = 0
    # 2 rotations = idx = -1 or 3
    # 3 rotations = idx = -2 or 2
    print('right idx', right_idx)
    if right_idx in tile_neigh[cur_tile_id]:
        cur_tile_id = tile_neigh[cur_tile_id][right_idx]
        print(cur_tile_id)
        need_to_match = ''.join([row[tile_size-1] for row in cur_tile])
        pass
    else:
        image.extend(tmp_img_buf)
        pprint.pprint(image)
        pprint.pprint(tile_pos)

        # Are we in the last row?
        if len(tile_pos) != len(tile_pos[0]):
            tmp_img_buf= [''] * tile_size

            cur_tile_id = (set(tile_neigh[tile_pos[-1][0]].values()) - tiles_used).pop()
            need_to_match = row_bottom[::-1]
            print('next row', 'cur_tile_id', cur_tile_id, 'need_to_match', need_to_match)
            tile_pos.append([])
        else:
            break
print('------')
pprint.pprint(tile_pos)
pprint.pprint(image)
