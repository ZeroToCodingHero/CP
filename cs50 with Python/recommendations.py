def main():
    difficulty = input("Difficult or Casual? ")
    players = input("Multiplayer or Single-player? ")

    if difficulty == "Difficult":
        if players == "Multiplayer":
            recommend("Poker")
        elif players == "Single-player":
            recommend("Klondike")
        else:
            print("Enter a valid number of players")
    elif difficulty == "Casual":
        if players == "Multiplayer":
            recommend("hearts")
        elif players == "Single-player":
            recommend("Clock")
        else:
            print("Enter a valid number of players")
    else:
        print("Enter a valid difficulty")


def recommend(game):
    print("You might like", game)


main()
