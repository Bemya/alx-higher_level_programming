#!/usr/bin/python3
""" some rectangle """


class Rectangle:
    """ class of rectangle the defines a rectangle """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def height(self):
        ''' property height'''
        return self.__height

    @property
    def width(self):
        ''' property width '''
        return self.__width

    @height.setter
    def height(self, value):
        ''' height setter '''
        if not(isinstance(value, int)):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @width.setter
    def width(self, value):
        ''' width setter '''
        if not(isinstance(value, int)):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
