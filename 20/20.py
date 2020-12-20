#!/usr/bin/env python3
from collections import defaultdict
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
#INPUT_FILE='20a-example.txt'

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
