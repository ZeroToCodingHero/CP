# Input user first name - Remove whitespace from str and capitalize user's name
# first_name = input("What's your first name? ").strip().title()  # method
# Input user last name
# last_name = input("What's your last name? ").strip().title()

# first_name = first_name.strip().title()
# last_name = last_name.strip().title()

# Output Hello + name
# print("Hello, " + first_name + ' ' + last_name)
# print("Hello,", first_name + ' ' + last_name)
# print(f"Hello, {first_name + ' ' + last_name}")

# culculator
# x = input("What's x? ")
# y = input("What's y? ")
# z = int(x) + int(y)
# print(z)

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x / y, 3)
print(z)

z = x / y
print(f"{z:.3f}")
