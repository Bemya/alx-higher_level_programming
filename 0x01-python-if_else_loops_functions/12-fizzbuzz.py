#!/usr/bin/python3
def fizzbuzz():
    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0:
            fb = 'FizzBuzz'
        elif n % 3 == 0:
            fb = 'Fizz'
        elif n % 5 == 0:
            fb = 'Buzz'
        else:
            fb = n
        print("{}".format(fb), end=' ')
