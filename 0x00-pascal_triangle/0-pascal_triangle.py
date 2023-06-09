#!/usr/bin/python3
"""
Function returns pascal's triangle
"""


def pascal_triangle(n):
    """Function for pascal triangle"""
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):  # n is another array in triangle
        row = [1]  # every row begins with 1
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle
