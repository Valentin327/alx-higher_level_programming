#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a = dict(a_dictionary)
    for key, value in sorted(a.items()):
        print("{}: {}".format(key, value))
