# Day 17
Example for 17a was evil since cycle 2 used a different reference point from cycle 1. The author was trying to save space by not printing empty rows/column. That meant that "the center cell in the original grid is the top center cell in the updated grid" (https://www.reddit.com/r/adventofcode/comments/ker0wi/2020_day_17_part_1_sample_input_wrong/gg44r6o?utm_source=share&utm_medium=web2x&context=3)

Sounds like he added this blurb later to help: (and the frame of view follows the active cells in each cycle)

Once you understood that the example view was shrunk to show a segment with active cells, it become clear that the grid doesn't have borders/fixed dimensions which helps explain why the graph can grow on each cycle.

TODO: Remove extra outer buffer that are all zeros at the end of the loop since they will be deadweight and we're always adding a buffer at the start of the loop

## Performance
Part a
```bash
(advent2020) ➜  17 git:(master) ✗ time python3 17a.py 
368
python3 17a.py  0.25s user 0.01s system 99% cpu 0.258 total
```

Part b
```bash
(advent2020) ➜  17 git:(master) ✗ time python3 17b.py

Cycle 1

Cycle 2

Cycle 3

Cycle 4

Cycle 5

Cycle 6
2696
python3 17b.py  9.40s user 0.01s system 99% cpu 9.411 total
```
