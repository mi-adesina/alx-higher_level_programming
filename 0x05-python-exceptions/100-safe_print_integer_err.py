#!/usr/bin/python3
# Author: Michael Ifeoluwalose Adesina
import sys


def safe_print_integer_err(value):
    """safe_print_integer_err: prints an integer.

    Args:
        Value: Integer to be printed.

    Returns:
        Nothing
    """
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        ret_value = False
    else:
        ret_value = True
    return ret_value
