#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    w_a = 0.0
    numerator = list(t[0] * t[1] for t in my_list)
    denominator = list(t[1] for t in my_list)
    w_a = (sum(numerator) / sum(denominator))
    return (w_a)
