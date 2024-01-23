#!/usr/bin/python3
# Author: Michael Ifeoluwalose Adesina
def safe_print_list(my_list=[], x=0):
    """safe_print_list: prints x elements of a list.
    Args:
        my_list:
        :

    Returns:
        Returns the real number of elements printed
    """
    i = 0
    try:
        while i < x:
            print("{}".format(my_list[i]), end="")
            i += 1
    except IndexError:
        pass
    finally:
        print()
    return (i)
