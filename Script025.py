"""
Course of programming "Lazy Python"
Lesson #25. Search on Youtube: ЛП0025
Link on playlist Youtube: bit.ly/lenivii
Link on blog: lenivii. wordpress.com
"""

"""
Goal:
    ('firstNameLastName', 'firstNameLastName', 'firstNameLastName', 'firstNameLastName')
"""

"""
1. Input;
2. Processing;
3. Output;

Output to files

File object

file_object = open(file_name [, access_mode][, buffering])

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

workFile = open('superFile.txt', 'a')
workFile.write("This is my first line.")
workFile.write("\n")
workFile.write("This is my second line.")
workFile.write("\n")
workFile.write("This is my third line.")
workFile.write("\n")
workFile.close()
print('Done.')
