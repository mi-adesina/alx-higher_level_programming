#!/usr/bin/python3

def best_score(a_dictionary):
    """best_score: returns a key with the biggest integer value.

    Args:
        a_dictionary:

    Returns:
        key with the biggest integer value.
    """
    ret_key = None
    ret_key_val = 0
    if (a_dictionary is None) or (len(a_dictionary) == 0):
        return ret_key
    for key in a_dictionary:
        if ret_key is None:
            ret_key_val = a_dictionary[key]
            ret_key = key
        elif ret_key_val < a_dictionary[key]:
            ret_key_val = a_dictionary[key]
            ret_key = key
    return (ret_key)
