#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for m in i:
            print("{:d}".format(matrix[i][j]), end= " ")
        print()
