# Double key (double index)

"""
AnthonySmith = {'alias': 'AnthonySmith', 'firstName': 'Anthony', 'familyName': 'Smith', 'function': 'Coordinator', 'fuelCapacity': 1000000, 'fuelUsagePerHour': 2}

print(AnthonySmith)
print('_' *30)
"""

"""
AnthonySmith = {'alias': 'AnthonySmith',
'name':{'first': 'Anthony', 'family': 'Smith'},
'function': 'Coordinator',
'fuel':{'capacity': 1000000, 'fuelUsagePerHour': 2}}

print(AnthonySmith)
print('_' *30)

name = AnthonySmith['name']
print(name)
print('_' *30)


firstName = AnthonySmith['name']['first']
print(firstName)
print('_' *30)


family = AnthonySmith['name']['family']
print(family)
print('_' *30)

BobSmith = {'alias': 'BobSmith',
'name':{'first': 'Bob', 'family': 'Smith'},
'function': 'Infector',
'fuel': {'capacity': 500000, 'fuelUsagePerHour': 2}}

BillSmith = {'alias': 'BillSmith',
'name':{'first': 'Bill', 'family': 'Smith'},
'function': 'Soldier',
'fuel': {'capacity': 500000, 'fuelUsagePerHour': 2}}

brigade = [AnthonySmith, BobSmith, BillSmith]
print(brigade)
print('_' *30)
"""


# []-for list/список
# {}-for dictionary/словарь


"""
# Increase fuel reserve by two times for all the cyborgs in the brigade

AnthonySmith = {'alias': 'AnthonySmith',
'name':{'first': 'Anthony', 'family': 'Smith'},
'function': 'Coordinator',
'fuel':{'capacity': 1000000, 'fuelUsagePerHour': 2}}

BobSmith = {'alias': 'BobSmith',
'name':{'first': 'Bob', 'family': 'Smith'},
'function': 'Infector',
'fuel': {'capacity': 500000, 'fuelUsagePerHour': 2}}

BillSmith = {'alias': 'BillSmith',
'name':{'first': 'Bill', 'family': 'Smith'},
'function': 'Soldier',
'fuel': {'capacity': 500000, 'fuelUsagePerHour': 2}}

brigade = [AnthonySmith, BobSmith, BillSmith]
print(brigade)
print('_' *30))

for cyborg in brigade:
        # cyborg['fuel']['capacity'] = cyborg['fuel']['capacity'] * 0.93333333333333
          cyborg['fuel']['capacity'] *= 0.93         
print(brigade)
print('_' *30) 
"""


"""
# Increase fuel reserve by two times for all the cyborgs in the brigade

AnthonySmith = {'alias': 'AnthonySmith',
'name':{'first': 'Anthony', 'family': 'Smith'},
'function': 'Coordinator',
'fuel':{'capacity': 1000000, 'fuelUsagePerHour': 2}}

BobSmith = {'alias': 'BobSmith',
'name':{'first': 'Bob', 'family': 'Smith'},
'function': 'Infector',
'fuel': {'capacity': 500000, 'fuelUsagePerHour': 2}}

BillSmith = {'alias': 'BillSmith',
'name':{'first': 'Bill', 'family': 'Smith'},
'function': 'Soldier',
'fuel': {'capacity': 500000, 'fuelUsagePerHour': 2}}

brigade = [AnthonySmith, BobSmith, BillSmith]
print(brigade)
print('_' *30)

for cyborg in brigade:
    if cyborg['name']['first'] == 'Anthony':
        cyborg['fuel']['capacity'] = cyborg['fuel']['capacity'] * 3.33
print(brigade)
"""       

# Deleting elements from dictionary

# In case with a simple dictionary


"""
AnthonySmith = {'alias': 'AnthonySmith', 'firstName': 'Anthony', 'familyName': 'Smith', 'function': 'Coordinator', 'fuelCapacity': 1000000, 'fuelUsagePerHour': 2}
print(AnthonySmith)
print('_' *30)

del AnthonySmith['fuelCapacity']
print(AnthonySmith)
print('_' *30)
"""

"""
# Deleting elements from dictionary

# In case with aan embedded dictionaries

AnthonySmith = {'alias': 'AnthonySmith',
'name': {'first': 'Anthony', 'family': 'Smith'},
'function': 'Coordinator',
'fuel': {'capacity': 1000000, 'fuelUsagePerHour': 2}}
print(AnthonySmith)
print('_' *30)

del AnthonySmith['fuel']['capacity']
print(AnthonySmith)
print('_' *30)
"""

# Deleting elements from dictionary

# In case with embedded dictionaries inside the list

AnthonySmith = {'alias': 'AnthonySmith',
'name': {'first': 'Anthony', 'family': 'Smith'},
'function': 'Coordinator',
'fuel': {'capacity': 1000000, 'fuelUsagePerHour': 2}}

BobSmith = {'alias': 'BobSmith',
'name':{'first': 'Bob', 'family': 'Smith'},
'function': 'Infector',
'fuel': {'capacity': 500000, 'fuelUsagePerHour': 2}}

BillSmith = {'alias': 'BillSmith',
'name':{'first': 'Bill', 'family': 'Smith'},
'function': 'Soldier',
'fuel': {'capacity': 500000, 'fuelUsagePerHour': 2}}

brigade = [AnthonySmith, BobSmith, BillSmith]
print(brigade)
print('_' *30)

for cyborg in brigade:
    del cyborg['fuel']['capacity']
print(brigade)
print('_' *30)

