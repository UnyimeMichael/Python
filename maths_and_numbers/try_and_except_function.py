from math import pi


# def area_circle(r):
#     try:
#         return pi * (r ** 2)
#     except (TypeError, ValueError):
#         print("Eyes dey pain you, enter an integer")
#
#
# print(area_circle('s'))


def multiply(x, y):
    try:
        return x * y
    except TypeError:
        return f"the input must be a number"

print(multiply("a", "b"))

