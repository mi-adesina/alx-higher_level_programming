#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """replace_in_list: replaces an element of a list
                        at a specific position (like in C).

    Args:
        my_list:
        idx:
        element:

    Returns:
        the element at the index(idx), otherwise None.
    """
    if (idx >= (len(my_list)) or idx < 0):
        return my_list
    my_list[idx] = element
    return my_list
