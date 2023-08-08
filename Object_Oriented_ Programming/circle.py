import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("radius cannot be negative")
        self.__radius = value



    def area_of_circle(self):
        area_of_circle = math.pi * self.radius ** 2
        return f" The area of a circle is {area_of_circle}"

    def parameter_of_circle(self):
        parameter_of_circle = 2 * math.pi * self.radius
        return f" The parameter of a circle is {parameter_of_circle}"


c1 = Circle(9)
print(c1.area_of_circle())
print(c1.parameter_of_circle())
