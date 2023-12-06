#!/usr/bin/python
def square_matrix_simple(matrix=[]):
    result = []
    for row in matrix:
        new_row = [elem ** 2 for elem in row]
        result.append(new_row)
    print(result)
