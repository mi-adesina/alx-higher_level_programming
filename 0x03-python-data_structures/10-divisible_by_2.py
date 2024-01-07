#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """divisible_by_2: finds all multiples of 2 in a list.
    Args:
        my_list:

    Returns:
        a new list of bool
    """
    ret_list = []
    for i in my_list:
        if ((i % 2) == 0):
            ret_list.append(True)
        else:
            ret_list.append(False)
    return ret_list
