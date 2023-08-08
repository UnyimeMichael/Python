from sys import getsizeof

#list gives comprehended display
double = [a ** 2 for a in range(1000000)]
#tuple list gives a generator
doubles = (a ** 2 for a in range(1000000))
print(getsizeof(double))
print(getsizeof(doubles))