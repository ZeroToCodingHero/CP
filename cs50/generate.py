# from random import choice / to requset just one part of the random module 
import random

coin = random.choice(["heads", "tails"])
print(coin)

number = random.randint(1,10)
print(number)

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)

# https://docs.python.org/3/library/random.html
