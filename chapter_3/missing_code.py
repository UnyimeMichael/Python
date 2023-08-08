for rows in range(4):
    for column in range(4):
        print('0', end='')
    print()

a = 1
b = 2
c = a
a = b
b = c
print(a)
print(b)

a = 1
b = 2
a, b = b, a
print(a)
print(b)


lst = [25, 10, 15, 5, 30, 55, 35, 45, 20]
#print(sorted(lst))

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
print(lst)
(lst.sort())
print(lst)
