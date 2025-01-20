import random

def dice_roll():
    available_choices = range(7)
    player = random.choice(available_choices)
    print(player)

dice_roll()


x = 5
y = 2
result = x ** y
print(result)