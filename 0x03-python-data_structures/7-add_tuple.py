#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """add_tuple: adds 2 tuples.

    Args:
        tuple_a=():
        tuple_b=():

    Returns:
        addition of tuples
    """
    def to_pair(tup=()):
        if len(tup) == 0:
            tup = 0, 0
        elif len(tup) == 1:
            tup = tup[0], 0
        return tup

    tuple_a = to_pair(tuple_a)
    tuple_b = to_pair(tuple_b)
    tuple_c = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]

    return tuple_c
