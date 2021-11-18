"""
Boolean operators, выразители предположений

==
!=
<>// Note that != is the same character sequence used by several languages for the not
equal to operator, including Java, C, and C++. Some languages, such as Visual Basic,
use <> as the not equal to operator.
>
<
>=
<=

"""

"""

If (condition):
    command
If statement
condition statement
branch construct
branching statement
decision statement

"""


marsians = float(input("Enter marsians: "))
cyborgs = float(input("Enter cyborgs: "))

print('Hello Earth! This is the beginning of report from Mars.')

#1
if(cyborgs > marsians):
    print('Success! Cyborg shave captivated Mars!')

#2
else:
    print('We are still in the process of captivating Mars.')

print('There are: ', round((marsians/(marsians+cyborgs)*100),2), '% of marsians.')
print ('And: ', round((cyborgs/(marsians+cyborgs)*100),2),'% of cyborgs.')
    
print('End of report, Your cyborgs.')


"""
marsians = float(input("Enter marsians: "))
cyborgs = float(input("Enter cyborgs: "))

print('Hello Earth! This is the beginning of report from Mars.')

#1
if(cyborgs > marsians):
    print('Success! Cyborgs have captivated Mars!')
#2
if (cyborgs < marsians):
    print('We are still in the process of captivating Mars.')
#3
if (cyborgs == marsians):
    print('There is equilibrium between cyborgs abd marsians.')

print('There are: ', round((marsians/(marsians+cyborgs)*100),2), '% of marsians.')
print ('And: ', round((cyborgs/(marsians+cyborgs)*100),2),'% of cyborgs.')

print('End of report, Your cyborgs.')
"""
