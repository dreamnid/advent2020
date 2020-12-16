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

def part_a()

ordering = [None]  * len(rules)
field_idx: Dict[str, int] = {}
not_valid = []
valid_tickets = []
not_valid_rule = defaultdict(set)
valid_rule = defaultdict(set)
for cur_ticket in others:
    ticket_valid = True
    for pos, number in enumerate(cur_ticket):
        valid = False

        for rule, constraints in rules.items():
            valid |= (constraints[0] <= number <= constraints[1]) or (constraints[2] <= number <= constraints[3])
            #print(number, valid)

        if not valid:
            not_valid.append(number)
            ticket_valid = False
            break

    if ticket_valid:
        valid_tickets.append(cur_ticket)

print('hi', mine + valid_tickets)

for cur_ticket in mine + valid_tickets:
    for pos, number in enumerate(cur_ticket):
        valid = False

        for rule, constraints in rules.items():
            valid |= (constraints[0] <= number <= constraints[1]) or (constraints[2] <= number <= constraints[3])
            #print(number, valid)

            if valid and pos not in not_valid_rule[rule]:
                valid_rule[rule].add(pos)
            else:
                if pos in valid_rule[rule]:
                    valid_rule[rule].remove(pos)
                not_valid_rule[rule].add(pos)

        if not valid:
            break

print(dict(valid_rule))
poss_rule_combos = []

from itertools import product
for i in product(*list(valid_rule.values())):
    valid = True
    seen = set()
    for j in i:
        if j not in seen:
            seen.add(j)
        else:
            valid = False
            break
    if valid:
        poss_rule_combos.append(i)
print(poss_rule_combos)


rules_name_idx = list(valid_rule.keys())
rules_list = [rules[rule] for rule in valid_rule.keys()]
print('ruleslist', rules_list)


not_valid_rule = defaultdict(set)
valid_rule = defaultdict(set)
good_combo = None
for cur_field_combo in poss_rule_combos:
    valid = True
    for cur_ticket in mine + valid_tickets:
        valid = True
        for cur_pos in cur_field_combo:
            number = cur_ticket[cur_pos]
            constraints = rules_list[cur_pos]

            valid &= (constraints[0] <= number <= constraints[1]) or (constraints[2] <= number <= constraints[3])

            if not valid:
                break
    if valid:
        good_combo = cur_field_combo
        break
assert good_combo
print(good_combo)

answer_b = []
for i, field in enumerate(mine):
    if rules_name_idx[good_combo[i]].startswith('departure'):
        answer_b.append(field)

print('part a:', sum(not_valid))
print('part b:', reduce(mul, answer_b, 1))
