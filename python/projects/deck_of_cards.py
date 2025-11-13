# full deck of cards
import random
from random import shuffle

suits = ['Hearts','Spades','Diamonds','Clubs']
cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A' ]

for i in suits:
    player_one = random.choice(suits)
    print(i)

# available_choices = suit, card
# player_one = random.choice(available_choices)
# player_two = random.choice(available_choices)
# print(f"player one hand =", player_one,'\n' "player two hand =", player_two)


# play_again = input("play again? (y/n): ")
# if play_again.lower() != "y":
#     exit
    
# print("Thank you for playing")