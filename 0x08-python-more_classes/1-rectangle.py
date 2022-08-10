#!/usr/bin/python3
"""Write a class that defines a rectangle"""


class Rectangle:
    """Instantiation with optional width and height"""
    def __init__(self, width=0, height=0):
        """Rectangle instance"""

        self._Rectangle__height = height
        self._Rectangle__width = width

    @property
    def height(self):
        """property for the
        rectangle
        raise:
            TypeError if the value of width
            is not an integer
            ValueError if the value
            is less than 0
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """setter for
        rectangle width
        property
        """
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        elif(value < 0):
            raise ValueError("width must be >= 0")
        self._Rectangle__height = value

    @property
    def width(self):
        """rectangle height
        property
        raise:
            typeError if the value of
            is not an integer
            ValueError if the value of
            height is less than 0
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """setter for
        rectangle height
        property
        """
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        elif(value < 0):
            raise ValueError("height must be >= 0")
        self._Rectangle__width = value
