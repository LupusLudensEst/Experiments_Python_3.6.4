AnthonySmith = {'alias': 'AnthonySmith', 'firstName': 'Anthony', 'familyName': 'Smith', 'function': 'Coordinator', 'fuelCapacity': 1000000, 'fuelUsagePerHour': 2}
BobSmith = {'alias': 'BobSmith', 'firstName': 'Bob', 'familyName': 'Smith', 'function': 'Infector', 'fuelCapacity': 500000, 'fuelUsagePerHour': 2}
JohnSmith = {'alias': 'JohnSmith', 'firstName': 'John', 'familyName': 'Smith', 'function': 'Soldier', 'fuelCapacity': 500000, 'fuelUsagePerHour': 2}

"""
# printing out several items from the dictionaries
print(AnthonySmith['firstName'], JohnSmith['fuelCapacity'])
"""

"""
# Manipulation on one item in the dictionary
# AnthonySmith['fuelCapacity'] = AnthonySmith['fuelCapacity'] * 2
# AnthonySmith['fuelCapacity'] *= 2
AnthonySmith['fuelCapacity'] -= 1500000
print(AnthonySmith)          
"""


# Adding fields to a dictionary one by one
JoshuaSmith = {}
JoshuaSmith['alias'] = 'JoshuaSmith'
JoshuaSmith['firstName'] = 'Joshua'
JoshuaSmith['familyName'] = 'Smith'
JoshuaSmith['function'] = 'Technician'
JoshuaSmith['fuelCapacity'] = 500000
JoshuaSmith['fuelUsagePerHour'] = 3

# print(JoshuaSmith)



"""
# Adding fields to a dictionary from lists,
# using built-in function zip
# {}-dictionary, []-list
"""

KenSmith = {}
keys = {'alias', 'firstName', 'familyName', 'function', 'fuelCapacity', 'fuelUsagePerHour'}
values = ['KenSmith', 'Ken', 'Smith', 'Scout', 1000000, 2]
moreValues = ['valueOne', 'valueTwo', 'valuethree', 'valueFour', 'valueFive', 'valueSix']

"""
print('+' * 5)
list(zip(keys, values, moreValues))
print(list(zip(keys, values, moreValues)))

print("+" * 7)
list(zip(keys, values))
print(list(zip(keys, values)))

"""

"""
print('+' * 9)
KenSmith = dict(zip(keys, values))
print(KenSmith)
"""

"""
print("+" * 11)
KenSmith.clear()
KenSmith = KenSmith.fromkeys(keys, "Don't know")
print(KenSmith)
"""


#print('+' * 13)
cyborgs = [AnthonySmith, BobSmith, JohnSmith, JoshuaSmith]
#print(cyborgs)



# Extracting first names for cyborgs with fuel capacity above 500000

print('+' * 15)
for cyborg in cyborgs:
    if cyborg['fuelCapacity'] >= 500000:
        print(cyborg['firstName'])

# Extracting all first names
print('+' * 17)
firstNames = [cyborg ['firstName'] for cyborg in cyborgs]
print(firstNames)

# Applying sum() - iterational built-in function
print('+' * 19)
toFuCap = sum(cyborg['fuelCapacity'] for cyborg in cyborgs)
print(toFuCap)

# Filtering out cyborgs with fuel capacity over 1000000
print('+' * 21)
print([cyborg['alias'] for cyborg in cyborgs if cyborg['fuelCapacity'] >= 1000000])

# increase fuel capacity by 5 and print out the first names for the rest
print('+' *23)
print([(cyborg['fuelCapacity'] * 5 if cyborg['function'] == 'Coordinator' else cyborg['firstName']) for cyborg in cyborgs])
#print(cyborgs)

# Filtering out cyborgs with fuel usage equal to 2
print('+' * 25)
currentName = (cyborg['firstName'] for cyborg in cyborgs if cyborg['fuelUsagePerHour'] == 3)
#print(currentName)
print(next(currentName))
