# Day 13

## Performance
Part b was initially solved with brute force using increment of 41*971 = 39811.
Did not time the run but seem like it took >30 minutes

After refactor:
```bash
(advent2020) ➜  13 git:(master) ✗ time ./13.py 
12 13 156
Part a None
a timing:  2.4318695068359375e-05
starting at 100000135196725 with increment 451416929 and diff 41
Part b ts:  404517869995362
b timing:  12.15181827545166

overall timing: 12.151852130889893
./13.py  12.21s user 0.01s system 99% cpu 12.224 total
```
