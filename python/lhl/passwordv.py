print("hello welcome to my passwood validator. ")

userinput1 = input("please enter your password. > ")
userinput2 = input("please confirm your password. > ")

if userinput1 != userinput2:
    print("password incorrect")
elif len(userinput1) < 8:
    print("password too short")
else: 
    print("you've successfully set the password")
