#!/usr/bin/python3
# Author: Michael Ifeoluwalose Adesina
def safe_print_integer(value):
    """safe_print_integer: prints an integer with "{:d}".format().
    Args:
        value:

    Returns:
        Boolean
    """
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError):
        ret_value = False
    else:
        ret_value = True
    return (ret_value)
