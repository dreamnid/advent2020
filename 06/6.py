#!/usr/bin/env python3
import math

from functools import reduce
from typing import List, Set

INPUT_FILE='6-input.txt'
INPUT_FILE='6-example.txt'

def get_any_yes() -> Set[str]:
    # Note that this depends on the file having an extra blank line at the end

    with open(INPUT_FILE) as fh:
        tmp = set()
        for line in fh:
            line = line.strip()

            if line != '':
                line_chars = {char for char in line}
                tmp.update(line_chars)
            else:
                yield tmp
                tmp=set()


def get_all_yes() -> Set[str]:
    # Note that this depends on the file having an extra blank line at the end

    with open(INPUT_FILE) as fh:
        first_person_in_group = True
        tmp = set()
        for line in fh:
            line = line.strip()

            if line != '':
                line_chars = {char for char in line}
                if first_person_in_group:
                    tmp = line_chars
                    first_person_in_group = False
                else:
                    tmp = tmp.intersection(line_chars)

            else:
                yield tmp
                tmp=set()
                first_person_in_group = True


any_res = [len(yes) for yes in get_any_yes()]
all_res = [len(yes) for yes in get_all_yes()]
print(f'Any yes Sum: {sum(any_res)}')
print(f'All agreed Sum: {sum(all_res)}')
