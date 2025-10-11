exit = "no"

while exit == "no":
  animal_sound = input("What animal do you want to hear?").lower().replace(" ", "")

  if animal_sound == "cow":
    print("A cow goes moo")
  elif animal_sound == "pig":
    print("A pig goes oink")
  elif animal_sound == "sheep":
    print("A sheep goes baa")
  elif animal_sound == "duck":
    print("A duck goes quack")
  elif animal_sound == "dog":
    print("A dog goes woof")
  elif animal_sound == "cat":
    print("A cat goes meow")
  else:
    print("I don't know that animal")
    
  exit = input("Do you want to exit?").lower().replace(" ", "")
  if exit != "no":
      print("Goodbye")
      exit = "yes" # this is to make sure that the while loop stops
      # if the user enters anything other than "no" the while loop will stop
      # the variable exit is used to stop the while loop

# the 1st variable is the last one that was used in the while loop

print(animal_sound)
