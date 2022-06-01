#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    if len(argv) == 1:
        strend = "arguments."
    elif len(argv) == 2:
        strend = "argument:"
    else:
        strend = "arguments:"
    print("{} {}".format(len(argv) - 1, strend))
    for n in range(1, len(argv)):
        print("{:d}: {:s}".format(n, argv[n]))
