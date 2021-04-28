def fizzBuzz(x):
    y = ""
    if x%3 == 0 or x == 3:
        y += "Fizz"
    if x%5 == 0 or x ==5:
        y += "Buzz"
    if y == "":
        y = x
    return y
