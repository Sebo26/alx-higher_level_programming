#!/usr/bin/python3
"""Empty class BaseGeometry"""


class BaseGeometry:
    """BaseGeometry representation"""
    pass

    def area(self):
        """Used when area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks what data type value is"""
        if value not in [int]:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
