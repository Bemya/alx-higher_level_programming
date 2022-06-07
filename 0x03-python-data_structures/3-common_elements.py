#!/usr/bin/python3
def common_elements(set_1, set_2):
    common = []
    [common.append(ch) if ch in set_2 else ch for ch in set_1]
    return common
