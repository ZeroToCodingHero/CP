print("*** Welcome to the tip calculator ***")
mybill = float(input("Enter your bill: "))
numberofpeople = int(input("Enter the number of people: "))
tip =int(input("Enter the tip percentage: "))
answer = mybill / numberofpeople
answer = round(answer, 2)

if tip == 5:
    answer = answer + (answer * 0.05)
    print("Each person should pay: ", answer)
elif tip == 10:
    answer = answer + (answer * 0.10)
    print("Each person should pay: ", answer)
elif tip == 15:
    answer = answer + (answer * 0.15)
    print("Each person should pay: ", answer)
else:
    print("Invalid tip percentage")