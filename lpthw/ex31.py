print("""Yoy enter a dark room with two doors.
Do you go through door #1 or door #2 or door 3?""")

door = input("> ")

if door == "1":
    print("There's a giant beaer here eating a cheese cake.")
    print("What do you do?")
    print("1, Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off.  Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

elif door == "3":
    print("Good choice")
    print("1. Gold coins")
    print("2. Treasure chest")

    price = input(">")

    if price == "1":
        print("You win one gold coin")
    elif price == "2":
        print("You win a treasure chest of silver coins")
    else:
        print("You lost it all")

else:
    print("You stumble around and fall on a knife and die. Good job!")
