print (" *** Day 11 How many seconds in a year*** ")

year = int(input("Enter the year: "))
seconds = 365 * 24 * 60 * 60
leap_year = (2000, 2004, 2008, 2012, 2016, 2020, 2024)

if year == leap_year:
    print("This is a leap year")
    print("There are", seconds + 86400, "seconds in this year")
else:
    print("This is not a leap year")
    print("There are", seconds, "seconds in this year")


# does not work, need to come back and fix it