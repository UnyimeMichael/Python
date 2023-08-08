number = input("Enter a number: ")
print(f"{number} rounded to 2 decimal places is {round(float(number),2)}")

print("Enter a number")
number = input()
print(f"The absolute value of {number} is {abs(float(number))}")


print("Enter a number1")
number1 = input()
print("Enter a number2")
number2 = input()
diff = float(number1) - float(number2)
print(f"The difference between {number1} and {number2} is an integer? {diff.is_integer()}")

print(f"The ans is {3 ** 0.125: .3f}")

print(f"The ans is ${150000: ,.2f}")

print(f"The ans is {2/10: .0%}")