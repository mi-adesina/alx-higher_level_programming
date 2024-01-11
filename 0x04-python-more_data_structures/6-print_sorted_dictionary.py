#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """print_sorted_dictionary: prints a dictionary by ordered keys.

    Args:
        a_dictionary

    Returns:
        nothing
    """
    key_list = list(a_dictionary.keys())
    key_list.sort()
    for key in key_list:
        print("{}: {}".format(key, a_dictionary[key]))
