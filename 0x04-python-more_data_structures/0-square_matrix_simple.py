#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = []
    for item in matrix:
        temp = []
        for integer in item:
            temp.append(integer ** 2)
        matrix2.append(list(temp))
    return matrix2
