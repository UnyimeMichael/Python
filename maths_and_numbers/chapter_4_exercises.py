# name_1 = "Animal"
# name_2 = "Badger"
# name_3 = "Honey Bee"
# name_4 = "Honeybadger"
# name_1 = name_1.lower()
# name_2 = name_2.lower()
# name_3 = name_3.lower()
# name_4 = name_4.lower()
# print(name_1)
# print(name_2)
# print(name_3)
# print(name_4)
# name_1 = name_1.upper()
# name_2 = name_2.upper()
# name_3 = name_3.upper()
# name_4 = name_4.upper()
# print(name_1)
# print(name_2)
# print(name_3)
# print(name_4)
#
# string1 = "   filet Mignon"
# string1 = string1.lstrip()
# string2 = "Brisket   "
# string2 = string2.rstrip()
# string3 = "   Cheeseburger   "
# string3 = string3.strip()
# print(string1)
# print(string2)
# print(string3)
#
#
# string1 = "Becomes"
# print(string1.startswith("Be"))
# string2 = "becomes"
# print(string2.startswith("be"))
# string3 = "BEAR"
# print(string3.startswith("BE"))
# string4 = "bEautiful"
# print(string4.startswith("bE"))
#
# password = input("Tell me your password: ")
# password = password.title()
# print("The first letter you entered was: " , password[0])
#
# num = 10
# num_eaten = 3
# pname_1 = "Animal"
# name_2 = "Badger"
# name_3 = "Honey Bee"
# name_4 = "Honeybadger"
# name_1 = name_1.lower()
# name_2 = name_2.lower()
# name_3 = name_3.lower()
# name_4 = name_4.lower()
# print(name_1)
# print(name_2)
# print(name_3)
# print(name_4)
# name_1 = name_1.upper()
# name_2 = name_2.upper()
# name_3 = name_3.upper()
# name_4 = name_4.upper()
# print(name_1)
# print(name_2)
# print(name_3)
# print(name_4)
#
# string1 = "   filet Mignon"
# string1 = string1.lstrip()
# string2 = "Brisket   "
# string2 = string2.rstrip()
# string3 = "   Cheeseburger   "
# string3 = string3.strip()
# print(string1)
# print(string2)
# print(string3)
#
#
# string1 = "Becomes"
# print(string1.startswith("Be"))
# string2 = "becomes"
# print(string2.startswith("be"))
# string3 = "BEAR"
# print(string3.startswith("BE"))
# string4 = "bEautiful"
# print(string4.startswith("bE"))
#
# password = input("Tell me your password: ")
# password = password.title()
# print("The first letter you entered was: " , password[0])
#
# num = 10
# num_eaten = 3
# print("i am going to eat the remaining " + str(num - num_eaten) + " pancakes")
#
# s = "24"
# print(int(s) * 2)
#
# s = "24"
# print(float(s) * 2)
#
# a = 4
# b = "4"
# print(str(a),b)
#
# number1 = input("Enter first number: ")
# number2 = input("Enter second number: ")
# multiply = int(number1) * int(number2)
# print("The product of ", int(number1) , "and" , int(number2), "is" , float(multiply))
# print(F"The product of {number1} and {number2} is {float(multiply)}")
# print("The product of {} and {} is {}".format(number1, number2, float(multiply)))

weight = 0.2
animal = "newt"
print(float(weight)," kg is the weight of the ", animal)
print("{} kg is the weight of the {} ".format(weight,animal))
print(f"{weight} kg is the weight of the {animal}")


text = input("Enter some text: ")
text = text.replace("a","4")
text = text.replace("b","8")
text = text.replace("e","3")
text = text.replace("l","1")
text = text.replace("o","0")
text = text.replace("s","5")
text = text.replace("t","7")
print(text)