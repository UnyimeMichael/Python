# double = {}
# for a in range(1, 11):
#     double[a] = a ** 2
# print(double)

# doubles = {a: a ** 2 for a in range(1, 11)}
# print(doubles)
#
# from


def div(number):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz:", number)
    elif number % 3 == 0:
        print("fizz", number)
    elif number % 5 == 0:
        print("buzz:", number)
    else:
        print(number)


for number in range(1, 50):
    div(number)

list2 = {1, 2, 3, 4, 5}


def square(numbers):
    return numbers ** 2


ans = list(map(square, list2))
print(ans)
