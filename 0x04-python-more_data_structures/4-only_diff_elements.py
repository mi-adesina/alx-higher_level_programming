#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """only_diff_elements: returns a set of all elements present
                           in only one set.

    Args:
        set_1:
        set_2:

    Returns:
        set of all elements present in only one set.
    """
    return (set_1 ^ set_2)
