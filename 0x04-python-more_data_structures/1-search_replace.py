#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """search_replace: replaces all occurrences of an element
                       by another in a new list.

    Args:
        my_list:
        search:
        replace:

    Returns:
        a new matrix
    """
    ret_list = my_list[:]
    for i in range(len(ret_list)):
        if ret_list[i] == search:
            ret_list[i] = replace
    return (ret_list)
