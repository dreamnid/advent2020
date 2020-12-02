#!/usr/bin/env python3

INPUT_FILE = '2-input.txt'

valid = 0
with open(INPUT_FILE) as fh:
    for line in fh:
        # E.g. 2-3 a: bbacda
        # Format of each line
        # char_limits inclusive required_character: password

        line_parts = line.split(' ')
        char_limits = list(map(int, line_parts[0].split('-')))
        char = line_parts[1][0]

        char_count = line_parts[2].count(char)
        if char_limits[0] <= char_count <= char_limits[1]:
            valid += 1

print("Number of valid passwords", valid)
