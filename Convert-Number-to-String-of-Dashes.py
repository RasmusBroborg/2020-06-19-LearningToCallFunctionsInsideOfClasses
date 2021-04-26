from random import randrange
num1 = randrange(60)
print("The random number between 1-60 is: " + str(num1))

def num_to_dashes(x):
    p = "_" * x
    return p

print(num_to_dashes(num1))
