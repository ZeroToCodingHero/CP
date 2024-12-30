# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.
# *args = If you do not know how many arguments that will be passed into your function, add a * - def my_function(*kids):
# **kwargs = If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** - def my_function(**kid):

emoticon = "v.v"


def main():
    global emoticon  # this modifies a global VAR
    say("Is anyone there?")
    emoticon = ":D"
    say("Oh, hi!")


def say(phrase):
    print(phrase + " " + emoticon)


main()


def main():
    print("Hello")
    return main

main()
