import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for name, house in reader:
        students.append({"name": name, "house": house})
                              
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")

print("--------------------------------")
with open("students.csv") as file:
    for line in file:
        name, house =  line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)


def get_name(student):
    return student["name"]
                              # key=lambda student: student["name"]:
for student in sorted(students, key=get_name, reverse=False):
    print(f"{student['name']} is in {student['house']}")

print("--------------------------------")
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")


        # row = line.rstrip().split(",")
        # print(f"{row[0]} is in {row[1]}")


# docs.python,org/3/library/csv.html
