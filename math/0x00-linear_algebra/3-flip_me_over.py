#!/usr/bin/env python3
"""matrix_transpose"""


def matrix_transpose(matrix):
    """Retunrs the transpose of a matrix"""
    transpose = []
    for i in range(len(matrix[0])):
        transpose.append([])
        for j in range(len(matrix)):
            (transpose[i]).append(matrix[j][i])
    return transpose
