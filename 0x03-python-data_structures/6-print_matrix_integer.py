#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """print_matrix_integer: prints a matrix of integers.

    Args:
        matrix:

    Returns:
        None.
    """
    for row in matrix:
        for integer in row:
            if not (integer == row[len(row) - 1]):
                print("{:d}".format(integer), end=" ")
            else:
                print("{:d}".format(integer), end="")
        print("".format())
