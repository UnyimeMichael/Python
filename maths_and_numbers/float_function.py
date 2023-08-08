def float_input(a: float, b: float):
    try:
        if type(a, b) in [float]:
            return f"{a} and {b} is a float"
    except TypeError:
        return f"{a} and {b} is an error"


a = 2.5
b = 9.0
print(float_input(a, b))
