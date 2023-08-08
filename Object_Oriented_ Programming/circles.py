from math import pi


def area_of_circle(radius):
    area = pi * (radius ** 2)
    if radius < 0:
        raise ValueError("radius cannot be less than 0")
    return f" The area of a circle is {area}"