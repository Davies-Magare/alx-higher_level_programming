#!/usr/bin/poython3
"""
The rectangle class
"""


from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        """set_width: width setter"""

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        """set_height: height setter"""

        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        """set_x: x setter"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        """set_y: y setter"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """area: returns the area of the rectangle"""

        return self.__height * self.__width

    def display(self):
        """display: prints the rectangle with #"""

        for i in range(self.__y):
            print()
        row = self.__width * '#'
        for i in range(self.__height):
            for j in range(self.__x):
                print(' ', end='')
            print(row)

    def __str__(self):
        return('[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.__x,
                                        self.__y, self.__width, self.__height))
