#!/usr/bin/python3
"""Area and Perimeter
Write a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)
"""


class Rectangle:
    """Defines a rectangle"""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get the current width of the square."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the current width of the square."""
        if not isinstance(value, int):
            raise TypeError("width must ne an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get the current height of the square."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the current height of the square."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """area of a rectangle
        area = width * height
        """
        area = self.width * self.height
        return area

    def perimeter(self):
        """perimeter of a rectangle
        perimeter = 2(width + height)
        """
        perimeter = 0
        if self.height == 0 or self.width == 0:
            return perimeter
        else:
            perimeter = 2 * (self.width + self.height)
        return perimeter
