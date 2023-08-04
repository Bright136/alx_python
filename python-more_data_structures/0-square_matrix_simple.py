# Write a function that computes the square value of all integers of a matrix.

# Prototype: def square_matrix_simple(matrix=[]):
# matrix is a 2 dimensional array
# Returns a new matrix:
# Same size as matrix
# Each value should be the square of the value of the input
# Initial matrix should not be modified
# You are not allowed to import any module
# You are allowed to use regular loops, map, etc.

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for arr in matrix:
        for i in range(len(arr)):
            arr[i] = arr[i] ** 2
        new_matrix.append(arr)
    return new_matrix
        


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# new_matrix = square_matrix_simple(matrix)
# print(new_matrix)
print(matrix)
# [[1, 4, 9], [16, 25, 36], [49, 64, 81]]