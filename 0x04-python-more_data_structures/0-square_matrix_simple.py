#!/usr/bin/python
def square_matrix_simple(matrix=[]):
    for row in matrix:
        for elem in row:
            return row * elem
    print(map(square_matrix_simple, elem))
