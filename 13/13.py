#!/usr/bin/env python3
from collections import defaultdict
from functools import partial, reduce
import math
import os
import re
from time import time
from typing import Dict, List, Set, Union

# Fix path so we can do a relative import: https://stackoverflow.com/a/27876800
if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

        # Relative imports here
        from util import *

INPUT_FILE='13-input.txt'
INPUT_FILE='13a-example.txt'

inputs = [line for line in get_file_contents(INPUT_FILE)[0]]
desired_time = int(inputs[0])

def a():
    min_diff = None
    best_bus = None
    for bus in [int(x) for x in inputs[1].split(',') if x != 'x']:
        diff = math.ceil(desired_time/bus) * bus - desired_time
        if not min_diff or diff < min_diff:
            min_diff = diff
            best_bus = bus
    print(min_diff, best_bus, min_diff*best_bus)

def b():
    input_split = inputs[1].split(',')
    print(input_split)
    bus_schedule = {i:int(x) for i, x in enumerate(input_split) if x != 'x'}

    any_simulatenous_buses = []
    for offset, bus_itr in bus_schedule.items():
        if bus_itr+offset in bus_schedule:
            any_simulatenous_buses.append((bus_itr+offset, bus_schedule[bus_itr+offset]))

    print(any_simulatenous_buses)
    time = 1068788
    found = True
    cur_time = 0
    while True:
        print(time)
        cur_time = time -7
        for offset, bus_itr in bus_schedule.items():
            found &= ((cur_time + offset) % bus_itr) == 0
            print('itr: ', offset, cur_time+offset, bus_itr, found)
            if not found:
                break

        if found:
            break

        time += 133

        if time > 1068789:
            break

    if found:
        print(cur_time)
    else:
        print('nope')

a()
b()
