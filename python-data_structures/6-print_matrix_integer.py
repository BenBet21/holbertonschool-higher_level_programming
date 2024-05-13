#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for lignes in matrix:
        for item in lignes:
            print("{:d}".format(item), end='')
        print()
