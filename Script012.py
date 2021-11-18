"""
String Methods

string.capitalize()
string.upper()
string.lower()
string.title()
string.swapcase()

string.find()
string.rfind()
string.index()
string.rindex()
string.replace('x', ''X')
string.split('A', 1)

"""

#Example 1:
    
list = ['Let', 'there', 'be', 'the light!']
variable = " ".join(list)
print(variable)

list = ['Let', 'there', 'be', 'the light!']
variableOne = " "
variableTwo = variableOne.join(list)
print(variableTwo)

string = " "
list = ["a", "b", "c"]
print(string.join(list))

listOne = ["a", "b", "c"]
listOne = " "
listTwo = listOne.join(list)
print(string.join(list))

