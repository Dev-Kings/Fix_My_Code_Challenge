#!/usr/bin/python3
""" Module for square class """


class square():

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Class instantiation"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ Perimeter of square object """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ String representation of square object """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Creating a square instance """
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
