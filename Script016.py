"""

if (condition):
    command
else:
    command

"""

"""
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

marsians = float(input("Enter marsians: "))
cyborgs = float(input("Enter cyborgs: "))
current_cyborg_ratio = round((cyborgs/(marsians+cyborgs)*100),2)
current_marsians_ratio = round((marsians/(marsians+cyborgs)*100),2)
print('Hello Earth! This is the beginning of report from Mars.')

#1
if cyborgs > marsians:
    print('Success! Cyborgs have captivated Mars!')
#2
elif 41 < current_cyborg_ratio <= 51:
   print('Mission is almost done. We are close to finish it.')
#3
elif 26 < current_cyborg_ratio <= 41:
    print('Mission is in the progress. We are in the second half of it.')
#4
elif 10 < current_cyborg_ratio <= 26:
    print('Mission in the progress. We are still in the first half of it.')
#5
elif 0 <= current_cyborg_ratio <= 10:
    print('Mission is at the beginning yet.')
#6   
else:
    print('We are still in the process of captivating Mars.')

print(f'There are: {current_marsians_ratio} % of marsians.')
print (f'And: {current_cyborg_ratio} % of cyborgs.')
    
print('End of report, Your cyborgs.')

