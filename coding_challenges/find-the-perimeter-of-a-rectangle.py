#Find the Perimeter of a Rectangle

#Create a function that takes height and width #and finds the perimeter of a rectangle.

#https://edabit.com/challenge/Yx2a9B57vXRuPevGh

def find_perimeter(height, width):
    result = (int(height)*2)+(int(width)*2)
    return result
    
#testing the function
print(find_perimeter(3, 2))
