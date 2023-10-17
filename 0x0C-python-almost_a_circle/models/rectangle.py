#!/usr/bin/python3
"""
The rectangle class
"""


from models.base import Base


class Rectangle(Base):
    """The class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width: returns the value of width"""
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
        """height: returns the height"""
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
        """x: returns the value of x"""

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
        """y: returns the value of y"""

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
        """str: returns string representation of rectangle"""

        return '[Rectangle] ({}) {}/{} - {}/{}'.format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """update: updates Rectangle attributes"""
        if (len(args) != 0):
            ls = []
            for item in args:
                ls.append(item)
            if len(ls) == 1:
                self.id = ls[0]
            elif len(ls) == 2:
                self.id, self.__width = ls
            elif len(ls) == 3:
                self.id, self.__width = ls[:2]
                self.__height = ls[2]
            elif len(ls) == 4:
                self.id, self.__width = ls[:2]
                self.__height, self.__x = ls[2:]
            elif len(ls) == 5:
                self.id, self.__width = ls[:2]
                self.__height, self.__x, self.__y = ls[2:]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.__width = kwargs["width"]
            if "height" in kwargs:
                self.__height = kwargs["height"]
            if "x" in kwargs:
                self.__x = kwargs["x"]
            if "y" in kwargs:
                self.__y = kwargs["y"]
