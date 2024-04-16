#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keysList = list(a_dictionary.keys())
    for key in sorted(keysList):
        print(key +":"+str(a_dictionary[key]))
    return keys_sorted
