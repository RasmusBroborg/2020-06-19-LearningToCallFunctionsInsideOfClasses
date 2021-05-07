def vowelCount():
    x = input("Write a word or a sentence: ")
    lenOfInput = len(x)
    vowelCount = 0
    vowelList = []
    completeVowelList = ["a", "o", "u", "e", "i", "y"]

    for i in range(0, lenOfInput):

        if x[i] in completeVowelList:
            vowelCount += 1
            vowelList += x[i]

    print("The user input " + x + " contains " + str(vowelCount) + " vowels. \n" +
          "The list of vowels used are the following: " + str(vowelList))
