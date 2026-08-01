#!/usr/bin/python3
"""Module that divides all elements of a matrix by a given divisor."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div, rounded to 2 decimals.

    Raises TypeError if matrix isn't a list of lists of int/float,
    if rows have different sizes, or if div isn't a number.
    Raises ZeroDivisionError if div is 0.
    """
    err_matrix = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(err_matrix)
    for row in matrix:
        if type(row) is not list or len(row) == 0:
            raise TypeError(err_matrix)
        for value in row:
            if type(value) is not int and type(value) is not float:
                raise TypeError(err_matrix)
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(value / div, 2) for value in row] for row in matrix]
