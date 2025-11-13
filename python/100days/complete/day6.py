print("*** My Login System ***")
print()

username = input("what's your username? ")
password = input("What's your password? ")

if username == "admin" and password == "1234":
  print(f"welcome {username} you are logged in, have a great day")

elif username == "john" and password == "2345":
  print(f"welcome {username} you are logged in, go get a morning coffee")

elif username == "karen" and password == "3456":
  print(f"welcome {username} you are logged in, you are late for work, get going")

elif username == "ethan" and password == "4567":
  print(f"welcome {username} you are logged in, the sun is shinning, take the day off.")

else:
  print("wrong username or password")
