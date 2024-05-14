#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    square = []
    for lines in matrix:
        new_line = []
        for value in lines:
            square_value = value **2
            new_line.append(square_value)
        square.append(new_line)
    return square
    