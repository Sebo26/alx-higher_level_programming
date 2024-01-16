#!/usr/bin/python3
"""Makes class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Create class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Create attributes of the square"""
        super().__init__(id, x, y, size, size)

    def __str__(self):
        """Return a string stating values of square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
