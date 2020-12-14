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

After starting time at 0 instead of 100000000000000:
```bash
(advent2020) ➜  13 git:(master) ✗ time ./13.py 
12 13 156
Part a None
a timing:  2.5510787963867188e-05
starting at 0 with increment 451416929 and diff 41
Part b ts:  404517869995362
b timing:  0.3642556667327881

overall timing: 0.3642904758453369
./13.py  0.43s user 0.01s system 99% cpu 0.438 total
```
