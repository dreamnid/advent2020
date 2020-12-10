#!/usr/bin/env python3
from collections import defaultdict
from functools import partial, reduce
import math
import os
import re
from typing import Dict, List, Set, Union

# Fix path so we can do a relative import: https://stackoverflow.com/a/27876800
if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

        # Relative imports here
        from util import *

INPUT_FILE='10-input.txt'
INPUT_FILE='10a-example.txt'
#INPUT_FILE='10b-example.txt'

content = sorted([int(num) for num in get_file_contents(INPUT_FILE)[0]])
used = set()

device = max(content) + 3

def use_all_adapters():
    diff = [0] * 4

    cur = 0
    while True:
        candidates = [num for num in content if num not in used and num - cur < 4]
        diff[candidates[0]-cur] += 1
        cur = candidates[0]
        used.add(cur)

        if len(content) == len(used):
            diff[3] += 1
            break
    return diff

def combinations(cur=0, buf=None, used=None, remaining=None, seen=None, idx=0):
    if buf is None:
        buf = []
    else:
        buf.append(cur)
        buf = sorted(buf)

    if used is None:
        used = set()
    else:
        used.add(cur)

    if remaining is None:
        remaining = content

    #print('top of call', cur, buf, used)
    if seen is None:
        seen = []

    while True:

        candidates = [num for num in content[idx:] if num not in used and num - cur < 4]
        if len(candidates) == 1:
            cur = candidates[0]
            buf.append(cur)
            used.add(cur)

            if cur == device-3:
                if set(buf) not in seen:
                    print('found', cur, buf, used)
                    seen.append(buf)

                    return 1
                return 0
        elif len(candidates) == 0:
            #print('no candidates')
            return 0
        else:
            #print('candi', candidates)
            return sum([combinations(candidate, buf.copy(), used.copy(), [], seen, idx+1) for candidate in candidates])
            #print(hmm)
        idx += 1


diff = use_all_adapters()
print(diff, diff[1] * diff[3])

print('Num combos: ', combinations())


