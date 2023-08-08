# def duplicate(items):
#     lst2 = set(items)
#     # print(lst2)
#     if len(lst2) == len(items):
#         return "There is no duplicate element in your list"
#     else:
#         return "There is a duplicate element in your list"
#
#
# list_of_item = ["yam", "rice", "beans", "garri", "rice"]
# print(duplicate(list_of_item))
#
#
# def duplicate2(lzt: list):
#     for stuff in lzt:
#         if lzt.count(stuff) > 1:
#             print(f"The item {stuff} occurred more than once")
#         else:
#             print(f"There is no duplicates")
#
#
# def discount(price):
#     discount_price = (10 * price) / 100
#     new_price = price - discount_price
#     return new_price
#
#
# price = int(input("Enter amount: "))
# print(f"Your discounted price from {price} is {discount(price)} ")

#
# number = int(input("Guess the winning number: "))
# winning_number = 35
# while number != winning_number:
#     print("wrong number...please try again\nguess the winning number: ")
#     number = int(input())
# print("Congratulations...you have won!!!")


for number in range(1, 11):
    print(f"{number}.", end="")