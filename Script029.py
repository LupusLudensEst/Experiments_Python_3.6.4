"""
Goal:
    ('firstNameLastName', 'firstNameLastName', 'firstNameLastName', 'firstNameLastName')
"""

"""
Output to files

File object

file object = open(file_name [, access_mode][, buffering])

File open modes in Python:

Mode  Read? Write? Overwrites  Creates new file 
                   existing    if file does not
                   file?       exist?

r       Y     N      N            N               
rb      Y     N      N            N               

r+      Y     Y      N            N               
rb+     Y     Y      N            N               

w       N     Y      Y            Y               
wb      N     Y      Y            Y               

w+      Y     Y      Y            Y               
wb+     Y     Y      Y            Y               

a       N     Y      N            Y               
ab      N     Y      N            Y               

a+      Y     Y      N            Y               
ab+     Y     Y      N            Y 
"""

"""
workFile = open('superFile.txt', 'r')
print('Done. Well done!')

workFile = open('superFile.txt', 'r+')
print('Done. Well done!')

workFile = open('superFile.txt', 'w')
print('Done. Well done!')

workFile = open('superFile.txt', 'w+')
print('Done. Well done!')

workFile = open('superFile.txt', 'a')
print('Done. Well done!')

workFile = open('superFile.txt', 'a+')
print('Done. Well done!')

"""

"""
workFile = open('superFile.txt', 'a')
workFile.write("This is my first line.")
workFile.write("\n")
#workFile.write("This is my second line.")
workFile.close()
print('Done.')
"""

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

"""
Dictionaries in Python
Sequence of key-value pairs

Model:
d = {'key': 'value', 'nextKey': 'value', 'anotherKey': 'value'}

Advantage of dictionaries:
-Easier search, extraction and update of data
-Dictionaries cab be used as databases
-Plenty of effective dictionary methods

How to initialize/create a dictionary:
d = {}

or

d = {'key': 'value', 'nextKey': 'value', 'anotherKey': 'value'}
E.g.
"""

"""
d = {'alias': 'John Smith', 'firstName': 'John', 'familyName': 'Smith'}
print(d)

c = {'key': 'value', 'nextKey': 'value', 'anotherKey': 'value'}
print (c)
"""

"""
#or
#d = dict(key=value, nextKey=value, anotherKey=value)
d = dict(alias='JohnSmith', firstName='John', familyName="Smith")
print(d)
"""
"""
d = dict.fromkeys(['key', 'nextKey', 'anotherKey'])
print(d)
"""

"""
d = dict.fromkeys(['alias', 'firstName', 'familyName'])
print(d)
"""

"""
#d = {key: value for expression}
d = {a: 'abc' for a in range (5)}
print(d)
"""

"""
d = {anyKey: 10 for anyKey in range (5)}
print(d)

d = {anyKey: anyKey + 1 for anyKey in range (5)}
print(d)

d = {a: a + a for a in range (5) }
print(d)

d = {a: a - 1 for a in range (5) }
print(d)

d = {a: a -a for a in range (5)}
print(d)

d = {a: a ** 2
     for a in range (5)}
print(d)

d = {a: a / 2
     for a in range (5)}
print(d)

#Adiing values to existing dictionary
#d[key] = value

d = {0: 1, 1: 2, 2: 3, 3:4, 4:5}
d[5] = 6
print(d)

#d.update(otherDictionary)
d = {0: 1, 1: 2, 2: 3, 3:4, 4:5}
d[5] = 6

dd = {6:7, 7:8}
d.update(dd)
print(d)
"""

"""
d = {0: 1, 1: 2, 2: 3, 3:4, 4:5}
d[5] = 6

dd = {6:7, 7:8}
d.update(dd)

ddd = {a: a + 1 for a in range (8, 15)}
d.update(ddd)

print(d)
"""

