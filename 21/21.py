#!/usr/bin/env python3
from collections import defaultdict
from functools import partial, reduce
import math
from operator import mul
import os
import pprint
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

INPUT_FILE='21-input.txt'
#INPUT_FILE='21a-example.txt'

input = [line for line in get_file_contents(INPUT_FILE)[0]]

start_a = time()
contains_regex = re.compile(r'\(contains (([\w]+(, )?)+)\)')
guesser = defaultdict(lambda: defaultdict(int))
counter_allergens = defaultdict(int)
counter_ingredients = defaultdict(int)
for line in input:
    ingredients = []

    allergens_match = contains_regex.search(line)
    allergens = allergens_match.group(1).split(', ')

    for allergen in allergens:
        counter_allergens[allergen] += 1

    line_split = line.split(' ')
    for word in line_split:
        if not word.startswith('('):
            ingredients.append(word)
            for allergen in allergens:
                guesser[word][allergen] += 1
            counter_ingredients[word] += 1
        else:
            break

pprint.pprint(counter_allergens)
pprint.pprint(counter_ingredients)

pprint.pprint(guesser)

safe_ingredients = []
poss_allergens = defaultdict(set)
for ingredient, cur_allergens in guesser.items():
    #pprint.pprint(cur_allergens.values())
    #pprint.pprint([val == 1 for val in cur_allergens.values()])
    #pprint.pprint([count < counter_allergens[cur_allergen] for cur_allergen, count in cur_allergens.items()])
    if all([count < counter_allergens[cur_allergen] for cur_allergen, count in cur_allergens.items()]):
        safe_ingredients.append(ingredient)
    for cur_allergen, count in cur_allergens.items():
        if count >= counter_allergens[cur_allergen]:
            poss_allergens[cur_allergen].add(ingredient)

#print(len(safe_ingredients), safe_ingredients)
total_times_safe_appears = reduce(lambda x, y: x + counter_ingredients[y], safe_ingredients, 0)
start_b = time()
print(total_times_safe_appears)
print('time a:', start_b - start_a)
print()

allergy_map = {}
while len(allergy_map) < len(counter_allergens):
    for ingredient, poss in poss_allergens.items():
        if ingredient in allergy_map:
            continue
        tmp_poss = poss - set(allergy_map.values())
        if len(tmp_poss) == 1:
            allergy_map[ingredient] = tmp_poss.pop()

print('Allergy mapping')
pprint.pprint(allergy_map)

print('Part (b) Answer:', ','.join([x[1] for x in sorted(allergy_map.items(), key=lambda x: x[0])]))
print('time b:', time() - start_b)
