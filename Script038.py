# raw_input()-used before 3 version
# input()-modern one, work with strings only

# input()
# int() # transforms into integer

"""
a = int(input('Please, enter a number:'))
b = a + 1
print(b)
"""
"""
a = input('Please, enter a number:')
b = int(a) + 1
print(b)
"""


# cheese = 1000000000000 # it is out of area of program-global
def butterbrott(bread_loaves, butter_gramms, cheese_gramms, sausage_gramms):

    global bread, butter, cheese, sausage # declaring arguments global inside the program
    
    if bread_loaves == 0:
        bread_loaves = int(input("Enter the bread quantity, pls: "))
    bread = (bread_loaves * 15) // 2

 
    if butter_gramms == 0:
        butter_gramms = int(input("Enter the butter amount in gramms, pls: "))
    butter = butter_gramms // 5

    if cheese_gramms == 0:
        cheese_gramms = int(input("Enter the cheese amount in gramms, pls: "))
    cheese = cheese_gramms // 10

    if sausage_gramms == 0:
        sausage_gramms = int(input("Enter the sausage amount in gramms, pls: "))
    sausage = sausage_gramms // 10

    amount = min(bread, butter, cheese, sausage)
    amountmax = max(bread, butter, cheese, sausage)

    return amount, amountmax

print("You will get: ", butterbrott(0, 0, 0, 0), "butterbrodes.")

print(type(butterbrott))

print(' ''Bread:',bread, 'slices'';\n','Butter:',butter,'slices'';\n','Cheese:',cheese,'slices'';\n','Sausage',sausage,'slices''.\n',)


"""
print(type(min)) # area of visioness
print(type(max))
print(type(butterbrott))
print(type(print))
print(type(type))
print(type(cheese))
"""
