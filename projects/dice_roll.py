import random

while True:
    def dice_roll():
        available_choices = range(1, 7)
        dice_one = random.choice(available_choices)
        dice_two = random.choice(available_choices)
        print(f"Dice One =", dice_one,'\n' "Dice Two =", dice_two)

    dice_roll()

    play_again = input("play again? (y/n): ")
    if play_again.lower() != "y":
        break

print("Thank you for playing")
