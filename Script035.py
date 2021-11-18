# def function_name(argument):

# def=define/declare

"""
c = 2 ** 4
print(c) # output 16

c = 16 ** 0.25
print(c) # output 2.0
"""

"""
def exponentiator(number):
    return number ** 2
print(exponentiator(25))
"""
"""
def taxcalc(number):
    if number <= 1000:
        tax = number * 0.1
    elif number >= 1001 and number <= 5000:
        tax = number * 0.15
    elif number > 5000:
        tax = number * 0.2
    return tax
print(taxcalc(1000))
print(taxcalc(1100))
print(taxcalc(3000))
print(taxcalc(5000))
print(taxcalc(6000))
print('-' * 25)
"""

# I did it myself based on example above
def age_status(age):
    if age > 0 and age <= 12:
        print("This age is of child: ")
    elif age >= 13 and age <= 25:
        print("This age is of young person:")
    elif age >= 26 and age <= 55:
        print("This age is of mature person:")
    elif age >= 56:
        print("This age is of smart long liver:")
    return age
print(age_status(10))
print(age_status(14))
print(age_status(29))
print(age_status(58))
