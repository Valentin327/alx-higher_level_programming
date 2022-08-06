#!/usr/bin/python3
"""Define a class Square with size"""


class Square:
    """class private instance attribute"""
    def __init__(self, size=0):
        """Square instance"""

        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self._Square__size = size
