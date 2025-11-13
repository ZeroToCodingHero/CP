emoticon = "v.v"


def main():
    global emoticon # this modifies a global VAR
    say("Is anynone there?")
    emoticon = ":D"
    say("Oh, hi!")


def say(phrase):
    print(phrase + " " + emoticon)

# doesn't run ?
