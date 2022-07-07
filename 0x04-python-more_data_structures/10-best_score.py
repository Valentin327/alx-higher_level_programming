#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)
    max_s = 0
    for key, value in a_dictionary.items():
        if value > max_s:
            max_s = value
    for key, value in a_dictionary.items():
        if max_s == value:
            return (key)
