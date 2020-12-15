#!/usr/bin/env python3
from collections import defaultdict
from functools import partial, reduce
import math
from operator import mul
import os
import re
from time import time
from typing import Dict, Generator, List, Set, Tuple, Union

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
INPUT_FILE='15a-example.txt'

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

def gnome_talker(limit: int) -> Generator[int, int, None]:
    """
    Generates the nth word spoken

    Note that the generator accepts send to set a new limit that must be higher than the previous limits.
    Done this way to learn how send works. In reality, would yield each number that was spoken

    :param limit: The nth word desired - e.g. 10 for the 10th word spoken
    """
    seen = {num:idx for idx, num in enumerate(input[0:-1])}
    new = input[-1]
    cur_num = input[-1]
    i = len(input)
    while True:
        if cur_num in seen and seen[cur_num] != (i-1):
            cur_num = i - seen[cur_num] - 1
        else:
            cur_num = 0

        seen[new] = i - 1
        new = cur_num

        if i == limit-1:
            send = yield cur_num
            if send is not None and send > i:
                limit = send
            else:
                break
        i += 1


start = time()
talker = gnome_talker(2020)
print('2020th number spoken:', next(talker))
startb = time()
print('a timing: ', startb - start)

# Use send to set new goal
print('30000000th number spoken:', talker.send(3000))
print('b timing: ', time() - startb)
print()
print('overall timing:', time() - start)
