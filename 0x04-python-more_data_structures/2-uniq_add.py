#!/usr/bin/python3

def uniq_add(my_list=[]):
    """uniq_add: adds all unique integers in a list
                 (only once for each integer).

    args:
        my_list

    Returns:
        sum of unique element
    """
    sum = 0
    for item in set(my_list):
        sum += item
    return (sum)
