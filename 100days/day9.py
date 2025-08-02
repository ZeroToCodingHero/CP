print("*** Day 9: Challenge ***")
year = int(input("What year are you born? "))

if year < 1925:
    print("You are too old for this program")
if year > 1925 and year < 1946:
    print("You are a Traditionalist")
if year > 1946 and year < 1965:
    print("You are a Baby Boomer")
if year > 1965 and year < 1981: 
    print("You are a Generation X")
if year > 1981 and year < 1997:
    print("You are a Millenial")
if year > 1997 and year < 2013:
    print("You are a Generation Z")
if year > 2013:
    print("You are a Generation Alpha")
else:
    print("You are too young for this program")
