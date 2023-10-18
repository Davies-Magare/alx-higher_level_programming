#!/usr/bin/python3

"""
square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The square class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """width: returns the size"""

        return self.width

    @size.setter
    def size(self, size):
        """width: sets the size"""

        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        elif (size <= 0):
            raise ValueError("width must be > 0")

        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """update: updates square attributes"""

        if len(args) != 0:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id, self.size = args
            elif len(args) == 3:
                self.id, self.size = args[:2]
                self.x = args[2]
            elif len(args) == 4:
                self.id, self.size = args[:2]
                self.x, self.y = args[2:]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
