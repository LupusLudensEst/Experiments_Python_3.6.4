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


def butterbrott(bread_loaves, butter_gramms, cheese_gramms, sausage_gramms):

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
    return amount
print("You will get: ", butterbrott(20, 0, 0, 0), "butterbodes.")
