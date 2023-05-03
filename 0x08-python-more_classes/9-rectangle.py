#!/usr/bin/python3
"""Define a Rectangle class"""


class Rectangle:
    """Represent a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new instance of the rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Compute the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Compute the perimeter of the rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return a string representation of the rectangle"""
        if not self.width or not self.height:
            return ""
        return "\n".join([str(self.print_symbol) * self.width] * self.height)

    def __repr__(self):
        """Return a string representation of the rectangle for recreation"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print a message when rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            return TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            return TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() > rect_2.area():
                return rect_1
            elif rect_2.area() > rect_1.area():
                return rect_2
            else:
                return rect_1

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
