# define a variable with a integar value
people = 50
cars = 40
trucks = 150

if cars > people or trucks > cars:
    print ("We should take the cars.")

elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars and people < trucks:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks")
else:
    print("We still can't decide.")

if not people > trucks:
    print("Alright, let's just take the trucks")
else:
    print("Fine, let's stay home then.")
