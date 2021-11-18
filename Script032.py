"""
firstNames = ['Anthony', 'Timothy', 'Sean', 'John']
lastNames = ['Smith', 'Parker', 'Conrad', 'Washington', 'Kennedy']
temporaryList = []
i = 0
b = 0
c = 0
for item in lastNames:
    for item in firstNames:
        temporaryList.insert(c, firstNames[i] + lastNames[b])
        i = i + 1
        c = c + 1
    if i > len(firstNames) - 1:

        # New block 1. Now writting current family name to families.txt
        file = open("families.txt", 'a')
        file.write(lastNames[b] + '/n')
        file.close()

        # New block 2. Now writting chain of cyborg-names to Smith.txt, Parker.txt, etc.
        print(lastNames[b], ' = ', temporaryList)
        file =open(lastNames[b] + ".txt", 'w')
        temporaryList = str(temporaryList)
        file.write(temporaryList)
        temporaryList = []
        file.close()
               
        b = b +1
        i = 0
        c = 0
"""

firstNames = ['Anthony', 'Timothy', 'Bob', 'Sean', 'John']
lastNames = ['Smith', 'Parker', 'Conrad', 'Washington', 'Kennedy']
tempDict = {}
i = 0
b = 0
for item in lastNames:
    for item in firstNames:
        tempDict = {'alias': firstNames[i] + lastNames[b], 'firstName': firstNames[i], 'familyName': lastNames[b]}
        file = open(lastNames[b] + ".txt", 'a')
        file.write(str(tempDict) + '\n')
        file.close()
        temporaryDict = {}
        i = i + 1
    if i >= len(firstNames):
        file = open("Families.txt", 'a')
        file.write(lastNames[b] + '\n')
        file.close()
        b = b + 1
        i = 0
        print(firstNames)
        print(lastNames)
