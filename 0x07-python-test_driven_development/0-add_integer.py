#!/usr/bin/python3
"""Function that adds 2 integers
A function that adds 2 integers or float
but returns an integer.
Returns TypeError for non integer or float values
"""


def add_integer(a, b=98):
    """function that adds 2 integers

    Args:
        a (int, float): first number
        b (int, optional): second number. Defaults to 98.

    Raises:
        TypeError: a must be an integer
        TypeError: b must be an integer

    Returns:
        int: returns the result of a + b
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
