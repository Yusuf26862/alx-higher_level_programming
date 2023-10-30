#!/usr/bin/python3
"""
Define a Rectangle class
"""


class Rectangle:
    """Rectangle class defined by width and height."""

    def __init___(self, width=0, height=0):
        """Initializes Rectangle instance in contructor."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of a Rectangle instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a Rectangle instance
        Args:
            value: valuse of the width, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of a Rectangle instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of a Rectangle instance
        Args:
            value: value of the height, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("heigh must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of a rectangle instance
        Returns:
            Area of the rectangle, given by height * width
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the area of a rectangle instance
        Returns:
            Perimeter of the rectangle, given by 2 * (height + width)
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
