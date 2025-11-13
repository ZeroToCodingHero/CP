students = int(input("how many students on the course? "))
groups = int(input("what is the desired group size? "))

number_of_groups = students // groups

print(f"Number of groups formed: {number_of_groups}")

students = int(input("How many students on the course? "))
group_size = int(input("What is the desired group size? "))
number_of_groups = students // group_size
if students % group_size != 0:
    number_of_groups += 1
print(f"Number of groups formed: {number_of_groups}")   