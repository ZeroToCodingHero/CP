import random
cards = ["jack", "queen", "king"]

def main():
    print(random.choices(cards, weights=[75, 20, 5], k=2))
        # random.sample                           # k= how many you wish to choose from

def main():
    random.seed(0) # to use to help debug
    print(random.choices(cards, k=2))


main()