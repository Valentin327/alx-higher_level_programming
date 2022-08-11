#!/usr/bin/python3
"""Base module"""

class Base:
    """Base of all other classes"""


    __nb_objects = 0


    def __init__(self, id=None):
        """Class constructor"""

        if type(id) != int and id is not None:
            raise TypeError("id must be an integer")
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
