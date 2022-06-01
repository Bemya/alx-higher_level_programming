#!/usr/bin/python3
import hidden_4
if __name__ == '__main__':
    for n in range(len(dir(hidden_4))):
        if dir(hidden_4)[n][0:1] != '_':
            print(dir(hidden_4)[n])
