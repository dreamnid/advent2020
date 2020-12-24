# Day 24
Had trouble figuring out coordinates system since in a regular cartesian grid, `nwwswee` would lead you one space left from the origin

To simplify logic, white is False, black is True. This lets us use `sum` which treats True as 1

### Part b
When doing part b, realized my coordinate system was not correct. Ended up looking up hexagonal coordinate implementations

### Future work
* Representing hexagonal coordinates as [complex numbers](https://www.reddit.com/r/adventofcode/comments/kja2qt/2020_day_24_complex_numbers_and_eval_ftw/)
* Checking out [other hexagon representations](https://www.redblobgames.com/grids/hexagons/#coordinates-offset)
* Come up with a visualization on the print_graph() output for each turn

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
part a timing: 0.003114938735961914

Initial grid
 w w w w w w B B B B w w B B B w B B w B w w w w w w w 
w w w w w w w w B B B B B B B B B B w B B w w w w w w 
 w w w w w B w w B B B B w w w w w B B B w w w w w w w 
w w w w w B w w B B w w B w w B B B w w w w w w w w w 
 w w w w B w B w B B B B w w w B B w w w B B w w w w w 
w w w w B B w B B B w w w B w w w B w B w B B w w w w 
 w w w B B B B w w B B w B B B w B B B B w w w w w w w 
w w w B w w B B B w B w B w B B B B B B B B B w w w w 
 w w w B w w B B w w B w w B B B B w B B B B w w w w w 
w w B w B B B B w w B B B B B w B w w w w w w B B w w 
 w w B w w B B w w B w B w w B w B w w B B w B w w w w 
w w w w w w w w B B B w B B w w B B B B B B B w B w w 
 w B B B B B B B B B w B w w B w B w w B B B B w w B w 
B w w w w B B w B w w w B z B B B B w w w B B w B B w 
 w B B w B w w B B B B w w B w w B w w B w B B w w B w 
w B w w B w w w B B B B w B w w B B B w w B w B w B w 
 w B B w w B B B B B B B w B w w B w w w B B B B B w w 
w w w B w w B w w B w B w B w B B w w B B w B B w w w 
 w w B B w w B w B w w w w B w w B w B B B B B B w w w 
w w w B w w w B B w w B w B B B B B w B B B B B w w w 
 w w w B B B B B w B B B w B B w B B B w B w B w w w w 
w w w w w B B w w B w w B B w w B w w B w w w w w w w 
 w w w w w w B w B B w B w w w w B w B B w w w w w w w 
w w w w w w w w w B w w w B B B w w w w B B w w w w w 
 w w w w w w B B B w w w B B w w B B w B w w w w w w w 
w w w w w w w w w w w w B B w B w w B w w w w w w w w 
 w w w w w w B B B w B B B B B w B w B B w w w w w w w 
================================================================================
*********
part b: 3466
part b timing 2.2052063941955566
python3 24.py  2.26s user 0.02s system 99% cpu 2.283 total
```
