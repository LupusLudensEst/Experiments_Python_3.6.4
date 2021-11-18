"""
Lists
list = [item1, item2, item3, item4]
listTwo = [item7, item9, item15, item16]
listthree = [list, listTwo, listThree]
"""

"""
bobSmith = ['Bob', 'Smith', 'Coordinator', 1000000, 1, 0, 0, 20, 'yes', 1000, 100]
marthaSmith = ['Martha', 'Smith', 'Infector', 500000, 2, 1000, 10, 15, 'no', 0, 0]
johnSmith = ['John', 'Smith', 'Soldier', 500000, 2, 0, 0, 20, 'yes', 2000, 200]
smithBrigade = [bobSmith, marthaSmith, johnSmith]
#print(smithBrigade)

robTrump = ['Rob', 'Trump', 'Technician', 500000, 3, 1000, 20, 15, 'yes', 1000,	100]
suziTrump = ['Suzi', 'Trump', 'Scout', 1000000,	2, 0, 0, 30, 'yes', 1000, 100]
hulkTrump = ['Hulk', 'Trump', 'Construction worker', 500000, 3, 1500, 40, 10, 'no', 0, 0]
trumpBrigade = [robTrump, suziTrump, hulkTrump]
#print(trumpBrigade)

print(smithBrigade, trumpBrigade )
"""

"""
b = ['text', 10, 'oneMoreText', 1.5]
for a in b:
    print(a)



b = ['text', 10, 'oneMoreText', 1.5]
for fragment in b:
    print(fragment)



superList = ['super', 'evenMoreSuper', 'theSuperest']
for super in superList:
    print(super)
"""


firstnames = ['Anthony', 'Timothy', 'Bob', 'Sean', 'John']
lastnames = ['Smith', 'Parker', 'Conrad', 'Washington', 'Kennedy']
temporarylist = []
i = 0
b = 0
c = 0
for item in lastnames:
    for item in firstnames:
        temporarylist.insert(c, firstnames[i] + '_' + lastnames[b])
        i = i + 1
        c = c + 1
    if i > len(firstnames) - 1:

        # New block 1. Now writing current family name to Families.txt
        file = open("Families.txt", 'a')
        file.write(lastnames
        [b] + '\n')
        file.close()

        # New block 2. Now writing chain of cyborg-names to Smith.txt, Parker.txt, etc.
        print(lastnames[b], ' = ', temporarylist)
        file = open(lastnames[b] + ".txt", 'w')
        temporarylist = str(temporarylist)
        file.write(temporarylist)
        temporarylist = []
        file.close()

        b = b + 1
        i = 0
        c = 0



"""
Smith  =  ['AnthonySmith', 'TimothySmith', 'BobSmith', 'SeanSmith', 'JohnSmith']
Parker  =  ['AnthonyParker', 'TimothyParker', 'BobParker', 'SeanParker', 'JohnParker']
Conrad  =  ['AnthonyConrad', 'TimothyConrad', 'BobConrad', 'SeanConrad', 'JohnConrad']
Washington  =  ['AnthonyWashington', 'TimothyWashington', 'BobWashington', 'SeanWashington', 'JohnWashington']
Kennedy  =  ['AnthonyKennedy', 'TimothyKennedy', 'BobKennedy', 'SeanKennedy', 'JohnKennedy']

cyborgsTeam = [Smith, Parker, Conrad, Washington, Kennedy]
lenghtAll = len(Smith) + len(Parker) + len(Conrad) + len(Washington) + len(Kennedy)
lenght = len(cyborgsTeam)

print('CyborgsTeams total: ', lenght, ';', 'Total in all teams: ', lenghtAll, ';', cyborgsTeam)
"""
