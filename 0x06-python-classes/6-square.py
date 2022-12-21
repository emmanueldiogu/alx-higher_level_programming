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
        if (type(size) is not int):
            raise (TypeError('size must be an integer'))
        elif (size < 0):
            raise (ValueError('size must be >= 0'))
        else:
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

    def area(self):
        """Calculate square of size"""
        return self.__size ** 2

    def my_print(self):
        """Print square matrix"""
        if self.__size > 0:
            for blank in range(self.position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.position[0], end='')
                print("#" * self.__size)
        else:
            print()

    @property
    def position(self):
        """Private position getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """Private position setter"""
        if (len(value) != 2) or (type(value) is not tuple) \
                or (type(value[0]) is not int) \
                or (type(value[1]) is not int) \
                or (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
