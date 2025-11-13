# name is the variable. It contains a string.
name = input("> ")
print(f"Hello, {name} it's very naice to meet you. ")

# taxRate, subtotal, tax and total are all variables that contain numbers.
taxRate = 0.14
subtotal = 20
tax = subtotal * taxRate
total = subtotal + tax
print("Your total bill is:")
print(total)

# travelDestinations is a variable containg a list.
# city is a variable-- It's value changes a few times.
travelDestinations = ["Almaty", "Moscow", "Buenos Aires", "Manila"]
for city in travelDestinations:
    print(city + " seems like a cool place to go.")
