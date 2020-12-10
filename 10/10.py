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
print('content', content)

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

def smart():
    content_rev = sorted(content, reverse=True)
    print(content_rev)
    seen = set()
    num_op = 0
    for i in range(len(content)):
        cur = content_rev[i]
        candidates = [j for j in content_rev[i+1:i+5] if cur - j < 4 and j not in seen]
        print('candidates', candidates, content_rev[i+1:i+4], seen, num_op)
        seen.update(candidates)

        num_op += max(len(candidates)-1, 0)
    print(num_op)
    
    return 2**num_op

seen = {}

def combinations2(idx=0, buffer=None):
    print('seen', seen, content[idx])
    if content[idx] in seen:
        print('early seen, returning', seen[content[idx]])
        return seen[content[idx]]
    total = 0
    if not buffer:
        buffer =[content[idx]]
    else:
        buffer.append(content[idx])
    while True:
        candidates = [num for num in content[idx+1:idx+4] if num - content[idx] < 4]
        print('idx', idx, 'content', content[idx], 'buffer', buffer, candidates)
        if len(candidates) == 1:
            cur = candidates[0]
            if cur in seen:
                return seen[cur]
            buffer.append(cur)
            #used.add(cur)

            if cur == device-3:
                print('finished')
                seen[content[idx]] = 1
                return total if total else 1
        elif len(candidates) == 0:
            #print('no candidates')
            return 0
        else:
            print('buffer', buffer, 'candi', candidates, '*************')
            rec = [combinations2(content.index(candidate, idx), buffer.copy()) for candidate in candidates]
            sum_rec = sum(rec)
            seen[content[idx]] = sum_rec

            total += sum_rec
            print('total', total, 'rec:', rec, 'seen', seen, '------------------')
            #print(hmm)
        idx += 1

        if idx > len(content):
            break
    print('return totla', total)
    return total
    
        


diff = use_all_adapters()
print(diff, diff[1] * diff[3])

print('Num combos: ', combinations2())

#            3  2      3  
#            3, 4      5  6   8    9   
# (0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)