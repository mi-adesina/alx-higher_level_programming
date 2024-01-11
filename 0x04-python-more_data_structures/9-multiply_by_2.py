#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """multiply_by_2: returns a new dictionary with all values
                      multiplied by 2

    Args:
        a_dictionary:

    Returns:
        new dictionary
    """
    ret_dict = {}
    for key in a_dictionary:
        ret_dict[key] = a_dictionary[key] * 2
    return (ret_dict)
