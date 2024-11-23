#!/usr/bin/python3
"""Module '0-rotate_2d_matrix.py' """


def rotate_2d_matrix(matrix):
    n = len(matrix)
    # reverse the array and transpose
    matrix.reverse()
    # loop thru each position and only swap values above the diagonal
    # to prevent duplicate swapping
    # swap [i][j] with [j][i]
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
