#!/usr/bin/env python3
from collections import defaultdict
from functools import partial, reduce
import math
from operator import mul
import os
import re
from time import time
from typing import Dict, List, Set, Tuple, Union

import humanize

# Fix path so we can do a relative import: https://stackoverflow.com/a/27876800
if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

        # Relative imports here
        from util import *

INPUT_FILE='13-input.txt'
#INPUT_FILE='13a-example.txt'
#INPUT_FILE='13b-example.txt'
#INPUT_FILE='13c-example.txt'
#INPUT_FILE='13d-example.txt'
#INPUT_FILE='13e-example.txt'

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
    bus_schedule = {i:int(x) for i, x in enumerate(input_split) if x != 'x'}
    diff, increment = find_best_step_size(bus_schedule)

    time = 0
    # time = 100000000000000
    # while True:
    #     if time % increment == 0:
    #         break
    #     time += 1
    print(f'starting at {time} with increment {increment} and diff {diff}')

    cur_time = finder(time, increment, diff, bus_schedule)

    if cur_time:
        return cur_time
    else:
        return None

def find_best_step_size(bus_schedule: Dict[int, int]) -> Tuple[int, int]:
    """
    Returns the best step size

    Look for buses that departs at the same time. The step size will be the products of the bus interval.
    We also need to return the offset in order to get back to the reference time (referred to as 't' in the puzzle)

    :param bus_schedule: a dictionary of time offset -> time interval
    :return: a list of tuple pairs where each pair is the the time offset and the increment
    """

    # Thanks to YufeiG for expanding on my observation that step size should be the product of the common bus departure time
    # Was only able to do it for the simplest case of the first bus and the bus that it reference as described in the puzzle
    results = [
        (offset, bus_interval * reduce(mul, [cur_bus_interval for cur_offset, cur_bus_interval in bus_schedule.items()
                                             if offset != cur_offset and abs(offset - cur_offset) == cur_bus_interval],
                                       1)) for offset, bus_interval in bus_schedule.items()]
    # Need to find the largest step size
    return sorted(results, key=lambda x: x[1], reverse=True)[0]


def finder(start_time: int, increment: int, subtract: int, bus_schedule: Dict[int, int]) -> int:
    time = start_time
    cur_time = 0
    try:
        while True:
            if cur_time % 1000 == 0 and False:
                print(humanize.intcomma(cur_time))
            #print(time)
            found = True
            # Since cur_time is the product of common departure times, need to back out to
            # get back to 't'
            cur_time = time - subtract
            for offset, bus_itr in bus_schedule.items():
                found &= ((cur_time + offset) % bus_itr) == 0
                #print('itr: ', offset, cur_time+offset, bus_itr, found)
                if not found:
                    break

            if found:
                break

            time += increment
    except KeyboardInterrupt:
        print('Interrupted, time at ', time)
        return None

    return cur_time

start = time()
print('Part a', a())
startb = time()
print('a timing: ', startb - start)
print('Part b ts: ', b())
print('b timing: ', time() - startb)
print()
print('overall timing:', time() - start)

def b_debug():
    """
    Prints out a debug view of time stamps and if a bus will depart on that time
    """
    input_split = inputs[1].split(',')
    print(len(input_split), input_split)
    bus_schedule = {i:int(x) for i, x in enumerate(input_split) if x != 'x'}
    start = 3410
    limit = start + 50

    print('    ', end='')
    for x in range(start, limit):
        print('{:02d}'.format(x), end=' ')

    print()

    for offset, bus_itr in bus_schedule.items():
        print('{:02d}  '.format(bus_itr), end='')
        for x in range(start, limit):
            if (x-offset) % bus_itr == 0:
                print('D ', end=' ')
            else:
                print('  ', end=' ')
        print()

#b_debug()

