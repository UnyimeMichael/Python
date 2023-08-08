print("Enter number1")
a = input()
print("Enter number2")
b = input()
c = a
a = b
b = c
print(a)
print(b)

a = input("enter a: ")
b = input("enter b: ")
a, b = b, a
print("a = " + a)
print("b = " + b)


name = "victoria"
#print(name[::-1])
print(name[0:8:2])
print(name[::-2])

name = input("enter name: ")
name = name.lower()
print(name)
name = name.upper()
print(name)

