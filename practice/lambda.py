# lambda is an anonymous function that can be used inside another function
# function called add with two arguments
def add(x,y):
    return(x + y)
print(add(5,5))
# waste of space if never using it this funcation again

# lambda with two arguments (x,y:) with one line a expression (x+y) than two arguments (5,5)
print((lambda x,y: x+y)(5,5))