#!/usr/bin/python3

def no_c(my_string):
    """no_c: removes all characters c and C from a string.

    Args:
        my_string

    Returns:
        the new string
    """
    new_string = ""
    i = 0
    while (i < len(my_string)):
        if not ((my_string[i] == 'c') or (my_string[i] == 'C')):
            new_string += my_string[i]
        i += 1
    return new_string
