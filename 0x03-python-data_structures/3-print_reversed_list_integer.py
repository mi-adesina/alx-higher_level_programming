#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """print_reversed_list_integer:  prints all integers of a list,
                                     in reverse order.

    Args:
        my_list:

    Returns:
        None.
    """
    if isinstance(my_list, list):
        for integer in my_list[::-1]:
            print("{:d}".format(integer))
