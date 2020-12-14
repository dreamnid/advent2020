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

INPUT_FILE='14-input.txt'
#INPUT_FILE='14a-example.txt'
#INPUT_FILE='14b-example.txt'

input = [line for line in get_file_contents(INPUT_FILE)[0]]

prog = re.compile(r'mem\[([\d]+)\] = ([\d]+)')
def parse_mask(cur_mask: str) -> Tuple[int, int]:
    cur_mask_or = int(cur_mask.replace('X', '0'), base=2)
    cur_mask_and = int(cur_mask.replace('X', '1'), base=2)

    return cur_mask_or, cur_mask_and

def run_mask_value():
    cur_mask_or = None
    cur_mask_and = None
    memory = defaultdict(int)
    for line in input:
        if line.startswith(('mask')):
            cur_mask_or, cur_mask_and = parse_mask(line[7:])
            #print('new mask', cur_mask_or, cur_mask_and)
        else:
            found = prog.match(line)
            addr = int(found.group(1))
            memory[addr] = int(found.group(2)) & cur_mask_and | cur_mask_or
            #print(addr, found.group(2), memory[addr])
    return sum(memory.values())

def run_mask_addr():
    cur_mask = None
    memory = defaultdict(int)
    for line in input:
        if line.startswith(('mask')):
            cur_mask = line[7:]
            #print('mask', cur_mask)
        else:
            found = prog.match(line)
            value = int(found.group(2))

            floating_bits = [idx for idx, value in enumerate(cur_mask) if value == 'X']
            for i in range(int(math.pow(2, len(floating_bits)))):
                #print('b {:036b}'.format(i))
                i_bin_str = '{:036b}'.format(i)
                addr = int(found.group(1)) | int(cur_mask.replace('X', '1'), base=2)
                addr_str = list('{:36b}'.format(addr))
                #print('old addr str', addr, i_bin_str)

                # Convert to string to do bit manipulation
                # Have to reverse iteration for j to access the lowest bytes first
                for j, float_bit in enumerate(reversed(floating_bits)):
                    #print(float_bit, -j, len(i_bin_str)-1-j, i_bin_str[len(i_bin_str)-1-j])
                    addr_str[float_bit] = i_bin_str[len(i_bin_str)-1-j]

                #print(''.join(addr_str))
                addr = int(''.join(addr_str), base=2)
                #print('Addr     {:036b}'.format(int(found.group(1))))
                #print('new addr {:036b} {}'.format(addr, addr))
                memory[addr] = value
    return sum(memory.values())

print('a: ', run_mask_value())
print('b: ', run_mask_addr())
