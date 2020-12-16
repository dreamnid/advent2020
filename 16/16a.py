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

INPUT_FILE='16-input.txt'
#INPUT_FILE='16a-example.txt'
#INPUT_FILE='16b-example.txt'

rules_input = [line for line in get_file_contents(INPUT_FILE)[0]]
mine = [[int(x) for x in line.split(',')] for line in get_file_contents(INPUT_FILE)[1][1:]]
others = [[int(x) for x in line.split(',')] for line in get_file_contents(INPUT_FILE)[2][1:]]

ranges_regex = re.compile(r' ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)$')
rules = {}
for cur_line in rules_input:
    line_parts = cur_line.split(':')
    type = line_parts[0]
    ranges_match = ranges_regex.match(line_parts[1])
    ranges = [int(ranges_match.group(i)) for i in range(1, 5)]
    rules[type] = ranges

print(rules)


not_valid = []
for cur_ticket in others:
    for pos, number in enumerate(cur_ticket):
        valid = False

        for rule, constraints in rules.items():
            valid |= (constraints[0] <= number <= constraints[1]) or (constraints[2] <= number <= constraints[3])
            #print(number, valid)

        if not valid:
            not_valid.append(number)
            break

print('part a:', sum(not_valid))
