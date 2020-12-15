# Day 15

Main issue was things were getting "seen" too early, so need to delay
adding numbers to the seen dictionary by 1 iteration

## Performance
```bash
(advent2020) ➜  15 git:(master) ✗ time python 15.py
2020th number spoken: 376
a timing:  0.000469207763671875
30000000th number spoken: 323780
b timing:  11.452055215835571

overall timing: 11.452534675598145
python 15.py  11.64s user 0.28s system 99% cpu 11.940 total
```
