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

INPUT_FILE='23-input.txt'
#INPUT_FILE='23a-example.txt'

input = [int(char) for line in get_file_contents(INPUT_FILE)[0] for char in line]
#print(input)
from itertools import cycle, islice
cur_cup_idx = 0
new_list = input.copy()
for turn in range(100):
    current_cup = new_list[cur_cup_idx]
    #print(turn+1, '{}[{}]{}'.format(''.join([str(i) for i in new_list[:cur_cup_idx]]), current_cup, ''.join([str(i) for i in new_list[cur_cup_idx+1:]])))
    cycle_list = cycle(new_list)
    pick_up = list(islice(cycle(new_list), cur_cup_idx+1, cur_cup_idx+4))
    for i in pick_up:
        new_list.pop(new_list.index(i))
    #print(turn+1, pick_up, '{}[{}]{}'.format(''.join([str(i) for i in new_list[:cur_cup_idx]]), current_cup, ''.join([str(i) for i in new_list[cur_cup_idx+1:]])))
    #print(turn + 1, current_cup, pick_up, new_list)


    target = current_cup
    while True:
        target -= 1
        if min(new_list) > target:
            target = max(new_list)

        if target in new_list:
            idx = new_list.index(target)
            #print('target', target, 'idx', idx)
            # if idx == len(new_list) - 3:
            #     new_list.append(pick_up[0])
            #     new_list += pick_up[1:]
            # elif idx == len(new_list) - 2:
            #     new_list += pick_up[:2]
            #     new_list += pick_up[2:]
            # elif idx == len(new_list) - 1:
            #     new_list += pick_up
            # else:
            new_list = new_list[:idx+1] + pick_up + new_list[idx+1:]
            cur_cup_idx = new_list.index(current_cup) + 1
            cur_cup_idx %= len(input)
            break
#print('new_list', new_list)
idx = new_list.index(1)
print(''.join([str(i) for i in new_list[idx+1:]] + [str(i) for i in new_list[:idx]]))

