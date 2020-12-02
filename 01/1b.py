#!/usr/bin/env python3

from functools import reduce
from typing import List, Union

INPUT_FILE = '1-input.txt'

DESIRED_SUM = 2020

# Read file contents into number
# Assume that there is no entry of 0 and that there are at least 3 entries in the file
numbers = []
with open(INPUT_FILE) as fh:
    numbers = [int(line) for line in fh]

# Dedup numbers and throw out any numbers greater than DESIRED_SUM
input = sorted([number for number in set(numbers) if number <= DESIRED_SUM])
input_len = len(input)
#print('input', input)
#print('input_len', input_len)


def find_3_parts_sum(input, desired_sum):
    # Deprecated - use find_var_parts_sum instead
    number = [0] * 3
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

def find_var_parts_sum(input_list: List[int], desired_sum: int, num_addends=3, addends=None, addend_idx=0) -> Union[List[int], None]:
    """
    Find the combination of numbers in the input_list that adds up to desired_sum

    :param input_list: The *sorted* list of available numbers
    :param desired_sum: The target sum that the addends should add to
    :param num_addends: The desired number of addends that should add up to desired_sum
    :param addends: private - buffer holding current result
    :param addend_idx: private - index of the addend list that is currently being worked on
    :return: The list of numbers that add up to the desired_sum or None if no solution found

    Note that this is a recursive call. Each recursion call works on the next addend hence why we pass
    the input_list without the first elemtn and 1 is added to addend_idx
    """
    if not addends:
        # Using None as initial value to help assert if I'm doing something dumb later
        addends = [None] * num_addends

    for input in input_list:
        addends[addend_idx] = input

        if addend_idx < num_addends-1:
            if sum(addends[:addend_idx]) > DESIRED_SUM:
                # sum is too large, so don't need to recurse again since the rest of the list is bigger
                return None
            temp_res = find_var_parts_sum(input_list[1:], desired_sum, num_addends=num_addends, addends=addends, addend_idx=addend_idx+1)
            if temp_res:
                return temp_res
        else:
            cur_sum = sum(addends)
            if cur_sum == desired_sum:
                return addends
            elif cur_sum > desired_sum:
                # sum is too large, so can skip the rest since they will be larger
                break

    if None not in addends and sum(addends) == desired_sum:
        return addends

    # Didn't find a result
    return None

#result = find_3_parts_sum(input, DESIRED_SUM)
result = find_var_parts_sum(input, DESIRED_SUM, 3)

if result:
    print('Found!', '+'.join(map(str, result)), DESIRED_SUM)
    print('Product', '*'.join(map(str, result)), reduce(lambda a, b: a*b, result))
else:
    print('Not Found')