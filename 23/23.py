#!/usr/bin/env python3
from collections import defaultdict
from functools import partial, reduce
from itertools import islice
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

INPUT_FILE='23-input.txt'
#INPUT_FILE='23a-example.txt'

class Node(object):
    def __init__(self, val: int):
        self.val = val
        self.next = None

    def getVal(self):
        return self.val

    def setNext(self, next_node):
        self.next = next_node

    def __iter__(self):
        node = self
        while node is not None:
            yield node
            node = node.next

    def __next__(self):
        if self.next is None:
            raise StopIteration
        return self.next

    def __repr__(self):
        return str(self.val)

    def __eq__(self, other):
        if isinstance(other, int):
            return self.getVal() == other
        else:
            return self.getVal() == other.getVal()

input = [int(char) for line in get_file_contents(INPUT_FILE)[0] for char in line]

def play_cups(input: List[int], num_moves: int) -> Node:
    #input_size = b_size

    max_val = input[0]
    min_val = input[0]
    lookup = dict()
    first_node: Node = None
    last_node: Node = None
    for el in input:
        if el > max_val:
            max_val = el
        if el < min_val:
            min_val = el

        node = Node(el)
        lookup[el] = node

        if not first_node:
            first_node = node
        if last_node:
            last_node.setNext(node)
        last_node = node

    last_node.setNext(first_node)

    cur_node: Node = first_node
    for turn in range(num_moves):
        pick_up = list(islice(next(cur_node), 3))
        cur_node.setNext(next(pick_up[-1]))
        #print(pick_up, list(islice(cur_node, 9)))

        target = cur_node.getVal()
        while True:
            target -= 1
            if (target == min_val and min_val in pick_up) or (target not in lookup):
                target = max_val

            if target not in pick_up:
                target_node = lookup[target]
                #print('target', target, target_node)
                tmp_next_node = next(target_node)

                target_node.setNext(pick_up[0])
                pick_up[-1].setNext(tmp_next_node)

                cur_node = next(cur_node)
                break

    return lookup[1]

start_a = time()
node_1 = play_cups(input, 100)
print('part a: ', end='')
cur_node = next(node_1)
next_node = next(cur_node)
for i in range(8):
    print(cur_node, end='')
    cur_node = next(cur_node)
print()
print('part a timing:', time() - start_a)

print()

start_b = time()

# Fill the rest of the input starting from the last number used + 1 to 1,000,000
b_size = pow(10, 6)
new_list = input + [i for i in range(len(input) + 1, b_size+1)]
# Play 10,000,000 moves
node_1 = play_cups(new_list, pow(10, 7))
cur_node = next(node_1)
next_node = next(cur_node)
print('Part b:', cur_node, next_node, cur_node.getVal() * next_node.getVal())
print('Part b timing:', time() - start_b)
