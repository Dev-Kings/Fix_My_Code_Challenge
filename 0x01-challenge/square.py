#!/usr/bin/python3
"""
Square module with functions to compute area and perimeter.
"""


class square():
    """ Class square with area and perimeter calculation functions.
    """
    def __init__(self, **kwargs):
        self.width = kwargs.get('width', 0)
        self.height = self.width

    @property
    def width(self):
        return (self._width)

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("Width must be a non-negative value")
        self._width = value
        self._height = value

    @property
    def height(self):
        return (self._height)

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("Height must be a non-negative value")
        self._width = value
        self._height = value

    def area_of_my_square(self):
        """ Area of the square """
        return (self.width * self.width)

    def PermiterOfMySquare(self):
        """ Perimeter of the square """
        return (self.width * 4)

    def __str__(self):
        return ("{}/{}".format(self.width, self.height))


if __name__ == "__main__":
    s = square(width=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
