# Day 24
Had trouble figuring out coordinates system since in a regular cartesian grid, `nwwswee` would lead you one space left from the origin

To simplify, white is False, black is True
--
When doing part b, realized my coordinate system was not correct. Ended up looking up hexagonal coordinate implementations

## Performance
Part a
```bash
(advent2020) ➜  24 git:(master) ✗ time python 24.py
300
python 24.py  0.06s user 0.02s system 99% cpu 0.077 total
```

Part a + b
```bash
(advent2020) ➜  24 git:(master) ✗ time python3 24.py 
part a: 300
part a timing: 0.0031075477600097656
================================================================================
part b: 3466
part b timing 2.2121362686157227
python3 24.py  2.29s user 0.00s system 99% cpu 2.290 total
```
