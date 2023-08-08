list1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


#
# def odd(number):
#     if number % 2 == 1:
#         return number
#
#
# ans = list(map(odd, list1))
# print(ans)


def odd_num(lzt):
    odd = []
    for n in lzt:
        if n % 2 == 1:
            odd.append(n)

    return odd


print(odd_num(list1))


def odd_value(n):
    if n % 2 != 0:
        return n


print(list(filter(odd_value, list1)))

#print(list(filter(lambda n: n % 2 != 0, list1)))
