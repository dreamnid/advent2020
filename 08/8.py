#!/usr/bin/env python3
from collections import defaultdict
from functools import partial, reduce
import math
import os
import re
from typing import Dict, List, Set, Tuple, Union

# Fix path so we can do a relative import: https://stackoverflow.com/a/27876800
if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

        # Relative imports here
        from util import *

INPUT_FILE='8-input.txt'
#INPUT_FILE='8a-example.txt'

def parse_value(value):
    num = int(value[1:])
    if value[0] == '+':
        return num
    else:
        return -num


program = get_file_contents(INPUT_FILE)[0]

def run(instructions: List[str]) -> Tuple[bool, int]:
    """
    Returns a tuple where:
      the first element indicates if the program terminated successfully and
      the second element contains the accumulator value
    :param instructions:
    :return:
    """
    ptr = 0
    early_return = False
    acc = 0
    seen = set()
    while True:
        if ptr in seen:
            # Already seen, terminate infinite loop
            early_return = True
            break
        seen.add(ptr)
        try:
            instr, value = instructions[ptr].split(' ')
        except IndexError:
            if ptr == len(program):
                # Reached the end of the program
                break
            print('out of bounds', ptr, len(instructions))
            break
        # print('instr', instr, value)
        if instr == 'nop':
            ptr += 1
            continue
        elif instr == 'acc':
            acc += parse_value(value)
            # print('acc', acc)
        elif instr == 'jmp':
            # print('old ptr', ptr)
            ptr += parse_value(value)
            # print('new ptr', ptr)
            continue
        else:
            print('Error - Unknown instr', instr)
            break

        ptr += 1
        if ptr >= len(program):
            break

    return not early_return, acc

def fix_program():
    indices = [i for i, x in enumerate(program) if x.split(' ')[0] in ('nop', 'jmp')]
    indices_idx = 0

    while True:
        modified_program = program.copy()
        # Bug is to replace one jmp->nop or nop->jmp instruction in the program so it will terminate normally
        try:
            line = modified_program[indices[indices_idx]].split(' ')
        except:
            print('Error', indices_idx, len(indices))
        if line[0] == 'nop' and line[1] != '+0':
            modified_program[indices[indices_idx]] = 'jmp {}'.format(line[1])
        else:
            modified_program[indices[indices_idx]] = 'nop {}'.format(line[1])
        #print(f'modified {program[indices[indices_idx]]}; {modified_program[indices[indices_idx]]}')

        res = run(modified_program)

        if res[0]:
            return res[1]

        indices_idx += 1
        if indices_idx >= len(indices):
            return None

print('a acc', run(program)[1])
print('b acc', fix_program())
