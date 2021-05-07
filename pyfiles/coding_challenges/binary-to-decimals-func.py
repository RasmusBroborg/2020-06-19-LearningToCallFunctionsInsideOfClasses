  #Binary to decimal

def binaryToDecimals(binaryNum):
    length = len(str(binaryNum))
    decimalsList = []
    x = 0
    y = length - 1


    while x < length:
        binaryDigit = int(str(binaryNum)[y]) * (2**x)
        decimalsList += [binaryDigit]

        y -= 1
        x += 1

    return sum(decimalsList)
