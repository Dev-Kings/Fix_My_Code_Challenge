#!/usr/bin/python3
""" Module for Square class """


class Square():

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Class instantiation"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the Square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ Perimeter of Square object """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ String representation of Square object """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Creating a Square instance """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
