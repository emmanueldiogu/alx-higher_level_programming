#!/usr/bin/python3
"""Print Squares
Print square with # character
"""


def print_square(size):
    """A function that prints square with # character

    Args:
        size (int): Length of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    
    for i in range(0, size):
        [print("#", end="") for k in range(0, size)]
        print("")
