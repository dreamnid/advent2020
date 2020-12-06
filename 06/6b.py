#!/usr/bin/env python3
from typing import List, Set

# Fix path so we can do a relative import: https://stackoverflow.com/a/27876800
if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

        # Relative imports here
        from util import *

INPUT_FILE='6-input.txt'
#INPUT_FILE='6-example.txt'

def any_agree(answers: List[Set[str]]) -> bool:
    # Return question(s) that received at least 1 yes from anyone in the group
#    print(answers)
    return set.union(*answers)

def all_must_agree(answers: List[Set[str]]) -> bool:
    # Return question(s) that received yes from everyone in the group
    return set.intersection(*answers)

# For each group, collect answers a list of set where each set contains the answer from each person
# e.g. [{a, b, c}, {a}]
forms = list(map(lambda x: [set(i) for i in x], get_file_contents(INPUT_FILE)))

#print(forms)
any_res = [len(any_agree(form)) for form in forms]
print(f'Any yes Sum: {sum(any_res)}')
all_res = [len(all_must_agree(form)) for form in forms]
print(f'All agreed Sum: {sum(all_res)}')
