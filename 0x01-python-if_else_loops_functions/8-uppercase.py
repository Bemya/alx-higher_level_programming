#!/usr/bin/python3
def uppercase(str):
    for n in range(0, len(str)):
        if ord(str[n]) >= 97 and ord(str[n]) <= 122:
            str_val = ord(str[n]) - 32
        else:
            str_val = ord(str[n])
        print("{:c}".format(str_val), end='')
    print()
