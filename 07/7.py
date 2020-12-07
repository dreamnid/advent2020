#!/usr/bin/env python3
from collections import defaultdict
from functools import partial, reduce
import math
import os
import re
from itertools import zip_longest
from typing import List, Set, Union

# Fix path so we can do a relative import: https://stackoverflow.com/a/27876800
if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

        # Relative imports here
        from util import *

INPUT_FILE='7-input.txt'
#INPUT_FILE='7a-example.txt'
#INPUT_FILE='7b-example.txt'

rules = defaultdict(dict)
for rule_text in get_file_contents(INPUT_FILE)[0]:
    rule_text_split = rule_text.split(' ')
    if len(rule_text_split) == 7:
        # Accounting for bags that don't contain other bags
        continue

    rules['{} {}'.format(*rule_text_split[:2])] = {'{} {}'.format(*n[1:3]): int(n[0])
                                                   for n in zip_longest(*([iter(rule_text_split[4:])] * 4))}

def contains_shiny_gold(color: str, seen: Set[str]=None) -> bool:
    if seen is None:
        seen = set()
    seen.add(color)
    for child_color, child_count in rules[color].items():
        if child_color == 'shiny gold' and child_count > 0:
            return True
        elif child_count > 0:
            if child_color not in seen:
                if contains_shiny_gold(child_color, seen):
                    return True
    return False

def get_num_bags(color: str) -> int:
    """Returns the number of bags contained inside the specified bag"""
    num_bags = 1
    for child_color, child_count in rules[color].items():
        num_bags += child_count * get_num_bags(child_color)
    return num_bags

print('Num bags that can contain shiny gold', sum([contains_shiny_gold(color) for color in set(rules.keys())]))
print('Num bags that are inside shiny gold bag', get_num_bags('shiny gold')-1)
