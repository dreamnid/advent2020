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

# Fix path so we can do a relative import: https://stackoverflow.com/a/27876800
if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

        # Relative imports here
        from util import *

INPUT_FILE='15-input.txt'
#INPUT_FILE='15a-example.txt'

input = [int(num) for num in get_file_contents(INPUT_FILE)[0][0].split(',')]

def nth_num_spoken(num:int) -> int:
    seen = {num:idx for idx, num in enumerate(input[0:-1])}
    new = input[-1]
    cur_num = input[-1]
    for i in range(len(input), num):
        if cur_num in seen and seen[cur_num] != (i-1):
            cur_num = i - seen[cur_num] - 1
        else:
            cur_num = 0

        seen[new] = i - 1
        new = cur_num
    return cur_num

start = time()
print('2020th number spoken:', nth_num_spoken(2020))
startb = time()
print('a timing: ', startb - start)
print('30000000th number spoken:', nth_num_spoken(30000000))
print('b timing: ', time() - startb)
print()
print('overall timing:', time() - start)
