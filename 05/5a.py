#!/usr/bin/env python3
import math

INPUT_FILE='5-input.txt'
#INPUT_FILE='5-example-1.txt'

with open(INPUT_FILE) as fh:
    input = [line.strip() for line in fh]

def get_seat(line):
    row = [0, 127]
    col = [0, 7]
    for char in line:
        if char == 'F':
            # Seat is in lower half
            row[1] = row[0] + math.floor((row[1] - row[0]) / 2)
        elif char == 'B':
            row[0] = row[0] + math.ceil((row[1] - row[0]) / 2)
        elif char == 'L':
            # Seat is in the lower half
            col[1] = col[0] + math.floor((col[1] - col[0]) / 2)
        elif char == 'R':
            col[0] = col[0] + math.ceil((col[1] - col[0]) / 2)

    return row[0], col[0]


max_seat_id = 0
for line in input:
    row, col = get_seat(line)
    seat_id = row * 8 + col
    if seat_id == 935:
        print(row, col)

    max_seat_id = max((seat_id, max_seat_id))

print(max_seat_id)

