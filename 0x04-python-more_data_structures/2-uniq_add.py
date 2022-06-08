#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = []
    [uniq.append(n) if n not in uniq else n for n in my_list]
    return sum(uniq)
