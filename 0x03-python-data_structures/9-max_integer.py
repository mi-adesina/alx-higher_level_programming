#!/usr/bin/python3

def max_integer(my_list=[]):
    """max_integer: finds the biggest integer of a list.

    Args:
        my_list:

    Returns:
        the biggest number in the list.
    """
    if (len(my_list) == 0):
        return None
    elif (len(my_list) == 1):
        return my_list[0]
    else:
        num = my_list[0]
        for i in my_list:
            if i > num:
                num = i
        return num