"""
# Create a mapping of country to capital
asia = {
    'Azerbajan': 'Baku',
    'Armenia': 'Yerevan',
    'Afganistan': 'Kabul',
}



# Create a mapping of capital to population
population = {
    'Baku': 2137000,
    'Yerevan': 1060000,
    'Kabul': 3000000,
}
"""

"""
# Adding some more population info (about Bangladesh and bahrain)
population['Dhaka'] = 18000000
population['Manama'] = 157000



# Printing out some population info
print('+' * 5)
print("Baku has the population of:", population['Baku'])
print("Erevan has the population of:", population['Yerevan'])



# Printing out info about the capital cities
print('+' * 5)
print("Azerbajan's capital is:", asia['Azerbajan'])
print("Armenia's capital is:", asia['Armenia'])


# Prining out the info about the population of capitals without mentioning the capitals

print('+' *5)
print("Azerbajan's capital has the population of:", population[asia['Azerbajan']])
print("Armenia's capital has the population of:", population[asia['Armenia']])


#dict.items()
# %s deviding on module and symbol of substitution

# Print every Asian country's capital
print('+' * 5)
for country, capital in asia.items():
    print("%s's capital %s'" % (country, capital))
#   print("%s capital is %s" % (country, capital))

# printing every Asian capital's population
print('+' * 5)
for capital, number in population.items():
    print("%s has the population of %s" % (capital, number))


# Now printing both pieces of information at the same time
print('+' * 5)
for country, capital in asia.items():
    print( "%s has the capital of %s with the population of %s" % (country, capital, population[capital]))

"""


# Create a mapping of country to capital
asia = {
    'Azerbajan': 'Baku',
    'Armenia': 'Yerevan',
    'Afganistan': 'Kabul',
    }



# Create a mapping of capital to population
population = {
    'Baku': 2137000,
    'Yerevan': 1060000,
    'Kabul': 3000000,
    }


""" 
Methods:

Clearing dictionary
dict.clear()
""" 

"""  
print('+' * 5)
population.clear()
print(population)
""" 



""" 
# Method.copy - creating a copy of the dictionary
# dict.copy()

print('+' * 5)
countriesOfAsia = asia.copy()
print(asia)
print(countriesOfAsia)
""" 

"""
# Method. keys - extracting only the keys from the dictionary
# dict.keys()
print('+' *5)
#print(asia.keys())
asiaclone = asia.keys()
print(asiaclone)
"""

"""
# Method. values - extracting only the values from the dictionary
# dict.values()
print('+' *5)
print(asia.values())

asiavalues = asia.values()
print(asiavalues)
"""

# Method.get - extracting key-value pairs and doing some actions in case if the value pairs are missing
""" 
print('+' * 5)
countryOne = asia.get('Azerbajan')
print(countryOne)

countryOne = asia.get('Tokyo')
print(countryOne)
"""

"""
# Using the .get method with 'if'

print('+' *5)
# he case when the country is not listed:
country = asia.get('Armenia')

if not country:
    print("Sorry, no info about this country")

if country:
    print(country)
"""


# key.value
# Adding lists as values - not always a good idea
# dict = {'key': [value, value, value], 'key2': [value, value, value]}
print('+' * 5)
citiesOfFrance = {'city': ['Paris', 'Marseille', 'Lyon'], 'population': ['3M', '2M', '1M']}
#print(citiesOfFrance)


# or
print(citiesOfFrance['city'][0])
print(citiesOfFrance['population'][0])



# or
print('+' * 5)
print(citiesOfFrance['city'][0], citiesOfFrance['population'][0])


# And here is why it is not always a good idea to include lists into dictionary
print('+' *5)
for city, population in citiesOfFrance.items():
    print("%s has the population of %s" % (city, population))

# This a way that would be much better
citiesofFrance = {'Paris': '3M', 'Marsellie': '2M', 'Lyon': '1M'}
for city, population in citiesofFrance.items():
    print("%s has the population of: %s" % (city, population))
    
