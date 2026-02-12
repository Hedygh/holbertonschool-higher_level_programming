#!/usr/bin/python3
""" pascal triangle to n"""


def pascal_triangle(n):
    """ pascal triangle to n"""
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        row = []
        row.append(1)
        if i > 1:
            prev = triangle[i - 1]
            for j in range(1, i):
                row.append(prev[j - 1] + prev[j])
        if i > 0:
            row.append(1)
        triangle.append(row)
    return triangle
