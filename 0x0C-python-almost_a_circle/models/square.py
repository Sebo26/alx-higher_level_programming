#!/usr/bin/python3
"""Makes class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Create class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Create attributes of the square"""
        super().__init__(id, x, y, size, size)

    @property
    def size(self):
        """Getter and setter for size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates attributes of class Rectangle"""
        if len(args) == 4:
            self.id, self.size self.x, self.y
            pass
        else:
            print("Arguments are not 5")

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        sqr_dictionary = {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
        return sqr_dictionary

    def __str__(self):
        """Return a string stating values of square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
