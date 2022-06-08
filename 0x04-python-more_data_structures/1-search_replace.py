#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [replace if ch == search else ch for ch in my_list]
    return new_list
