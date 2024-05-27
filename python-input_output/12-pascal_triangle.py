#!/usr/bin/python3
"""This function returns a list of lists \
of integers representing the Pascal’s triangle"""


def pascal_triangle(n):
    """This function returns a list of lists \
    of integers representing the Pascal’s triangle"""
    if n <= 0:
        return []
    triangle_pascal = [[1]]

    for i in range(1, n):
        prev_cell = triangle_pascal[-1]
        new_cell = [1]

        for j in range(1, i):
            new_cell.append(prev_cell[j - 1] + prev_cell[j])

        new_cell.append(1)
        triangle_pascal.append(new_cell)

    return triangle_pascal
