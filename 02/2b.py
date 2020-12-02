#!/usr/bin/env python3

INPUT_FILE = '2-input.txt'

valid = 0

with open(INPUT_FILE) as fh:
    for line in fh:
        # E.g. 2-3 a: bbacda
        # Format of each line
        # valid_char_pos required_character: password
        # Note that char_pos is 1-indexed
        line_parts = line.split(' ')
        char_pos = list(map(int, line_parts[0].split('-')))
        char = line_parts[1][0]
        password = line_parts[2]

        # Check if the char in specified pos matches 
        res = [password[cur_pos-1] == char for cur_pos in char_pos if cur_pos < len(password)]
        #print(char, char_pos, password, res.count(True))

        # Note that the character can't be in both positions!
        if sum(res) == 1:
           valid += 1

print("Number of valid passwords", valid)
