#!/usr/bin/python3
for n in range(97, 123)[::-1]:
    last_num = n % 10
    if last_num % 2 == 0:
        print("{:c}".format(n), end='')
    else:
        print("{:c}".format(n - 32), end='')
