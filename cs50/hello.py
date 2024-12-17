#  variable = name - ( = is the assignment operator ) - return value = (What's your name ")
name = input("What's your name ").strip().title() # ask user for their name with a "str"
# remove whitespace & capitalize the user's name - .strip = method
# name = name.capitalize() capitalize the frist letter

#split user's name into frist name and last name
first, last = name.split(" ")

# print is a function - "hello, world" is a arguments - the output is a side effect - mistakes are bugs
# what you can pass to a function & what those inputs and called are parameters
# what you actually use the function and pass in values inside of those parentheses, those inputs, those values are arguments
'''
parameters & arguments are the same thing, but the terms you use from looking at the problem from different directions.
When we're looking at what the function can take versus what you're actually passing into the function.
'''
print("hello, ") # say hello to user
print(name)
print("hello, " + name) # + = concatenation
print("hello,", name)
print("hello, ", end='') # how to override end= removes \n from code
print(name)
print("hello, ", name, sep='') # how to override sep= (separator)
print("hello, \"02codinghero\"")
print(f"hello, {first}") # f = multiple different inputs

# \n = new line

# docs.python.org/3/library/functions.html
# docs.python.org/3/library/functions.html#print

def hello(to="world"):
    print("hello,", to)


hello()
name = input("What's your name? ")
hello(name)


def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()
