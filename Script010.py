"""
String Methods

.capitalize()
.upper()
.lower()
.title()
.swapcase()


.find()
.rfind()
.index()
.rindex()
.replace('x', ''X')

a = "Hit the ball before ball hits you!"
b = a.find('f')
print(b)

a = "Hit the ball before ball hits you!"
b = a.rfind('f')
print(b)

a = "Hit the ball before ball hits you!"
b = a.find('it')
print(b)
c = a.rfind('it')
print(c)

a = "Hit the ball before ball hits you!"
b = a.index('f')
print(b)
c = a.rindex('f')
print(c)

a = "Hit the ball before ball hits you!"
b = a.index('i')
print(b)
c = a.rindex('i')
print(c)

a = "Hit the ball before ball hits you!"
b = a.index('it')
print(b)
c = a.rindex('it')
print(c)

a = "Hit the ball before ball hits you!"
b = a.index('m')
print(b)
c = a.rindex('m')
print(c)
"""


a = "Hit the ball before ball hits you!"
b = a.replace('ball', 'girl')
print(b)

