# def common_list(lst1, lst2):
#     lst1 = []
#     lst2 = []
#     lst3 = []
#     for element in lst1 and lst2:
#         return tuple()


def common_list(a, b):
    return tuple([i for i in a if i in b])


a = [1, 2, 3, 4, 5]
b = [4, 0, 7, 3, 2]
print(common_list(a, b))
