#!/usr/bin/python3
"""Define Rectangle which inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Create class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Create the private instance attributes and getters/setters"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Return getter and sets properties for width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Return getter and sets properties for height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Return getter and sets properties for x"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Return getter and sets properties for y"""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Returns area of a rectangle"""
        return self.width * self.height

    def display(self):
        """Prints the rectangle according to height and width, made of '#'"""
        for m in range(self.y):
            print()

        for i in range(self.height):
            for n in range(self.x):
                print(" ", end='')
            for j in range(self.width):
                print('#', end='')
            print()

    def update(self, *args, **kwargs):
        """Updates attributes of class Rectangle"""
        if len(args) == 5:
            self.id, self.width, self.height, self.x, self.y
            pass
        else:
            print("Arguments are not 5")

    def __str__(self):
        """Return a string stating values of rectangles"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                self.width, self.height)
