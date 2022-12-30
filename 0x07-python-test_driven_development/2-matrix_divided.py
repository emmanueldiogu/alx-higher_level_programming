#!/usr/bin/python3
"""divides all elements of a matrix
All elements of the matrix should be delived by div,
rounded to 2 decimal places and
return a new matrix
"""

arr1 = [
    [1, 2, 3],
    [4, 5, 1],
    [4, "5", 1],
    [4, 5, 1],
]


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix

    Args:
        matrix (list): matrix must be a list of integers or floats
        div (int, float): number (int or float)
    """
    sizeofmat = len(matrix[0])
    for i in range(len(matrix)):
        if (sizeofmat != len(matrix[i])):
            raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    for row in matrix:
        for col in row:
            if type(col) not in [int, float]:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")


matrix_divided(arr1, 3)
