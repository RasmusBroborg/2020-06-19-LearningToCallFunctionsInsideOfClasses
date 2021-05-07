#Area of a Triangle Coding Challenge

#Description: Write a function that takes the base
#and height of a triangle and return its area.
#Area of a triangle is b*h/2

def areaTriangle(b,h):
    return b*h/2

base = int(input("Enter the triangle base value: "))
height = int(input("Enter the triangle height value: "))

print(areaTriangle(base,height))
