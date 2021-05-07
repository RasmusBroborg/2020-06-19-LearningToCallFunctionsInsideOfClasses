#What is the average of the number?

#Create a function that takes a list of numbers and return the average of the number.

#[1, 2, 3] ➞ 2 #1 + 2 + 3 = 6 / 3 = 2

#[34, 65, 12] ➞ 37

#[13, 13, 13] ➞ 13

def averageNum(listOfNum):
    
    lengthOfList = len(listOfNum)
    sumOfList = sum(listOfNum)
    average = int(sumOfList / lengthOfList)
    
    return average


#Testing the function:
print(averageNum([34, 65, 12]))
