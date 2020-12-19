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

INPUT_FILE='19-input.txt'
#INPUT_FILE='19a-example.txt'

rules = [None] * len(get_file_contents(INPUT_FILE)[0])
for line in get_file_contents(INPUT_FILE)[0]:
    line_split = line.split(':')
    rule_num = int(line_split[0])
    space_split = line_split[1][1:].split(' ')
    rule = [[]]
    for el in space_split:
        if el.startswith('"'):
            rule[-1].append(el[1:-1])
        elif el != '|':
            rule[-1].append(int(el))
        else:
            rule.append([])
    rules[rule_num] = rule


def matcher(rule: int, match: str) -> str:
    num_found = 0
    res = []
    for rule in rules[rule]:
        matched = ''
        found = False
        idx = 0
        for el in rule:
            found = False
            if idx >= len(match):
                # Rule has more chars required than what we have
                reason = 'too long'
                break

            if isinstance(el, int):
                cur_poss = matcher(el, match[idx:])
                if cur_poss:
                    matched += cur_poss
                    found |= True
                    idx += len(cur_poss)
                else:
                    reason = 'matcher returned None'
                    pass
            else:
                if el == match[idx]:
                    matched += el
                    found |= True
                    idx += 1
                else:
                    reason = f'char does not match: {el} != {match[idx]}, {match[:idx] + "[" + match[idx] + "]" + match[idx+1:]}'
                    pass

            if not found:
                break
        if found:
            res.append(matched)
            num_found += 1
            #break

    return res[0] if num_found else None


messages = [line for line in get_file_contents(INPUT_FILE)[1]]
valid_messages = []
too_long = []

for message in messages:
    tmp = message
    res = matcher(0, message)
    if res and res == message:
        valid_messages.append(message)
    elif res:
        too_long.append(message)

print('Total too long', len(too_long))
print('Total valid messages', len(valid_messages), '/', len(messages))


