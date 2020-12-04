#!/usr/bin/env python3
import re
import sys

if not (sys.version_info.major == 3  and  sys.version_info.minor >= 8):
    print("This script requires Python 3.8 or higher")
    sys.exit(1)

# Requires Python3.8

INPUT_FILE = '4-input.txt'
#INPUT_FILE = '4a-example.txt'

# Note that the input file needs to have a blank line at the end of the file

passports = []
result = 0

with open(INPUT_FILE) as fh:
    tmp = {}
    for line in fh:
        line = line.strip()

        if line != '':
            for i in line.split(' '):
                entry = i.split(':')
                tmp[entry[0]] = entry[1]
        else:
            req_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
            keys = set(tmp.keys())
            if len(keys.intersection(req_keys)) == len(req_keys):
                result += 1
            tmp = {}

print(f'Result: {result}')
