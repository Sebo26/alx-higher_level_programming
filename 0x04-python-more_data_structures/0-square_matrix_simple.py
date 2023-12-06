#!/usr/bin/python
def square_matrix_simple(matrix=[]):
    map(sqr_root, matrix)
    def sqr_root(num):
        return num ** num
