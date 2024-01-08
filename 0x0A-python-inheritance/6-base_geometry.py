#!/usr/bin/python3
"""Empty class BaseGeometry"""


class BaseGeometry:
    """BaseGeometry representation"""
    pass

    def area(self):
        """Used when area is not implemented"""
        raise Exception("area() is not implemented")
