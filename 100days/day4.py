print("***ADVENTURE STORY***")
name = input("what's your name? ")
age = int(input("what's your age? "))
place = input("where do you live? ")

# three ways to print the same thing
print("'Hello", name, "you are", age, "years old and you live in", place)
print(f"Hello {name} you are {age} years old and you live in {place}")
print("Hello " + name + " you are " + str(age) + " years old and you live in " + place)