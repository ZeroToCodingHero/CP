emoticon = "v.v"


def main():
    global emoticon  # this modifies a global VAR
    say("Is anyone there?")
    emoticon = ":D"
    say("Oh, hi!")


def say(phrase):
    print(phrase + " " + emoticon)


main()


def main():
    print("Hello")
    return main

main()