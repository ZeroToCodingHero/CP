def name():
    name = input("What's your name? ").strip().title()
    hello(name)

def hello(to="world"):
    print("Hello,", to)

name()

# hello()
# name = input("What's your name? ")
# hello(name)

def main():
    print("Hello world")
    print("This is CS50.")

main()

