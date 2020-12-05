#!/usr/bin/env python3
import math

INPUT_FILE='5-input.txt'
def get_seat_id(row: int, col:int) -> int:
    return row * 8 + col

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

seat_ids = set()
for line in input:
    row, col = get_seat(line)
    seat_ids.add(row * 8 + col)

# Find the missing seat
# First few rows will be missing so need to skip
first_valid_seat_found = False
found = False
for row in range(128):
    for col in range(8):
        seat_id = get_seat_id(row, col)
        if get_seat_id(row, col) not in seat_ids:
            if first_valid_seat_found:
                print(f'[{row}, {col}]: {seat_id}')
                found = True
                break
        else:
            first_valid_seat_found = True
            pass
    if found:
        break


