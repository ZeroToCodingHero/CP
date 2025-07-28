print("bill splitter")

total = float(input("what is your total amount ? "))
tip = int(input("what is the tip percentage ? "))
people = int(input("how many people splitting the bill ? "))

tip_total = (tip / 100) * total
total_with_tip = total + tip_total
ppp = total_with_tip / people


print(f"Bill Total:", total)
print(f"Tip percentage:", tip)
print(f"number of people:", people)
print(f"each person should pay:", ppp)
