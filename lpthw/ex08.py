formatter = "{} {} {} {}" # Variable & place holders
#     Variable  Method what I want to add to the place holder
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, False))
print(formatter.format(formatter, formatter, formatter, formatter)) # this prints 16 as it prints 4 x 4
print(formatter.format(
    "try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
