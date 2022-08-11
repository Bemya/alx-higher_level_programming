#!/usr/bin/python3
""" some rectangle """


class Rectangle:
    """ class of rectangle the defines a rectangle """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @height.setter
    def height(self, value):
        if not(isinstance(value, int)):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @width.setter
    def width(self, value):
        if not(isinstance(value, int)):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if 0 in [self.__height, self.__width]:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        rstr = ""
        if 0 in [self.__width, self.__height]:
            return rstr
        for n in range(self.__height):
            for _ in range(self.__width):
                rstr += "#"
            if n != self.__height - 1:
                rstr += "\n"
        return rstr
