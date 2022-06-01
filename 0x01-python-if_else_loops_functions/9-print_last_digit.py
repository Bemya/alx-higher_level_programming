#!/usr/bin/python3
def print_last_digit(number):
    last = number % 10
    if number < 0:
        last = 10 - last
    print("{}".format(last), end="")
    return last
