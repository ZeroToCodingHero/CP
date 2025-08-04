forecast = int(input("What is the weather forcast tomorrow? "))
rain = (input("Will it rain? (yes/no)"))

a = ("Wear jeans and a T-shirt")
b = ("I recommend a jumper as well")
c = ("Take a jacket with you")
d = ("Make it a warm coat, actually")
e = ("I think gloves are in order")
r = ("Don't forget your umbrella")

if forecast >= 20 and rain == "no":
    print(a)
elif forecast >= 20 and rain == "yes":
    print(a)
    print(r)
elif forecast > 10 and forecast <= 19 and rain == "no":
    print(a)
    print(b)
elif forecast > 10 and forecast <= 19 and rain == "yes":
    print(a)
    print(b)
    print(r)
elif forecast >= 5 and forecast <= 10 and rain == "no":
    print(a)
    print(b)
    print(c)
elif forecast >= 5 and forecast <= 10 and rain == "yes":
    print(a)
    print(b)
    print(c)
    print(r)
elif forecast < 5 and rain == "no":
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(c)
elif forecast < 5 and rain == "yes":
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(r)
else:
    ("print invaild anwser")
