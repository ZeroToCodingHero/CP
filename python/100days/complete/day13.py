print("***GRADE GENERATOR***")
print("Enter your marks below")
test1 = int(input("Enter your test1 marks: "))
test2 = int(input("Enter your test2 marks: "))
test3 = int(input("Enter your test3 marks: "))

grade = (test1 + test2 + test3) / 3 # calculate the average of the three tests

if grade >= 90:
  (print("Your grade is a A", grade, "is your average"))
elif grade >= 80 and grade < 90:  
  (print("Your grade is B", grade, "is your average"))
elif grade >= 70 and grade < 80:
  (print("Your grade is C", grade, "is your average"))
elif grade >= 60 and grade < 70:
  (print("Your grade is D", grade, "is your average"))
else:
  (print("Your grade is F", grade, "is your average"))

print(grade)