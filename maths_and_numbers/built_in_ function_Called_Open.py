# file = open("student_records.txt", mode='w')
# file.write("001 mariam 75\n")
# file.write("002 david 75\n")
# file.write("001 sultan 75\n")
# file.write("001 torin 75\n")
# file.close()
#
with open("record2.txt", mode='w') as file:
    file.write("001 hyelnati 70\n")
    file.write("002 segun 80\n")
    file.write("003 femi 90\n")

# #append
# with open("record2.txt", mode='a') as file:
#     file.write("004 mariam 75\n")
#
#
# # read and write
# with open("record2.txt", mode='r+') as file:
#     file.write("005 hyelnati 70\n")
#
# # overwriting the file
# with open("record2.txt", mode='w+') as file:
#     file.write("005 hyelnati 70\n")

#
#
# with open("product.txt", mode='w') as file:
#     file.write("101 Benz 50m \n")
#     file.write("102 Toyota 30m \n")
#     file.write("103 Gac 45m \n")
#     file.write("104 Lexus 40m \n")
#
# with open("record2.txt", mode='r') as records:
#     for record in records:
#         num, name, score = record.split()
#         print(f"{num: <10}{name: <10}{score: >10}")

file1 = open('record2.txt', mode ='r')

file2 = open('record.txt', mode='w')

with file1, file2:
    for record in file1:
        sn, name, score = record.split()
        if sn != "005":
            file2.write(record)
        else:
            new_record = ' '.join([sn, "oluwarotimi", score])
            file2.write(new_record + "\n")

