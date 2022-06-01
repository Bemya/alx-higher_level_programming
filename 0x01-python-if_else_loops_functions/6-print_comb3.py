#!/usr/bin/python3
for y in range(0, 9):
    for x in range(0, 10):
        if y == 8 and x == 9:
            print("{}{}".format(y, x))
        elif y < x:
            print("{}{}".format(y, x), end=', ')
