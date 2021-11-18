"""
Goal:
    ('firstNameLastName', 'firstNameLastName', 'firstNameLastName', 'firstNameLastName')
"""

"""
Output to files

File object

file object = open(file_name [, access_mode][, buffering])

File open modes in Python:

Mode  Read? Write? Overwrites  Creates new file    Where is the cursor?
                   existing    if file does not
                   file?       exist?

r       Y     N      N            N               Beginning              
rb      Y     N      N            N               Beginning               

r+      Y     Y      N            N               Beginning                 
rb+     Y     Y      N            N               Beginning             

w       N     Y      Y            Y               Beginning                 
wb      N     Y      Y            Y               Beginning                 

w+      Y     Y      Y            Y               Beginning                
wb+     Y     Y      Y            Y               Beginning                 

a       N     Y      N            Y               End               
ab      N     Y      N            Y               End               

a+      Y     Y      N            Y               End               
ab+     Y     Y      N            Y               End 
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

#Creates commands based on lastnames and firstnames
firstNames = ['Anthony', 'Timothy', 'Sean', 'John']
lastNames = ['Smith', 'Parker', 'Conrad', 'Washington', 'Kennedy']
temporaryList = []
a = 0
b = 0
c = 0
for item in lastNames:
    for item in firstNames:
        temporaryList.insert(c, lastNames[b] + '_' + firstNames[a])
        a = a + 1
        c = c + 1
    if a > len(firstNames) - 1:
        
        
        # New block 1. Now writting current family name to Families.txt
        file = open("Families.txt", 'a') #a - append to the file
        file.write(lastNames[b] + '\n')
        file.close()

        # New block 2. Now writting chain of cyborg-names to Smith.txt, Parker.txt, etc.
        print(lastNames[b], ' = ', temporaryList)
        file =open(lastNames[b] + ".txt", 'w') #w - rewrite in the file
        temporaryList = str(temporaryList)
        file.write(temporaryList)
        temporaryList = []
        file.close()

        b = b +1
        a = 0
        c = 0     
        
print('Done.', 'Files created')
