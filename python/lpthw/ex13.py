from sys import argv
# read the WYSS section for how to run this
script, frist, second, third = argv

print("The script is called:", script)
print("Your frist variable is:", frist)
print("your second variable is:", second)
print("Your third varibale is:", third)

user_input = input("Add some text: ")
print(f"Your input was: {user_input}")

# argv = commandline input
# to run code python ex13.py 1st 2nd 3rd
