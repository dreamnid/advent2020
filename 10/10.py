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
#INPUT_FILE='10a-example.txt'
#INPUT_FILE='10b-example.txt'

content = sorted([int(num) for num in get_file_contents(INPUT_FILE)[0]])
# Need to start with the outlet
content.insert(0, 0)

device = max(content) + 3
content.append(device)


def use_all_adapters():
    """
    Count the diff in jolts between the adapters

    :return: an array that contains the count where the index is the difference in jolts
    """
    diff = [0] * 4
    used = set()

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


def combinations1(idx=0, buffer=None, seen=None):
    if seen is None:
        seen = {}

    #print('seen', seen, content[idx])
    if content[idx] in seen:
        #print('early seen, returning', seen[content[idx]])
        return seen[content[idx]]

    if not buffer:
        buffer = [content[idx]]
    else:
        buffer.append(content[idx])
    while True:
        candidates = [num for num in content[idx+1:idx+4] if num - content[idx] < 4]
        #print('idx', idx, 'content', content[idx], 'buffer', buffer, candidates)
        if len(candidates) == 1:
            cur = candidates[0]
            if cur in seen:
                return seen[cur]
            buffer.append(cur)

            if cur == device:
                seen[content[idx]] = 1
                return 1
        elif len(candidates) == 0:
            print('no candidates')
            return 0
        else:
            #print('buffer', buffer, 'candi', candidates, '---------------------')
            rec = [combinations1(content.index(candidate, idx), buffer.copy(), seen) for candidate in candidates]
            sum_rec = sum(rec)
            seen[content[idx]] = sum_rec
            #print('total', total, 'rec:', rec, 'seen', seen, '*********************************')
            return sum_rec
        idx += 1

        if idx > len(content):
            break

diff = use_all_adapters()
print(diff, diff[1] * diff[3])

print('Num combos: ', combinations1())
