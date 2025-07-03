class Rectangle:
    def __init__(self, width, height):
        self.__width =  width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
       if value >= 0:
           self.__width = value
       else:
           print('invalid value! Must be non-negative.')

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value >= 0:
            self.__height = value
        else:
            print('invalid value! Must be non-negative.')

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)


r = Rectangle(10, 5)
print(r.area())
print(r.perimeter())
r.width = -3
r.height = 7
print(r.width)
print(r.height)