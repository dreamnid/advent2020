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
1990
./11.py  6.01s user 0.00s system 99% cpu 6.013 total
```