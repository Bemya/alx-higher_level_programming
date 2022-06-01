#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    sum = 0
    if len(argv) == 1:
        sum = 0
    else:
        for n in range(1, len(argv)):
            sum = sum + int(argv[n])
    print("{:d}".format(sum))
