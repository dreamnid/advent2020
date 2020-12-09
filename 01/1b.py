#!/usr/bin/env python3

from functools import reduce


# Fix path so we can do a relative import: https://stackoverflow.com/a/27876800
if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

        # Relative imports here
        from util import *

INPUT_FILE = '1-input.txt'

DESIRED_SUM = 2020

# Read file contents into number
# Assume that there is no entry of 0 and that there are at least 3 entries in the file
numbers = []
with open(INPUT_FILE) as fh:
    numbers = [int(line) for line in fh]

# Dedup numbers and throw out any numbers greater than DESIRED_SUM
input = sorted([number for number in set(numbers) if number <= DESIRED_SUM])

def find_3_parts_sum(input, desired_sum):
    # Deprecated - use find_var_parts_sum instead
    number = [0] * 3
    input_len = len(input)
    for idx_0 in range(input_len):
        number[0] = input[idx_0]
        for idx_1 in range(idx_0+1, input_len):
            number[1] = input[idx_1]
            for idx_2 in range(idx_1+1, input_len):
                number[2] = input[idx_2]
                cur_sum = sum(number)
                if cur_sum == desired_sum:
                    return number
                elif cur_sum > desired_sum:
                    # sum is too large, so can skip the rest since they will be larger
                    break

    # Didn't find a result
    return None



#result = find_3_parts_sum(input, DESIRED_SUM)
result = find_var_parts_sum(input, DESIRED_SUM, 3)

if result:
    print('Found!', '+'.join(map(str, result)), DESIRED_SUM)
    print('Product', '*'.join(map(str, result)), reduce(lambda a, b: a*b, result))
else:
    print('Not Found')