#!/usr/bin/python3

def weight_average(my_list=[]):
    """weight_average: returns the weighted average of all integers tuple.

    Args:
        my_list:

    Returns:
        converted integer
    """
    if not my_list:
        return 0

    score = 0
    weight = 0
    for a, b in my_list:
        score += (a * b)
        weight += b
    return (score / weight)
