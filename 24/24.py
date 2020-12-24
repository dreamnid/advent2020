#!/usr/bin/env python3
from collections import defaultdict
from functools import partial, reduce
from itertools import chain, cycle, takewhile
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

INPUT_FILE='24-input.txt'
#INPUT_FILE='24a-example.txt'

grid = defaultdict(bool)

input = [line for line in get_file_contents(INPUT_FILE)[0]]
#input = ['nwwswee']

for line in input:
    point = [0, 0]
    while True:
#        print(point, line)
        if not line:
            break
        char2 = line[0:2]
        char1 = line[0]
        found = False
        if char2 == 'ne':
            point[0] += 1
            point[1] += 1
            found = True
        elif char2 == 'se':
            point[0] += 1
            point[1] -= 1
            found = True
        elif char2 == 'sw':
            point[0] -= 1
            point[1] -= 1
            found = True
        elif char2 == 'nw':
            point[0] -= 1
            point[1] += 1
            found = True
        if found:
            line = line[2:]
            continue

        if char1 == 'e':
            point[0] += 2
        elif char1 == 'w':
            point[0] -= 2
        else:
            assert False, 'bad'
        line = line[1:]
    point_tuple = tuple(point)
    grid[point_tuple] = not grid[point_tuple]

print(sum([value for value in grid.values()]))


#print(grid)
