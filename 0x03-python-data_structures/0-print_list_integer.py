#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """print_list_integer: all integers of a list.

    Args:
        my_list

    Returns:
        None
    """
    for integer in my_list:
        print("{:d}".format(integer))
