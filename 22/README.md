# Day 22

Was stuck on part b for 2 reasons.
1. Forgot to make a copy of the player cards before recursing
2. Didn't realize the copy was a subset whose size is the card you pulled. 
     Was passing the remaining cards.

## Performance
Part a
```bash
(advent2020) ➜  22 git:(master) ✗ time python3 22a.py
32272
python3 22a.py  0.09s user 0.02s system 61% cpu 0.176 total
```

Part b
```bash
(advent2020) ➜  22 git:(master) ✗ time python3 22b.py
33206
python3 22b.py  7.34s user 0.07s system 95% cpu 7.776 total
```
