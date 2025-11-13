people1 = [
    "Mal",
    "Zoe",
    "Wash",
    "Jayne",
    "Sage",
    "Ian",
    "Kaylee"
]

people2 = [
    "Ryan",
    "Karen",
    "Dexter",
    "Wally",
    "Ian",
    "Pat"
]

# concatenate lists
people3 = people1 + people2

# to add to a list
people3.insert(0, "John")
people3[0] = ("Ethan")
# to remove from the list
people3.pop()
del people3[1]
people4 = ["Christi","Patrice","Craig","Dexter","Wally"]
people3.extend(people4)
people3.insert(8, "Hubert")
people3.insert(12, "Omar")
people3.insert(9, "Otto")
people3.insert(-9, "Chauncey")

# Oh no-- Now "AVERAGE PLAYER" is no longer in the middle! Find a way to fix this. 
people3.insert(7, "Average Player")
people3[7] = people3[7].upper()


print(people3[0:])
num = (len(people3))
print(num / 2)
