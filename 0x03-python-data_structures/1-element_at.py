#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return (None)
    num = len(my_list)
    if idx > num:
        return (None)
    for i in range(0, num + 1):
        if my_list[i] == idx:
            return (my_list[i])
