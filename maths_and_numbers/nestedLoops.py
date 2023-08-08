# for i in range(7):
#     print("step", end = " ")
#     for i in range(3):
#         print("clap")

def multiplication(number):
    for i in range (1, 12+1):
        for j in range(1,number+1):
            print(end=" " f"{i: >4} * {j: >1} = {i * j: >3}  ")
        print()

multiplication(20)


found = False
names = ["sultan", "david" , "mariam", "lateef"]
for name in names:
    if name.startswith("s"):
        print("found")
        found = True
        break
else:
    print("not found")

