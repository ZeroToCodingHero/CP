# F to C
fahrenheit = int(input("Please type in a temperture in (F)? "))
celsius = (float(fahrenheit - 32) * 5 / 9)

if fahrenheit > 21:
    print(f"{fahrenheit} degrees Fahrenheit equals {celsius} degrees Celsius")
if fahrenheit <= 21:
    print(f"{fahrenheit} degrees Fahrenheit equals {celsius} degrees Celsius")
    print("Brr! It's cold in here!")

# C to F
def c_to_f():
    celsius = int(input("Please type in a temperture in (C)? "))
    fahrenheit = (float(celsius) * 9 / 5 + 32)
    if celsius > 69:
        print(f"{celsius} degrees Fahrenheit equals {fahrenheit} degrees Celsius")
    if celsius <= 69:
        print(f"{celsius} degrees Fahrenheit equals {fahrenheit} degrees Celsius")
        print("Brr! It's cold in here!")