"""
if (condition):
    command
else:
    command
"""

"""
= used in math
== used in logic

if condition:
    command
elif conditionTwo:
    command
elif conditionThree:
    command
elif conditionFour:
    command
else:
    command
"""

"""
and
or
not
"""

"""
if TRUE and TRUE:
    command
"""

"""
passport = str(input("Enter yes if you have a passport, pls: "))
age = int(input("Enter your age: "))

if age >= 16 and passport == 'yes':
    print('Yes. You can travel abroad.')
if age < 16 and passport == 'yes':
    print('Wait till 16 years and get a foreign passport.')
if age >= 16 and passport != 'yes':
    print('Receive your passport.')
"""

"""
if TRUE and TRUE:
    command

if TRUE or TRUE:
    command

if FALSE or TRUE:
    command

if TRUE or FALSE:
    command
if not:
    command
"""

"""
passport = str(input("Enter yes if you have a passport, pls: "))
age = int(input("Enter your age: "))

if passport == 'yes' and age >= 16:
    print('Yes, you can travel abroad')
else:
    print('No, you can not travel abroad')
"""

"""
ticket = str(input("Enter no/yes if you have a ticket, pls: "))
money = str(input("Enter no/yes if you have a money, pls: "))
#1
if ticket == "yes" and money == 'yes':
        print('Yes. You may board the bus.')
#2
if ticket == "no" and money == 'no':
        print('You are not allowed board the bus.')
#3
if ticket == "no" and money == 'yes':
    print('You are not allowed board the bus. Buy the ticket or pay the penalty.')
#4
if ticket == "yes" and money == 'no':
    print('Yes. You may board the bus.')
"""

"""
price = float(input("Enter the price: "))
money = float(input("Enter the money: "))
condition = money >= price
if not condition:
    print('You may board the bus in the rabbit day.')
else:
    print('You may not board the bus in the rabbit day.')
"""

"""
price = float(input("Enter the price: "))
money = float(input("Enter the money: "))
condition = money >= price
if condition:
    print('You may board the bus.')
else:
    print('You do not have enough money.')
"""

"""
marsians = 90
cyborgs = 51

print('Hello Earth! This is the beginning of report from Mars.')

if(cyborgs >= 51):
    print('Success! Cyborgs have captivated Mars!')
elif cyborgs > 41 and cyborgs < 51:
    print('Mission is almost done. We are close to finish it.')
elif cyborgs > 26 and cyborgs <= 41:
    print('Mission is in the progress. We are in the second half of it.')
elif cyborgs > 10 and cyborgs <= 26:
    print('Mission in the progress. We are still in the first half of it.')
elif cyborgs >= 0 and cyborgs <= 10:
    print('Mission is at the beginning yet.')
   
else:
    print('We are still in the process of captivating Mars.')
    
print('End of report, Your cyborgs.')
"""
