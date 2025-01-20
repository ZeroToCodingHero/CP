names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello, {name}")


# with open("names.txt") as file:
#     for line in sorted(file):
#         print("hello,", line.rstrip())

# with open("names.txt", "r") as file:
#     for line in file:
#        print("hello,", line.rstrip())

# name = input("what's your name? ")

# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

# names = []

# for _ in range(3):
#     names.append(input("What's your name? "))
# for name in sorted(names):
#     print(f"hello, {name}")

# docs.python,org/3/library/functions.html#open
