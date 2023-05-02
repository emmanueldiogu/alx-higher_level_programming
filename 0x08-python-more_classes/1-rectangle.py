#!/usr/bin/python3
"""Real definition of a rectangle
Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
"""


class Rectangle:
    """Defines a rectangle"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the current width of the square."""
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        """Set the current width of the square."""
        if not isinstance(value, int):
            raise TypeError("width must ne an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._Rectangle__width = value

    @property
    def height(self):
        """Get the current height of the square."""
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        """Set the current height of the square."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._Rectangle__height = value
