#!/usr/bin/python3
"""Print area"""


class Square:
    """Defines the area of a square"""

    def __init__(self, size=0):
        if (type(size) is not int):
            raise (TypeError('size must be an integer'))
        elif (size < 0):
            raise (ValueError('size must be >= 0'))
        else:
            self.__size = size

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
        if self.__size > 0:
            for i in range(self.__size):
                print('#' * self.__size)
        else:
            print()
