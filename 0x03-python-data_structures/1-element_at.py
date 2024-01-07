#!/usr/bin/python3

def element_at(my_list, idx):
    """element_at: retrieves an element from a list like in C.

    Args:
        my_list:
        idx:

    Returns:
        the element at the index(idx), otherwise None.
    """
    if (idx >= (len(my_list)) or idx < 0):
        return None
    return my_list[idx]
