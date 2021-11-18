"""
b = ['Timothy', 'Sean', 'Anthony']
order = 0
for human in b:
    print(order, '. ', human, sep = '')
    order = order + 1

b = ['Timothy', 'Sean', 'Anthony', 'Mike']
order = 0
for human in b:
    print(order, '. ', b[order], sep = '')
    order = order + 1
"""

"""
Goal:
    ('firstNameLastName', 'firstNameLastName', 'firstNameLastName', 'firstNameLastName')
"""


firstNames = ['Timothy ', 'Sean ', 'Anthony ', 'Mike ']
lastNames = ['Smith', 'Parker', 'Ivanoff']
temporaryList = []
i = 0
b = 0
c = 0
for item in lastNames:
    for item in firstNames:
        temporaryList.insert(c, firstNames[i] + '_' + lastNames[b])
        i = i + 1
        c = c + 1
    if i >= len(firstNames) - 1:
        b = b + 1
        i = 0
        c = 0
        print(temporaryList)

