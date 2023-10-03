#!/usr/bin/python3
"""
This module defines a function that divides all elements of
a matrix
"""


def matrix_divided(matrix, div):
    """
    matrix_divided - divides all elements of a matrix

    Parameters
    __________
    matrix: a list of lists of integers and floats
    div: The divisor to divide the elements of matrix

    Returns
    _______
    A matrix with the original matrix elements
    divided by div

    """
    if not matrix or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists)of
                        integers / floats")
    len_1 = len(matrix[0])
    for item in matrix:
        if len(item) != len_1:
            raise TypeError("Each row of the matrix must
                            have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    try:
        result = []
        for list in matrix:
            res_tmp = []
            for x in list:
                res_tmp.append(round((x / div), 2))
            result.append(res_tmp)
    except Exception:
        raise TypeError("matrix must be a matrix (list of lists)of
                        integers / floats")
    return result
