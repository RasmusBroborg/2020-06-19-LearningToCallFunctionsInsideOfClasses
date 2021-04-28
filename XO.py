def XO(varY):

    str(varY)
    listOfXs = []
    listOfOs = []

    varY = varY.lower()

    numOfChar = len(varY)

    for i in range(0, numOfChar):
        if varY[i] == "x":
            listOfXs += [varY[i]]
        elif varY[i] == "o":
            listOfOs += [varY[i]]

    if len(listOfOs) == len(listOfXs):
        return True
    else:
        return False
