#!/usr/bin/python3
"""Print area"""


class Square:
    """Defines square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Private property getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Private property setter"""
        if (type(value) is not int):
            raise (TypeError('size must be an integer'))
        elif (value < 0):
            raise (ValueError('size must be >= 0'))
        else:
            self.__size = value

    @property
    def position(self):
        """Private position getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """Private position setter"""
        if (not isinstance(value, tuple) or len(value) != 2
                or all(isinstance(num, int) for num in value)
                or all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculate square of size"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
