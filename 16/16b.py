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
mine = [int(x) for x in get_file_contents(INPUT_FILE)[1][1].split(',')]
others = [[int(x) for x in line.split(',')] for line in get_file_contents(INPUT_FILE)[2][1:]]

ranges_regex = re.compile(r' ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)$')
rules = {}
for cur_line in rules_input:
    line_parts = cur_line.split(':')
    type = line_parts[0]
    ranges_match = ranges_regex.match(line_parts[1])
    ranges = [int(ranges_match.group(i)) for i in range(1, 5)]
    rules[type] = ranges

valid_tickets = []
valid_rule = defaultdict(set)

# Get rid of bad tickets by looking for values in a ticket that doesn't match any rule.
# The any says that number in a ticket can match any rule
# The all says all numbers in the ticket must at least match one rule
valid_tickets = [cur_ticket for cur_ticket in others if
                 all([any(
                     [(constraints[0] <= number <= constraints[1]) or (constraints[2] <= number <= constraints[3]) for
                      constraints in rules.values()])
                      for number in cur_ticket])]

# Group all the field values together. The ith element in the list contains the ith value in all the tickets
fields_values = [sorted(list(i)) for i in zip(*([mine]+valid_tickets))]

print('pos | values for that position')
for i, row in enumerate(fields_values):
    print(f'{i:03d} | ', end=' ')
    for col in row:
        print(f'{col:03d}', end=' ')
    print()

pos_to_rule_poss = [set() for i in range(len(rules))]
count = 0
for rule, constraints in rules.items():
    for pos, cur_field_values in enumerate(fields_values):
        valid = True
        for number in cur_field_values:
            valid &= (constraints[0] <= number <= constraints[1]) or (constraints[2] <= number <= constraints[3])
            #print(number, valid)

            if not valid:
                if pos == 0 and False:
                    count += 1
                    print('Not valid due to ', number, rule, constraints, pos, count)
                break

        if valid:
            if pos == 0 and False:
                print('Adding', rule, constraints, pos, count)
            valid_rule[rule].add(pos)
            pos_to_rule_poss[pos].add(rule)


print('Poss position per rule:', dict(valid_rule))
from collections import Counter

print('number of poss rules per position:', Counter([j for i in valid_rule.values() for j in i]))

print()
print('Possible rules per position')
for i, pos in enumerate(pos_to_rule_poss):
    print(f'{i:03d} | ', ', '.join(sorted(list(pos))))
print()

def finder(assigned:List[str]=None, used:Set[str]=None) -> List[str]:
    """
    Returns the fields for each index of the list

    :param assigned:
    :param used:
    :return:
    """
    if assigned is None:
        assigned = [None] * len(rules)
    if used is None:
        used = set()

    if sum([rule is None for rule in assigned]) == 0:
        return assigned
    while True:
        possibles_to_use = [None]*len(rules) # Since we're trying to minimize this, set the initial value to the max size
        least_poss_idx = None
        # Find index with smallest set of possibilities
        for i, possibles in enumerate(pos_to_rule_poss):
            if assigned[i]:
                continue
            modified_pos = possibles - used
            if len(modified_pos) == 0:
                # Nothing available to use - so this is not the right path
                return
            elif len(modified_pos) < len(possibles_to_use) and assigned[i] is None:
                possibles_to_use = modified_pos
                least_poss_idx = i

        if len(possibles_to_use) == 1:
            assigned[least_poss_idx] = possibles_to_use.pop()
            used.add(assigned[least_poss_idx])
        else:
            # Recurse for each possibility
            for poss_rule2 in possibles_to_use:
                assigned2 = assigned.copy()
                assigned2[least_poss_idx] = poss_rule2
                used2 = used.copy()
                used2.add(poss_rule2)
                res = finder(assigned2, used2)
                if res:
                    return res

        if sum([rule is None for rule in assigned]) == 0:
            return assigned

assigned = finder()
print(assigned)
answer_b = [field_value for i, field_value in enumerate(mine) if assigned[i].startswith('departure')]

print('part b:', answer_b, reduce(mul, answer_b, 1))
