x = input("What's x? ")
y = input("What's y? ")
z = int(x) + int(y)
print(z)

x = int(input("What's x? ")) # nesting functions
y = int(input("What's y? ")) # int = 8
print(x + y)
print(int(input("What's x? ")) + int(input("What's y? ")))

x = float(input("What's x? ")) # float = 8.8
y = float(input("What's y? "))
z = round(x + y)
print(round(x + y)) # round up
print(z)

x = float(input("What's x? ")) # float = 8.8
y = float(input("What's y? "))
z = (x + y)
z = round(x + y)
print(f"{z:,}") # :, = ,

x = float(input("What's x? "))
y = float(input("What's y? "))
z = (x / y)
z = round(x / y, 2) # the 2 is rounding to two digits
print(z)
# print(f{z:2f}) # using a f STR to rounding to two digits $ error?

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


main()
#docs.python.org/3/library/functions.html#round
