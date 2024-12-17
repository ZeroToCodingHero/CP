# students = ["Herione", "Harry", "Ron"]

# for student in students:
#     print(student)

# for i in range(len(students)):
#     print(i + 1, students[i])

students = {
    "Hermione": "Gryffindor", 
    "Harry": "Gryffindor", 
    "Ron": "Gryffindor",
    "Draco": "Slytherin",  
}

print(students["Hermione"])

# how to print keys & index 
for student in students:
    print(student,students[student], sep=", ")

students = [
    {"name": "Hermione", "house": "gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "gryffindor", "patronus": "Jack Russell terrrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
