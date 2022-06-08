#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new_v = {key: value}
    a_dictionary.update(new_v)
    return a_dictionary
