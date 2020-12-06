#!/usr/bin/env python3
import math

from functools import reduce
from typing import List, Set

INPUT_FILE='6-input.txt'
INPUT_FILE='6-example.txt'


def any_agree(answers: List[Set[str]]) -> bool:
    # Return question(s) that received at least 1 yes from anyone in the group
    return set.union(*answers)

def all_must_agree(answers: List[Set[str]]) -> bool:
    # Return question(s) that received yes from everyone in the group
    return set.intersection(*answers)

def get_answers() -> List[Set[str]]:
    # Note that this depends on the file having an extra blank line at the end

    with open(INPUT_FILE) as fh:
        tmp = []
        for line in fh:
            line = line.strip()

            if line != '':
                line_chars = {char for char in line}
                tmp.append(line_chars)
            else:
                yield tmp
                tmp=[]



any_res = [len(any_agree(answers)) for answers in get_answers()]
print(f'Any yes Sum: {sum(any_res)}')
all_res = [len(all_must_agree(answers)) for answers in get_answers()]
print(f'All agreed Sum: {sum(all_res)}')
