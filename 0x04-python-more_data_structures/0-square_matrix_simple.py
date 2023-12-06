#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def sqr_root(num):
        return num ** 2
    result = list(map(lambda row: list(map(sqr_root, row)), matrix))
    return result
