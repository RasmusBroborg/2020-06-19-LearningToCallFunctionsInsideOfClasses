def shuffleName(name):

  splitName = name.split()
  lenNames = len(splitName)
  listOfNames = []

  for i in range(0, lenNames):
      listOfNames = [splitName[i]] + listOfNames

  nameWrongOrder = " ".join(listOfNames)
  return nameWrongOrder

#Testing of function:
print(shuffleName("Benedict Cumberbatch"))
