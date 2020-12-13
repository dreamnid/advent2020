#!/usr/bin/env python3
from collections import defaultdict
from functools import partial, reduce
import math
import os
import re
from time import time
from typing import Dict, List, Set, Union

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

inputs = [line for line in get_file_contents(INPUT_FILE)[0]]
desired_time = int(inputs[0])

def yufei_find_step_size(bus_and_offset):
    # Ref: https://github.com/YufeiG/adventofcode2020/blob/46e50685581fb004daa3d3ddf2e5527fa73e6ce0/script13.py#L23
    largest_step_size = None
    largest_step_size_i = None
    for (reference_i, reference_bus) in bus_and_offset:
        bus_numbers_that_leave_with_reference_bus = []
        for (i, bus) in bus_and_offset:
            if i == reference_i:
                continue
            if abs(reference_i - i) == bus:
                print('Yuf found', reference_i, reference_bus, i, bus)
                bus_numbers_that_leave_with_reference_bus.append(bus)
        step = reference_bus * yufei_multiply_list(bus_numbers_that_leave_with_reference_bus)
        print('Yuf simul buses', reference_i, reference_bus, bus_numbers_that_leave_with_reference_bus, step)
        if largest_step_size is None or largest_step_size < step:
            largest_step_size = step
            largest_step_size_i = reference_i

    return largest_step_size, largest_step_size_i

def yufei_multiply_list(myList) :
    # Ref: https://github.com/YufeiG/adventofcode2020/blob/46e50685581fb004daa3d3ddf2e5527fa73e6ce0/script13.py#L4
    # Multiply elements one by one
    result = 1
    for x in myList:
         result = result * x
    return result

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
    print(len(input_split), input_split)
    bus_schedule = {i:int(x) for i, x in enumerate(input_split) if x != 'x'}
    print(bus_schedule)


    any_simulatenous_buses = []
    for offset, bus_itr in bus_schedule.items():
        if bus_itr+offset in bus_schedule:
            any_simulatenous_buses.append((bus_itr+offset, bus_schedule[bus_itr+offset]))

    print('Simultaneous bus', any_simulatenous_buses)
    print('Yuf step size & i', yufei_find_step_size(bus_schedule.items()))


    return
    try:
        increment = any_simulatenous_buses[0][0] * any_simulatenous_buses[0][1]
        diff=any_simulatenous_buses[0][0]
    except:
        increment = bus_schedule[0]
        diff = 0
    print(increment)

    time = 100000000000000
    #time = 0
    while True:
        if time % increment == 0:
            break
        time += 1
    print('starting at ', time)

    cur_time = finder(time, increment, diff, bus_schedule)

    if cur_time:
        print('answer:', cur_time)
    else:
        print('nope')

def finder(start_time, increment, subtract, bus_schedule):
    time = start_time
    cur_time = 0
    try:
        while True:
            if cur_time % 1000 == 0 and False:
                print(humanize.intcomma(cur_time))
            #print(time)
            found = True
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
#a()
b()

def b_debug():
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

