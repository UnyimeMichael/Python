my_list = []
name = ["sultan","mariam","torin","awwal","david"]
students = [["sultan",35,200,90.9],["mariam",32,200,95.0]]
print(students[0])
ones = [1]*100
print(ones)
list2 = students + name
print(name[::-1])
print(list2)


for number in range(0,50,2):
    list = [number]
    print(list)

even_number =[]
for number in range(0,51,2):
    even_number.append(number)
    print(even_number)


# even_number = list(range(0,50))
# if even_number % 2 == 1:
#     print(even_number)


number = [1,2,3,4,5]
number[0] = 10
number[4] = 555
print(number)
print(len(number))


number = [1,2,3,4,5]
# x = number[0]
# y = number[1]
# z = number[2]
# a = number[3]
# b = number[4]


# unpacking of variables
x,y,z,a,b = number
X,Y,*others = number
print(x,y,others)
x,y,*other,b = number
print(x,y,other,b)


letters = list("Hello c16")
letter1 = ['a','b','c','d']
print(letters)
print(letter1)

for index, letter in enumerate(letters):
    print(index, letter)


letter1.append('e')
print(letter1)
letter1.insert(0, "z")
print(letter1)
letter1.remove("z")
print(letter1)
letter1.pop()
print(letter1)


even_num = []
for number in range (21):
    if number % 2 == 0:
        even_num.append(number)

even_num2 = [i for i in range(21) if i % 2 == 0]
odd_num = [i for i in range(21) if i % 2 != 0]
print(even_num)
print(even_num2)
print(odd_num)



my_list = []
data =[['dele',10_000.00,20,'09039283848'],
       ['sam', 5000, 10,'09036463735'],
       ['joy', 3000,30,'08038283828'],
       ['vikky',4000,20,'07037363635'],
       ['bayo', 2000, 40, '09049493929']]

data[0][0] = 'femi'
data[0][1] = 7_000
data[1][0] = 'segun'
data[1][2] = 15
print(data)

for number in range(1,21):
    print(number)
for odd_number in range(1,21,2):
    print (odd_number)
number =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
number[4] = 0
number[5] = 0
number[6] = 0
number[7] = 0
number[8] = 0
number[9] = 0
print(number)

list1 = list(range(1,21))
print(list1)
odd_number = list1[::2]
print(odd_number)
list1[4:10] = [0] * len(list1[4:10])
print(list1)
first_seven = list1[:7]
print(first_seven)
list1[:] = []
print(list1)
