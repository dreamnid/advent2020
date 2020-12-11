# Day 11

## Performance
```bash
(advent2020) ➜  11 git:(master) ✗ time ./11.py 
2183
1990
./11.py  6.58s user 0.00s system 99% cpu 6.585 total
```

Use json to deepcopy instead of copy.deepcopy
```bash
(advent2020) ➜  11 git:(master) ✗ time ./11.py 
2183
a timing:  1.8563430309295654
1990
b timing:  4.025422096252441

overall timing: 5.881777763366699
./11.py  5.89s user 0.01s system 99% cpu 5.904 total
```
