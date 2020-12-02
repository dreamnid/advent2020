INPUT_FILE = '1-input.txt'

DESIRED_SUM = 2020

# The 2 numbers whose sum adds up to DESIRED_SUM
PART_0 = None
PART_1 = None

numbers = []
with open(INPUT_FILE) as fh:
    numbers = [int(line) for line in fh]

# Dedup numbers and throw out any numbers greater than DESIRED_SUM
numbers = sorted([number for number in set(numbers) if number <= DESIRED_SUM])

# Straight forward algo: Iterate through list, check if DESIRED_SUM - current exist in the numbers list
for number in numbers:
    if DESIRED_SUM - number in numbers:
        PART_0 = number
        PART_1 = DESIRED_SUM - number
        break

if PART_0:
    print('Found!', PART_0, '+', PART_1, DESIRED_SUM)
    print('Product', PART_0, '*', PART_1, PART_0 * PART_1)
else:
    print('Not Found')