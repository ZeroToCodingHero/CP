forecast = int(input("What is the weather forcast tomorrow? "))
rain = (input("Will it rain? (yes/no)"))

a = ("Wear jeans and a T-shirt")
b = ("I recommend a jumper as well")
c = ("Take a jacket with you")
d = ("Make it a warm coat, actually")
e = ("I think gloves are in order")
r = ("Don't forget your umbrella")

if forecast >= 20:
    print(a)
if forecast >= 10 and forecast <= 19:
    print(b)
if forecast >= 5 and forecast <= 9:
    print(c)
if forecast <= 4:
    print(d)
    print(e)
if rain == "yes":  
    print(r)
else:
    ("print invaild anwser")
   