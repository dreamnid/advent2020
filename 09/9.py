#!/usr/bin/env python3
from collections import defaultdict
from functools import partial, reduce
import math
import os
import re
import sys
from typing import Dict, List, Set, Union

# Fix path so we can do a relative import: https://stackoverflow.com/a/27876800
if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

        # Relative imports here
        from util import *

INPUT_FILE='9-input.txt'
#INPUT_FILE='9a-example.txt'
PREAMBLE_COUNT = 25

#INPUT_FILE='9b-example.txt'
#PREAMBLE_COUNT = 5

content = [int(num) for num in get_file_contents(INPUT_FILE)[0]]

target = 0
for t in range(PREAMBLE_COUNT, len(content)):
    buffer = sorted(content[t-PREAMBLE_COUNT: t])
    target = content[t]

    parts = find_var_parts_sum(buffer, target, num_addends=2)
    #print(t, buffer, target, parts)
    if not parts or parts[0] == parts[1]:
        print('target not found: ', target)
        break


for t in range(len(content)-PREAMBLE_COUNT):
    buffer = content[t:t+PREAMBLE_COUNT]
    #print(t, buffer, target, parts)
    for i in range(PREAMBLE_COUNT):
        for j in range(1, PREAMBLE_COUNT):
            if sum(buffer[i:j]) == target:
                print('Found!', buffer[i:j], 'min+max:', min(buffer[i:j]) + max(buffer[i:j]))
                sys.exit(0)

