#!/usr/bin/python3
for n in range(0, 100):
    print("{:0>2}, ".format(n) if n < 99 else "{}".format(n), end='')
print()
