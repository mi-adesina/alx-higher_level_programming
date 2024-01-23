#!/usr/bin/python3
# Author: Michael Ifeoluwalose Adesina
import sys


def safe_function(fct, *args):
    """safe_function: executes a function safely.

    Args:
        fct:
        args:

    Returns:
        on success: the result of the function
        on  failure: None
    """
    try:
        output = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        output = None
    return output
