# student = {"name" : "torin", "age": 41, "no_of_children": 6}
# print(student["name"], student["age"])
#
# students = [
#             {"name" : "torin", "age": 41, "no_of_children": 6},
#             {"name": "sultan", "age": 32, "no_of_children": 3},
#             ]
# print(students[0]["name"], students[0]["age"], students[1]["name"], students[1]["age"])
#


student_records = [{"Id": 101, "Name": "femi", "score:": (40, 50, 60)},
           {"Id": 102, "Name": "kemi", "score": (60, 70, 80)},
           {"Id": 103, "Name": "yemi", "score": (70, 75, 80)},
           {"Id": 104, "Name": "kunle", "score": (50, 70, 80)},
           {"Id": 105, "Name": "dayo", "score": (70, 60, 80)}
           ]
student_records.append({"Id": 106, "Name": "segun", "score:": (80, 70, 55)})
student_records.append({"Id": 107, "Name": "bayo", "score:": (80, 90, 65)})
print(student_records)
student_records.pop(4)
print(student_records)



