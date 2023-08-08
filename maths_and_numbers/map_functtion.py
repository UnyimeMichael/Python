#map is used to iterate through a list of element

list2 = {1, 2, 3, 4, 5}


def square(numbers):
    return numbers ** 2


ans = list(map(square, list2))
print(ans)