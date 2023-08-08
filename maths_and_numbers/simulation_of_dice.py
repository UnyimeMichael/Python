import random

one = 0
two = 0
three = 0
four = 0
five = 0
six = 0

count = 1
while count <= 10000:
    number = random.randrange(1, 7)
    if number == 1:
        one += 1
    elif number == 2:
        two += 1
    elif number == 3:
        three += 1
    elif number == 4:
        four += 1
    elif number == 5:
        five += 1
    elif number == 6:
        six += 1
    count += 1


print("The number of times one appear is ",one )
print("The number of times two appear is " , two )
print("The number of times three appear is ", three )
print("The number of times four appear is " , four )
print("The number of times five appear is ", five )
print("The number of times six appear is ", six )