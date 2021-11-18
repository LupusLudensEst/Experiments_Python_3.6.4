# #Dictionary
# my_dict = {
#     'name':  'Bronx',
#     'age': '2',
#     'occupation': "Corey's Dog"
# }
# for key,val in my_dict.items():
#     # print("My {} is {}.".format(key,val))
#     print(f'My {key} is: {val}\n')
#
# #List. Give me each number in a list squared
# my_list = [1.0, 1.4142135623730951, 1.7320508075688772, 2.0, 2.23606797749979, 2.449489742783178, 2.6457513110645907, 2.8284271247461903, 3.0, 3.1622776601683795]
# squares = [round(num * num, 2) for num in my_list]
# print(f'{squares}')
# # for num in my_list:
# #     print(f'{round(num, 2)} ** {round(num, 2)} = {round(num * num, 2)};')


# #List. Give me of each number square root
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# square_root = [round(num ** 0.5, 2) for num in my_list]
# print(f'{square_root}')
# # for num in my_list:
# #     print(f'Square root from {num} = {round(num ** 0.5, 2)};')

# # Fibonacci generator
# num = int(input("Enter the number: ")) # every next number is the sum of two numbers preceded
# def fib(num):
#     a, b = 0, 1
#     for i in range(0, num):
#         yield "{}:{}".format(i + 1, a)
#         a, b = b, a + b
# for item in fib(num):
#     print(item, end = '; ')

# n = int(input("Enter the number: "))
# def fib(n):
#     a = 0
#     b = 1
#     for i in range(0, n):
#         yield "{}:{}".format(i + 1, a)
#         a, b = b, a + b
#     return a
# for item in fib(n):
#     print(item, end = '; ')

# # Function for nth Fibonacci number
# n = int(input("Enter the number of member: "))
# def fibonacci(n):
#     if n < 0:
#      print("Incorrect input")
#     elif n >= 3:
#         return fibonacci(n-1) + fibonacci(n-2)
#     # member #1 is 1, member #2 is 2
#     elif n == 1 or n == 2:
#         return 1
#     # member #0 is 0
#     else:
#         return 0
# print('Member #', n, 'is:', fibonacci(n),'.')

# # Function for nth Fibonacci number
# n = int(input("Enter the number: "))
# def Fibonacci(n):
#     if n < 0:
#         print("Incorrect input")
#     # First Fibonacci number is 0
#     elif n == 1:
#         return 0
#     # Second Fibonacci number is 1
#     elif n == 2:
#         return 1
#     elif n == 3:
#         return 2
#     else:
#         return Fibonacci(n - 1) + Fibonacci(n - 2) # Fibonacci(n - 1) gives 2 and Fibonacci(n - 2) gives 1, together is 3
# # Driver Program
# print(f'Member # {n} is: {Fibonacci(n)}.')

# #Object Oriented Programming
# class Person(object):
#     def __init__(self, name):
#         self.name = name
#
#     def reveal_identity(self):
#         print("My name is {}".format(self.name))
#
# class SuperHero(Person): # subclass SuperHero inherits all features of superclass Person
#     def __init__(self, name, hero_name):
#         super(SuperHero, self).__init__(name)
#         self.hero_name = hero_name
#
#     def reveal_identity(self):
#         super(SuperHero, self).reveal_identity()
#         print("...And I am {}".format(self.hero_name))
#
# #Instance of class Person
# corey = Person('Corey')
# corey.reveal_identity()
#
# #Instance of class SuperHero
# wade = SuperHero('Wade Wilson', 'Deadpool')
# wade.reveal_identity()

# # Swap 2 varibles
# a = int(input('Enter variable 1: '))
# b = int(input('Enter variable 2: '))
# print("\nBefore swap a = %d and b = %d" %(a, b)) # print("\nBefore swap a = {} and b = {}".format(a, b))
# a, b = b, a # this is core
# print("\nAfter swaping a = %d and b = %d" %(a, b)) # print("\nAfter swaping a = {} and b = {}".format(a, b))

# #Split w. delimeter
# words = 'This is random text we’re going to split apart'
# words2 = words.split(' ')
# print(f'{words2}')

# #Concatenate
# test =  {'2', '1', '3'} # {one_element, another_element} is a set, a collection which is both unordered and unindexed
# s = '; '
# print(s.join(test),';' ,type(s.join(test)))

# test = {'Python', 'Java', 'Ruby'}
# s = '->->'
# print(s.join(test),';' ,type(s.join(test)))

# # #Attributes/methods
# # # Python code for accessing attributes of class
# class emp:
#     name = 'Harsh'
#     salary = '25000'
#
#     def show(self):
#         print (self.name)
#         print (self.salary)
#
# e1 = emp()
# # Use getattr instead of e1.name
# print(getattr(e1, 'name'))
# print(getattr(e1, 'salary'))
#
# # returns true if object has attribute
# print(hasattr(e1, 'name'))
# print(hasattr(e1, 'salary'))
#
# # sets an  attribute
# setattr(e1, 'height', 152)
#
# # returns the value of attribute name height
# print(getattr(e1, 'height'))
#
# # returns the value of attribute name salary
# print(getattr(e1, 'salary'))
#
# # delete the attribute
# delattr(emp, 'salary')
#
# # returns the value of attribute name salary
# print(getattr(e1, 'salary'))

# Python code to reverse a string
# using loop

# def reverse(s):
#     str = "" #declare empthy variable str
#     for i in s:
#         str = i + str
#     return str
#
# s = input('Enter the string: ')
#
# print("The original string  is : ", end="")
# print(s)
#
# print("The reversed string(using loops) is : ", end="")
# print(reverse(s))

# s = str(input('Enter the string: '))
# def reverse_str(s):
#     return s[::-1]
# print(reverse_str(s))

"""
Given even number. Find sum of its digits.
If returned not number, return 'Are the nerdy geek?'
"""

# some_digit = input("Enter the number: ")
# def sum_of_digits(some_number):
#     try:
#         global number_of_digits
#         number_of_digits = len(str(some_number))
#         result = 0
#         for digit in range(number_of_digits):
#             result += int(str(some_digit)[digit])
#         return result
#     except ValueError:
#         return 'Are you the nerdy geek?'
#
# print('Sum of digits: ', sum_of_digits(some_digit))
# print('Quantity of symbols: ', number_of_digits)

"""
Given integer some_digit. Return MAX number containing
exactly some_digit digits
"""

# def largest_number(some_digit):
#     return 10 ** some_digit - 1
#
# some_digit = int(input("Enter the number: "))
#
# print('Largest number is: ', largest_number(some_digit),'.')
# print('Lenght of the number is: ', len(str(10 ** some_digit - 1)), '.')
