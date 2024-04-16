#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keysList = list(a_dictionary.keys())
    print('keysList',keysList)
    keys_sorted = keysList.sort()
    print('keys_sorted',keys_sorted)
    for key in keys_sorted:
        print("key :"+str(a_dictionary[key]))
    return keys_sorted
