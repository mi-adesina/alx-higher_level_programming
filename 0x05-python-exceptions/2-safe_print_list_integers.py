#!/usr/bin/python3
# Author: Michael Ifeoluwalose Adesina
def safe_print_list_integers(my_list=[], x=0):
    """safe_print_list_integers: prints the first x elements
                                 of a list and only integers.
    Args:
        my_list:
        x:

    Returns:
        real number of integers printed
    """
    i = 0
    j = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            j += 1
        except (TypeError, ValueError):
            '''
            IndexError was ommited on purpose because
            it is requested by the project.
            '''
            pass
        i += 1
    print()
    return (j)
