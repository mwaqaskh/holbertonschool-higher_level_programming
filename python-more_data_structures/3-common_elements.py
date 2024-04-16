#!/usr/bin/python3
def common_elements(set_1, set_2):
    c_set=set()
    for item in set_1:
        for item2 in set_2:
            if item == item2:
                c_set.add(item2)
    return c_set
