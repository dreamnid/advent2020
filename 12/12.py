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

INPUT_FILE='12-input.txt'
#INPUT_FILE='12a-example.txt'

inputs = [(line[0], int(line[1:])) for line in get_file_contents(INPUT_FILE)[0]]

def a():
    direction = 90
    coordinates = [0, 0]
    for instruction, value in inputs:
        #print(direction, coordinates)
        if instruction == 'F':
            if direction == 90:
                instruction = 'E'
            elif direction == 180:
                instruction = 'S'
            elif direction == 270:
                instruction = 'W'
            elif direction == 0:
                instruction = 'N'

        if instruction == 'N':
            coordinates[1] += value
        elif instruction == 'S':
            coordinates[1] -= value
        elif instruction == 'E':
            coordinates[0] += value
        elif instruction == 'W':
            coordinates[0] -= value
        elif instruction == 'L':
            direction -= value
            direction %= 360
        elif instruction == 'R':
            direction += value
            direction %= 360

    return coordinates

def b():
    ship_coordinates = [0, 0]
    waypoint_offset= [10, 1]
    for instruction, value in inputs:
        #print(ship_coordinates, waypoint_offset)
        if instruction == 'F':
            ship_coordinates[0] += value * waypoint_offset[0]
            ship_coordinates[1] += value * waypoint_offset[1]

        if instruction == 'N':
            waypoint_offset[1] += value
        elif instruction == 'S':
            waypoint_offset[1] -= value
        elif instruction == 'E':
            waypoint_offset[0] += value
        elif instruction == 'W':
            waypoint_offset[0] -= value
        elif instruction == 'L':
            for i in range(int(value/90)):
                tmp = waypoint_offset[1]
                waypoint_offset[1] = waypoint_offset[0]
                waypoint_offset[0] = -tmp
        elif instruction == 'R':
            for i in range(int(value/90)):
                tmp = waypoint_offset[0]
                waypoint_offset[0] = waypoint_offset[1]
                waypoint_offset[1] = -tmp

    return ship_coordinates

start = time()
print('Part a - Manhatten distance:', sum(map(abs, a())))
startb = time()
print('a timing: ', startb - start)
print('Part b - Manhatten distance:', sum(map(abs, b())))
print('b timing: ', time() - startb)
print()
print('overall timing:', time() - start)
