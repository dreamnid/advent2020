#!/usr/bin/env python3
from collections import defaultdict
from functools import partial, reduce
from itertools import chain, cycle, starmap, takewhile
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

INPUT_FILE='25-input.txt'
#INPUT_FILE='25a-example.txt'

input = [int(line) for line in get_file_contents(INPUT_FILE)[0]]

def calc_loop_size(target: int) -> int:
    value = 1
    loop=1
    while True:
        value *= 7
        value %= 20201227

        if value == target:
            break

        loop += 1

    return loop

def get_transform(subject: int, loop_size: int) -> int:
    return reduce(lambda x, y: (x * subject) % 20201227, range(loop_size), 1)


loop_nums = list(map(calc_loop_size, input))
print(list(zip(input, reversed(loop_nums))))
encryption_keys = list(starmap(get_transform, zip(input, reversed(loop_nums))))
print('answer a:', encryption_keys[0])