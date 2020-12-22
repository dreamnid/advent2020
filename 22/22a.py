#!/usr/bin/env python3
from collections import defaultdict
from functools import partial, reduce
import math
from operator import mul
import os
import pprint
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

INPUT_FILE='22-input.txt'
#INPUT_FILE='22a-example.txt'

player_1 = [int(line) for line in get_file_contents(INPUT_FILE)[0][1:]]
player_2 = [int(line) for line in get_file_contents(INPUT_FILE)[1][1:]]

#pprint.pprint(player_1)
#pprint.pprint(player_2)

round = 1
while True:
    player_1
    card_1 = player_1.pop(0)
    card_2 = player_2.pop(0)

    if card_1 > card_2:
        player_1.append(card_1)
        player_1.append(card_2)
    else:
        player_2.append(card_2)
        player_2.append(card_1)

    if not player_1 or not player_2:
        break

    round += 1

if player_1:
    res = player_1
else:
    res = player_2

result = sum([card * (len(res)-idx) for idx, card in enumerate(res)])
print(result)


