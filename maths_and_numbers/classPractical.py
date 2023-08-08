# import datetime
#
# # print("Enter a name: ")
# # name = input()
# # name = name.replace(name[0], "3")
# # print(name)
#
#
# def age(year):
#     year1 = datetime.datetime.now()
#     current = year1.year - year
#     return current
#
#
# print("Enter your year of birth")
# year = int(input())
# print(age(year))
#
#
# def convert(amount):
#     return amount * 750
#
#
# print("Enter amount in dollar")
# amount = int(input())
# print(f"${amount} is {convert(amount): ,.2f} naira")
#
# # word = input("Enter a word : ")
# # print(word[::-1])
# # print(word[2:6:-1])
#
#
# def multiply(x, y):
#     return x * y
#
#
# print(multiply(3, 10))

#
# def multiply(*lst):
#     product = 1
#     for num in lst:
#         product *= num
#     return product
#
#
# print(multiply(3, 10, 5, 16))
#
# add = 0
# for number in range(11):
#     add += number
# print(add)

names = []
print("Enter names not more than 10 characters: ")
for name in range(5):
    name = input()
    if 0 < len(name) <= 10:
        names.append(name)
    else:
        while 1 > len(name) > 10:
            name = input("please kindly enter names not more than 10 characters: ")
            if 0 < len(name) <= 10:
                names.append(name)

print(names)


# names = []
# name = input("Enter names not more than 10 characters: ")
# for name in range(5):
#     if 0 < len(name) <= 10:
#         names.append(name)
#     print(names)
# else:
#     name = input("Enter names not more than 10 characters: ")