Convert Minutes into Seconds
#https://edabit.com/challenge/FQyaaJx7orS7tiwz8

#Description: Write a function that takes an integer minutes
#and converts it to seconds.

def minToSec(minutes):
    sec = minutes*60
    return sec

print(minToSec(int((input()))))
