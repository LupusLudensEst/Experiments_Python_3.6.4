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

if(cyborgs > marsians):
    print('Success! Cyborgs have captivated Mars!')

if (cyborgs < marsians):
    print('We are still in the process of captivating Mars.')

if (cyborgs == marsians):
    print('There is equilibrium between cyborgs abd marsians.')

print('There are: ', round((marsians/(marsians+cyborgs)*100),2), '% of marsians, and: ', round((cyborgs/(marsians+cyborgs)*100),2),'% of cyborgs.')

print('End of report, Your cyborgs.')
