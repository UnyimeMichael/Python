list1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


def odd_value(n):
    if n % 2 != 0:
        return n


# print(list(filter(odd_num, list1)))

print(list(filter(lambda n: n % 2 != 0, list1)))

list2 = {1, 2, 3, 4, 5}


def square(numbers):
    return numbers ** 2


ans = list(map(lambda numbers: numbers ** 2, list2))
print(ans)
