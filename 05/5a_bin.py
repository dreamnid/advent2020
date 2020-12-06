#!/usr/bin/env python3
import math

INPUT_FILE='5-input.txt'
#INPUT_FILE='5-example-1.txt'

# Inspired by others [esp. github user tckmn] who realized that
# the input is a binary string that needs to be converted to decimal
#
# Ref: https://github.com/tckmn/polyaoc-2020/blob/master/05/rb/05.rb
with open(INPUT_FILE) as fh:
    input = [line.strip() for line in fh]

claimed_seats = [int(line.translate(str.maketrans('FBLR', '0101')), 2) for line in input]
print(max(claimed_seats))

