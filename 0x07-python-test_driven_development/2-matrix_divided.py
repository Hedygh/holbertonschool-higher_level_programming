#!/usr/bin/python3
""" Matrix division """


def matrix_divided(matrix, div):
    """ Divide all element of matrix

    Elements must be of type int or floats.

    """
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
            raise TypeError("Each row of the matrix must have the"
                            "same size")

    for row in matrix:
        if type(row) is not list or row == []:
            raise TypeError("matrix must be a matrix "
                            "(list of lists) of integers/floats")
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(i / div, 2) for i in row] for row in matrix]
