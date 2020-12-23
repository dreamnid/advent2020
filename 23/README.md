# Day 23
Part A - Spent too long trying to trace where I was going wrong. 
Realized I didn't need to format the list as shown as the example so didn't need to worry about moving things off the end of list to the beginning

## Performance
Part a
```bash
(advent2020) ➜  23 git:(master) ✗ time python3 23a.py
82635947
python3 23a.py  0.07s user 0.00s system 99% cpu 0.070 total
```

Part a refactored as linked list
```bash
(advent2020) ➜  23 git:(master) ✗ time python3 23b.py
82635947
python3 23b.py  0.06s user 0.01s system 99% cpu 0.069 total
```

23.py running for both part (a) and (b)
```bash
(advent2020) ➜  23 git:(master) ✗ time python 23.py
part a: 82635947
part a timing: 0.00023055076599121094

Part b: 470997 * 333437 = 157047826689
Part b timing: 24.703123092651367
python 23.py  27.51s user 0.07s system 99% cpu 27.597 total
```
