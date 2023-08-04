#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    new_list= []
    for arr in matrix:
        new_list = [arr[i] ** 2 for i in range(len(arr)) ]
        new_matrix.append(new_list)
    return new_matrix


        


