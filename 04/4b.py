#!/usr/bin/env python3
import re
import sys

if not (sys.version_info.major == 3  and  sys.version_info.minor >= 8):
    print("This script requires Python 3.8 or higher")
    sys.exit(1)

# Requires Python3.8

INPUT_FILE = '4-input.txt'
#INPUT_FILE = '4a-example.txt'
#INPUT_FILE = '4b-example.txt'

# Note that the input file needs to have a blank line at the end of the file

passports = []
result = 0

def height_checker(x: str) -> bool:
    unit = x[-2:]
    if unit not in ['in', 'cm']:
        return False

    try:
        measure = int(x[:-2])
    except ValueError:
        print(f'{x} is not valid number')
        return False
    if unit == 'in':
        return 59 <= measure <= 76
    return 150 <= measure <= 193

validators = {
    'byr': lambda x: (x_int := int(x), 1920 <= x_int <= 2002)[1],
    'iyr': lambda x: (x_int := int(x), 2010 <= x_int <= 2020)[1],
    'eyr': lambda x: (x_int := int(x), 2020 <= x_int <= 2030)[1],
    'hgt': height_checker,
    'hcl': lambda x: re.match(r'#[0-9,a-f]{6}', x),
    'ecl': lambda x: x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
    'pid': lambda x: re.match(r'\d{9}$', x),
}

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
                for key, value in tmp.items():
                    valid = bool(validators.get(key, lambda x: True)(value))
                    if not valid:
                        break

                if valid:
                    result += 1
            tmp = {}

print(f'Result: {result}')
