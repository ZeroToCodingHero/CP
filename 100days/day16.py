from time import sleep

print("Fill in the blank lyrics!")
sleep(2)
print("can you guess the missing lyrics?")
sleep(2)
print("Never going to _____ you up.")


counter = 1
while True:
    answer = input("whats your guess? ").lower().replace(" ", "")
    if answer == "give":
        print("Well done! It only took you", counter, "attempts!")
        break    # This will exit the loop
    else:
      print("nope! try again!")
      counter += 1
