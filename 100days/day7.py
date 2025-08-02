print("***FAKE FAN FINDER***")

fakefan = input("what is your favarite super hero? ")
if fakefan == "batman":
  print("good choice")
  cape = input("do you like the cape? ")
  if cape == "yes":
    print("you are not a fake fan")
  elif cape == "no":
    print("you are a fake fan")
  else:
    print("try again")
elif fakefan == "superman":
  print("good choice")
  fly = input("do you like to fly? ")
  if fly == "yes":
    print("you are not a fake fan")
  elif fly == "no":
    print("you are a fake fan")
  else:
    print("try again")
else:
  print("you are a fake fan")