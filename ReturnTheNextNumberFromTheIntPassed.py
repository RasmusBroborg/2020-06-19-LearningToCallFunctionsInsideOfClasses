#Return the Next Number from the Integer Passed
#https://edabit.com/challenge/KjCS7occ9hfu5snpb

#Create a function that takes a number as an argument,->
#increments the number by +1 and returns the result.


#Function

def nextIntNum(x):
    x = x+1
    return x

#Testing of function
h = int(input("Enter an integer: "))
print(str(h) + " + 1 is " + str(nextIntNum(h)))
