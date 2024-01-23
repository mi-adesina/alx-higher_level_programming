#!/usr/bin/python3
# Author: Michael Ifeoluwalose Adesina
def safe_print_division(a, b):
    """safe_print_division: divides 2 integers and prints the result.
    Args:
        a:
        b:

    Returns:
        value of division or None
    """
    quotient = 0
    try:
        quotient = a / b
    except ZeroDivisionError:
        quotient = None
    finally:
        print("Inside result: {}".format(quotient))
    return quotient
