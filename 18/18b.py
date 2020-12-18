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

INPUT_FILE='18-input.txt'
#INPUT_FILE='18a-example.txt'
#INPUT_FILE='18b-example.txt'
#INPUT_FILE='18c-example.txt'
#INPUT_FILE='18d-example.txt'

num_match = re.compile(r'[\d]+')
input = [[bla for bla in line.split(' ') if bla] for line in get_file_contents(INPUT_FILE)[0]]

expr_result = []

def eval_expr(b):
    op = None
    result = 0
    stack = []
    take = True
    for i, a in enumerate(b):
        if op == '+':
            result += a
            op = None
            continue
        elif op == '*':
            result *= a
            op = None
            continue
        elif take:
            result = a
            take = False

        if a == '+':
            op = a
        elif a == '*':
            stack.append(result)
            take = True

    if stack:
        stack.append(result)
        result = reduce(mul, stack)
    return result

for expr in input:
    stack = [[]]
    for el in expr:
        parens_begin = 0
        afaf = ''
        for i, char in enumerate(el):
            if char == '(':
                parens_begin += 1
                stack.append([])
            elif char == ')':
                if (num_match.match(afaf)):
                    stack[-1].append(int(afaf))
                afaf = ''
                stack[-2].append(eval_expr(stack.pop()))
            else:
                afaf += char
        if (num_match.match(afaf)):
            stack[-1].append(int(afaf))
        else:
            stack[-1].append(afaf)

    expr_result.append(eval_expr(stack.pop()))

print(sum(expr_result))
