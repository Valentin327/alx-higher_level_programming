#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range(1, 6):
        idx = -1 * i
        print("{:d}".format(my_list[idx]))
