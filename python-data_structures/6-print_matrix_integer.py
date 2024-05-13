#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    if not matrix:
        return
    
    for lignes in matrix:
        for item in lignes:
            print("{:d}".format(item), end='')
            if lignes[-1] != item:
                print(" ", end='')
        print()
