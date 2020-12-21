#!/usr/bin/env python3
from collections import defaultdict
from copy import deepcopy
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
#INPUT_FILE='19b-example.txt'

rules = dict()
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


def matcher(rule_id: int, match: str, rules: Dict[int, List[List[Union[str, int]]]]) -> str:
    res = []
    for rule in rules[rule_id]:
        #print('Rule', rule_id, rule)
        buffer = ['']
        for el in rule:
            found = False
            new_buf = []
            for cur_buf in buffer:
                #print('--')
                #print('top of cur_buf', cur_buf, buffer)

                found = False
                if len(cur_buf) >= len(match):
                    # Rule has more chars required than what we have
                    reason = 'too long'
                    break

                if isinstance(el, int):
                    cur_poss = matcher(el, match[len(cur_buf):], rules)
                    if cur_poss:
                        for poss in cur_poss:
                            new_buf.append(cur_buf + poss)
                        found |= True
                    else:
                        reason = 'matcher returned None'
                        #print(reason, el, f'[{match[len(cur_buf):]}]')
                else:
                    if el == match[len(cur_buf)]:
                        new_buf.append(cur_buf + el)
                        found |= True
                        reason = f'char match: {el} == {match[len(cur_buf)]}, {match[:len(cur_buf)] + "[" + match[len(cur_buf)] + "]" + match[len(cur_buf)+1:]}'
                        #print(reason)
                    else:
                        reason = f'char does not match: {el} != {match[len(cur_buf)]}, {match[:len(cur_buf)] + "[" + match[len(cur_buf)] + "]" + match[len(cur_buf)+1:]}'
                        #print(reason)
                        pass
            #print('new_buf', new_buf)
            buffer = new_buf

        if buffer:
            res += buffer
        #print('buffer', buffer)
    return res if res else None



def find_matches(messages, rules):
    valid_messages = []
    too_long = []

    for message in messages:
    #    print('Matching ', message)
        res = matcher(0, message, rules)
        if res and res[0] == message:
            valid_messages.append(message)
        elif res:
            too_long.append(message)
    #    print()
    #    print(valid_messages, too_long)

    #    print('----------------')
    return valid_messages, too_long


messages = [line for line in get_file_contents(INPUT_FILE)[1]]
start_a = time()
valid_messages, _ = find_matches(messages, rules)
print('Part a - Total valid messages:', len(valid_messages), '/', len(messages))
start_b = time()
print('Part a timing:', start_b - start_a)
print()

# For part b - introducing loops
# Have to use deepcopy since deep_copy_json uses json to clone and json doesn't support int strings
new_rules = deepcopy(rules)
new_rules[8] = [[42], [42, 8]]
new_rules[11] = [[42, 31], [42, 11, 31]]

valid_messages, _ = find_matches(messages, new_rules)
print('Part b - Total valid messages:', len(valid_messages), '/', len(messages))
print('Part b timing:', time() - start_b)
