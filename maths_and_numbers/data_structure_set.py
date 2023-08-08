lst = (4, 1, 1, 1, 2, 2, 3, 4, 1)
lst = {4, 1, 1, 1, 2, 2, 3, 4, 1}
print(list)
print(set(list))
print(len(set(list)))

set1 = {1,2,3,4}
print(set1)
set2 = {1,4,5,6,7,9}
set2.add(10)
print(set2)
# union
print(set1 | set2)
# intersection
print(set1 & set2)
# uncommon values
print(set2 ^ set1)


if 6 not in set1:
    print("yes")


lst = [1, 2, 4, 5, 2, 3, 5, 6, 3, 5]
num = set(lst)
print(num)
