#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """square_matrix_simple: computes the square value of all integers
                           of a matrix.

    Args:
        matrix

    Returns:
        a new matrix
    """
    return ([list(map(lambda x: x * x, row)) for row in matrix])
