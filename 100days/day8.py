print("***INSULT GENERATOR 3000***")

name = input("What's your name ? ").lower() # .lower() could be used to avoid case sensitivity
print(f"good day {name}")
day = input("What day is it ? ").lower()
workout = input("Did you workout today ? (yes/no) ").lower()
coding = input("Did you code today ? (yes/no) ").lower()
feelings = int(input("How are you feeling today ? (1-5) "))

    
if day == "monday" or day == "Monday" or day == "MONDAY":
    print("It's monday, my dudes get to work")
    if workout == "yes" or workout == "Yes" or workout == "YES":
        print("You did good")
    else:
        print("do better")
    if coding == "yes" or coding == "Yes" or coding == "YES":
        print("You did good")  
    else:
        print("do better")
    print(f"this is how you feel in a emoji {feelings}")      
elif day == ("tuesday", "Tuesday, TUESDAY"): # a diffrent way to coding it
    print("It's tuesday, my dudes ")
    if workout == "yes":
      print("You did good")
    else:
      print("do better")
    if coding == "yes":
      print("You did good")
    else:
      print("do better")
    if feelings <= 3:
        print("cheer up")
    else:
        print("keep it up")
elif day == "wednesday" or day == "thursday" or day == "friday" or day == "saturday" or day == "sunday":
    print("this is the time to relax")
    if workout and coding != "yes":
        print("you need to do better")
    else:
        print("you did good")
else:
    print("not a valid answer, try again")
