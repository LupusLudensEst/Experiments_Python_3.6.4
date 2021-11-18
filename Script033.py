firstNames = ['Anthony', 'Timothy', 'Bob', 'Sean', 'John', 'Ivan', 'Sergey', 'Peter', 'Anton', 'Nikolas', 'Armen']
lastNames = ['Smith', 'Parker', 'Conrad', 'Washington', 'Kennedy']

coordinatorSet = {'role': 'coordinator', 'capacity': 1000000, 'fuelhrusage': 1, 'hardware': 0, 'hardwareusage': 0, 'hrdistance': 20, 'weapons': 'Yes', 'ammunition': 1000, 'ammunitionhrusage': 100}
infectorSet = {'role': 'infector', 'capacity': 500000, 'fuelhrusage': 2, 'hardware': 1000, 'hardwareusage': 10, 'hrdistance': 15, 'weapons': 'No', 'ammunition': 0, 'ammunitionhrusage': 0}
soldierSet = {'role': 'soldier', 'capacity': 500000, 'fuelhrusage': 2, 'hardware': 0, 'hardwareusage': 0, 'hrdistance': 20, 'weapons': 'Yes', 'ammunition': 2000, 'ammunitionhrusage': 200}
technicianSet = {'role': 'technician', 'capacity': 500000, 'fuelhrusage': 3, 'hardware': 1000, 'hardwareusage': 20, 'hrdistance': 15, 'weapons': 'Yes', 'ammunition': 1000, 'ammunitionhrusage': 100}
scoutSet = {'role': 'scout', 'capacity': 1000000, 'fuelhrusage': 2, 'hardware': 0, 'hardwareusage': 0, 'hrdistance': 30, 'weapons': 'Yes', 'ammunition': 1000, 'ammunitionhrusage': 100}
workerSet = {'role': 'worker', 'capacity': 500000, 'fuelhrusage': 3, 'hardware': 1500, 'hardwareusage': 40, 'hrdistance': 10, 'weapons': 'No', 'ammunition': 0, 'ammunitionhrusage': 0}

fSets = [coordinatorSet, infectorSet, soldierSet, technicianSet, scoutSet, workerSet]

i = 0
b = 0

for item in lastNames:
    c = 0
    for item in firstNames:
        tempDict = {'alias': firstNames[i] + lastNames[b], 'firstName': firstNames[i], 'familyName': lastNames[b]}
        if tempDict['firstName'] == 'Anthony':
            tempDict.update(coordinatorSet)
        elif tempDict['firstName'] != 'Anthony' and c < len(fSets)-1:
            tempDict.update(fSets[c])
        elif tempDict['firstName'] != 'Anthony' and c == len(fSets)-1:
            tempDict.update(fSets[c])
            c = 0

        file = open(lastNames[b] + ".txt", 'a')
        file.write(str(tempDict) + '\n')
        file.close()
        temporaryDict = {}
        i = i + 1
        c = c + 1


    if i >= len(firstNames):
        file = open("Families.txt", 'a')
        file.write(lastNames[b] + '\n')
        file.close()
        b = b + 1
        i = 0
print(coordinatorSet)
