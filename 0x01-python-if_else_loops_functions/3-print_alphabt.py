#!/usr/bin/python3
for p in range(ord('a'), ord('z') + 1):
    if chr(p) != 'e' and chr(p) != 'q':
        print("{:c}".format(p), end='')
