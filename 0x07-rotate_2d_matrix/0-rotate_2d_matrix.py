#!/usr/bin/python3
"""
Rotate 2D Matrix Interview question
"""


def rotate_2d_matrix(matrix):
    """rotating a 2d matrix in place"""
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(len(matrix)):
        matrix[i].reverse()


"""
slice notation method
def rotate_2d_matrix(matrix):
    matrix[:] = zip(*matrix[::-1])

"""
