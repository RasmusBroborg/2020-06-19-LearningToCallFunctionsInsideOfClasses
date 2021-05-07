#Is the Number Even or Odd?
#https://edabit.com/challenge/DruRW8YM8PNiH9Kg7

#Create a function that takes a number as an argument and
#returns "even" for even numbers and "odd" for odd numbers.

def isEvenOrOdd(num):
    if num%2 == 0:
        return"even"
    else:
        return"odd"

#Testing

print(isEvenOrOdd(33))
print(isEvenOrOdd(40))
