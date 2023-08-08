# from pip._internal.req.constructors import operators
#
#
# class Calculator:
#     def __init__(self, number1: int, number2: int, operators: chr):
#         self.number1 = number1
#         self.number2 = number2
#         self.operators = operators
#
#     @property
#     def operators(self, addition):
#         addition = chr(+)
#         return self.number1 + self.number2
#
#     @operators.setter
#     def operators(self, value):
#         self._operators = value
#
#
# @operators.setter
#     def operators(self, value):
#         self._operators = value
#
#
# def subtraction(self):
#         return self.number1 - self.number2
#
#     def division(self):
#         return self.number1 // self.number2
#
#     def __str__(self):
#         return f"{self.number1}{self.number2}{self.operators}"

def calculator(number1: int, number2: int, operators: chr()):
    
cal = Calculator(2, 3, +)
print(cal.addition())
