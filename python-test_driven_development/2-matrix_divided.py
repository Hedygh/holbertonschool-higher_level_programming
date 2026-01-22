#!/usr/bin/python3
"""This module provides a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Return a new matrix where each element is divided by div.

    The matrix must be a list of lists of integers or floats and each row
    must have the same size. The division result is rounded to 2 decimals.
    """
    MATRIX_ERR = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if (not isinstance(matrix, list) or matrix == [] or
            any(not isinstance(row, list) or row == [] for row in matrix)):
        raise TypeError(MATRIX_ERR)
    row_len = None
    for row in matrix:
        if row_len is None:
            row_len = len(row)
        elif len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if (not isinstance(item, (int, float)) or isinstance(item, bool)):
                raise TypeError(MATRIX_ERR)
    new_matrix = []
    for row in matrix:
        new_row = [round(item / div, 2) for item in row]
        new_matrix.append(new_row)
    return new_matrix
