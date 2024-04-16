#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys_unsorted = list(a_dictionary.keys())
    keys_sorted = keys_unsorted.sort()
    for key in keys_sorted:
        print("key :"+str(a_dictionary[key]))
    return keys_sorted
