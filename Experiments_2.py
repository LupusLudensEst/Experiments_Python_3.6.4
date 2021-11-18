"""
def toJadenCase(string):
    return " ".join(w.capitalize() for w in string.split())


import string
def toJadenCase(NonJadenStrings):
    return string.capwords(NonJadenStrings)


import string
toJadenCase = string.capwords


from string import capwords as toJadenCase


import string
def toJadenCase(string1):
    return string.capwords(string1)


def toJadenCase(string):
  return ' '.join(x.capitalize() for x in string.split())


def toJadenCase(string):
    # ...
    sentence = ''
    words = []
    st = string.split()
    for i in st:
        il = list(i)
        il[0] = il[0].upper()
        words.append(''.join(il))
    return ' '.join(words)


def toJadenCase(string):
    return " ".join([x.capitalize() for x in string.split(" ")])



   def toJadenCase(string):
    return " ".join( map( lambda x: x.capitalize() , string.split(' ') ) )


   from string import capwords
def toJadenCase(string):
  return capwords(string, " ")



import string

def toJadenCase(tweet):
    # using import string cap words does it all for you (split, capitalize, join)
    return string.capwords(tweet)


def toJadenCase(string):
    return " ".join(x[0].upper()+x[1:] for x in string.split(" "))


import string
def toJadenCase(stuff):
    return string.capwords(stuff)
"""

# print("Count sum.")
# def get_sum(a, b):
#     return a + b
# a = float(input("Enter A: "))
# b = float(input("Enter B: "))
# print(f'Summ: {get_sum(a, b)}')

# print("Sum")
# a = float(input("A: "))
# b = float(input("B: "))
# print("Sum A + B: ", a + b)

# print('Enter your sex, pls. M if male and F if female.')
# p = str(input());
# if p == 'M':
#     print('Hello, dude!')
#     quit()
# elif p == 'F':
#     print('Hello, beauty!')
#
# else:
#     print('Who are you?')
#
# print('What is up?')
# k = str(input());
# if k == 'Ok':
#     print('Ok is Ok. That is standard!))')
#
# elif k == 'Not good':
#     print('Do not upset, rise up)) ')
#
# elif k == 'Excellent':
#     print('You are good!!!')
#
# elif k == 'Exctrasuper':
#     print('Hmmm...')
#
# else:
#     print('Let is drink?')
#
# import time
#
# time.sleep(5)

# a=2
# b=5
# t1=a
# a=b
# b=t1
#
# t1=a
# t2=b
# a,b=t2,t1
#
# a,b=b,a

# a=a+b # 2+5=7
# b=a-b # 7-5=2
# a=a-b # 7-2=5
# print(f'{a}\n{b}')

# # Dictionary
# my_dict={'name': 'Bronx', 'age': '2', 'occupation': "Corey's dog"}
# for key,val in my_dict.items():
#     print("My {} is {}".format(key,val))
#
# # List. Give me each number in list squared
# my_list=[1,2,3,4,5,6,7,8,9,10]
# squares=[num*num for num in my_list]
# print(F'{squares}')

# # Fibonacci generator
# num=int(input("Enter the number: "))
# def fib(num):
#     a,b=0,1
#     for i in range(0,num):
#         yield"{}:{}".format(i+1,a)
#         a,b=b,a+b
#     return a
# for item in fib(num):
#     print(item)

# # Function for nth member of Fibonacci row
# n=int(input("Enter the number of member: "))
# def fib(n):
#     if n<0:
#         print("Incorrect input")
#     elif n>=3:
#         return fib(n-1)+fib(n-2)
#     # member #1 is 1, member #2 is 1
#     elif n==2 or n==1:
#         return 1
#     # member #0 is 0
#     else:
#         return 0
# print("Member #", n, "is :", fib(n), '.')

# n=int(input("Enter the number of member: "))
# def fib(n):
#     if n<0:
#         print("Incorrect input")
#         # First Fibonacci number is 0
#     elif n==1:
#         return 0
#     # Second Fibonacci number is 1
#     elif n==2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# print("Member #", n, "is", fib(n), ".")

# Object oriented programming
# class Person(object):
# #     def __init__(self, name):
# #         self.name=name
# #
# #     def reveal_identity(self):
# #         print("My name is: {}".format(self.name))
# #
# # class SuperHero(Person):
# #     def __init__(self, name, hero_name):
# #         super(SuperHero, self).__init__(name)
# #         self.hero_name=hero_name
# #
# #     def reveal_identity(self):
# #         super(SuperHero, self).reveal_identity()
# #         print("...And I am: {}".format(self.hero_name))
# #
# # # Instance of class Person
# # corey=Person(input("Enter the name: "))
# # corey.reveal_identity()
# #
# # # Instance of class SuperHero
# # wade=SuperHero(input("Enter the SuperHero function: "), input("Enter the what is he doing: "))
# # wade.reveal_identity()

# a=2
# b=5
# print(f"a and b before swap {a}, {b}")
# # t1=a
# # a=b
# # b=t1
# a=a+b
# b=a-b
# a=a-b
# print(f"a and b after swap {a}, {b}")

# Splitting the text
# words='This string would be splitted down'
# words_splitted=words.split(' ')
# print(f'Before split: {words},\nafter split: {words_splitted}')

# Concatenate
# test_0={'2','1','3'}
# s=', '
# print(s.join(test_0))
#
# test_1={'Python','Java','Ruby'}
# s='->->'
# print(s.join(test_1))

# Python code for accessing attributes of class
# class emp:
#     name='Harsh'
#     salary='25000'
#
#     def show(self):
#         print(self.name)
#         print(self.salary)
#
# e1=emp()
# # Use getattr instead of e1.name
# print(getattr(e1, 'name'))
#
# # returns true if object has attribute
# print(hasattr(e1, 'name'))
#
# # sets an attribute
# setattr(e1, 'height', 152)
#
# # returns the value of attribute name height
# print(getattr(e1, 'height'))
#
# # delete the attribute
# delattr(emp, 'salary')

# Python code to reverse a string using loop
# def reverse(s):
#     str=""
#     for i in s:
#         str=i+str
#     return str
#
# s="Gurov Vic"
#
# print("The original string is :", end=" ")
# print(s)
#
# print("The reversed string is :", end=" ")
# print(reverse(s))

"""
If
    example_list=[1,2,3,1]
go to
    contains_duplicates(example_list)=True

If
    example_list=[1,5995,0,7]
go to
    contains_duplicates(example_list)=False

If
    example_list=[]
go to
    contains_duplicates(example_list)=False 
"""


# days_week = int(input('Input days in week: '))
# day_sec = 86400
# week_sec = day_sec * days_week
# print(week_sec)

# def area_triangle(base, height):
#     return base*height/2
# area_1 = area_triangle(float(input('Input the base 1: ')), float(input('Input the height 1: ')))
# area_2 = area_triangle(float(input('Input the base 2: ')), float(input('Input the height 2: ')))
# sum = area_1 + area_2
# print(f'The common area is: {sum}')

# name = str(input("Input the name: "))
# number = float(len(name)) * 9
# print(f"Hello {name}. Your lucky number is: {number}.")

# def lucky_num(name):
#     num = float(len(name)) * 9
#     print(f"Hello {name}. Your lucky number is: {num}.")
#
# lucky_num("Kay")
# lucky_num(str(input("Input the name: ")))

# def print_monthly_expense(month, hours):
#     expenses = round((hours * 0.65),2)
#     print(f'In {month} we had {hours} hours and spent: ${expenses}.')
#
# print_monthly_expense('June', 243)
# print_monthly_expense('July', 325)
# print_monthly_expense('August', 298)

# def print_monthly_expense(month, hours):
#     expenses = round((hours * 0.65), 2)
#     print("In " + month + " we spent: " + str(expenses))
#
# print_monthly_expense('June', 243)
# print_monthly_expense('July', 325)
# print_monthly_expense('August', 298)

# def print_monthly_expense(month, hours):
#     expenses = hours * 0.65
#     print("In " + month + " we spent: " + str(expenses))
#
# print_monthly_expense('June', 243)
# print_monthly_expense('July', 325)
# print_monthly_expense('August', 298)

# def convert_distance(miles):
#     km = miles * 1.6
#     return km
# result = convert_distance(55)
# print("The distance in Kilometers is " + str(result))
# print("The round-trip in Kilometers is " + str(result*2))

# # 1) Complete the function to return the result of the conversion
# def convert_distance(miles):
# 	km = miles * 1.6  # approximately 1.6 km in 1 mile
#
# my_trip_miles = 55
#
# # 2) Convert my_trip_miles to kilometers by calling the function above
# my_trip_km = ___
#
# # 3) Fill in the blank to print the result of the conversion
# print("The distance in kilometers is " + ___)
#
# # 4) Calculate the round-trip in kilometers by doubling the result,
# #    and fill in the blank to print the result
# print("The round-trip in kilometers is " + ___)

# # This function compares two numbers and returns them
# # in increasing order.
# def order_numbers(number1, number2):
# 	if number2 > number1:
# 		return number1, number2
# 	else:
# 		return number2, number1
#
# # 1) Fill in the blanks so the print statement displays the result
# #    of the function call
# smaller, bigger = order_numbers(100, 99)
# print(smaller, bigger)

# print(10>1)
#
# print(10<1)
#
# print("Cat"=="Dog")
#
# print("Cat"!="Dog")
#
# print(type(10))
#
# print(type('Str'))

# def hint_user_name(user_name):
#     if len(user_name) < 3:
#         print("Invalid username. It should be at least 3 symbols long")
#     elif len(user_name) > 15:
#         print("Invalid username. It should be at most 15 symbols long")
#     else:
#         print("Valid username.")
# hint_user_name(str(input("Enter the user name: ")))

# def calculate_storage(filesize):
#     block_size = 4096
#     full_blocks = filesize // block_size
#     partial_block = filesize % block_size
#     if partial_block > 0:
#         return (full_blocks + 1) * block_size
#     return filesize
#
# print(calculate_storage(1))    # Should be 4096
# print(calculate_storage(4096)) # Should be 4096
# print(calculate_storage(4097)) # Should be 8192
# print(calculate_storage(6000)) # Should be 8192

# def color_translator(color):
# 	if color == "red":
# 		hex_color = "#ff0000"
# 	elif color == "green":
# 		hex_color = "#00ff00"
# 	elif color == "blue":
# 		hex_color = "#0000ff"
# 	else:
# 		hex_color = "unknown"
# 	return (str(hex_color))
#
# print(color_translator("blue")) # Should be #0000ff
# print(color_translator("yellow")) # Should be unknown
# print(color_translator("red")) # Should be #ff0000
# print(color_translator("black")) # Should be unknown
# print(color_translator("green")) # Should be #00ff00
# print(color_translator("")) # Should be unknown

# print("big" > "small")

# print(11 % 5)

# def format_name(first_name, last_name):
#     # code goes here
#     if first_name and last_name:
#         return 'Name: ' + last_name + ", " + first_name + ''
#     elif first_name or last_name:
#         return 'Name: ' + first_name + last_name + ''
#     else:
#         return ('')
#     return string
#
#
# print(format_name("Ernest", "Hemingway"))
# # Should return the string "Name: Hemingway, Ernest"
#
# print(format_name("", "Madonna"))
# # Should return the string "Name: Madonna"
#
# print(format_name("Voltaire", ""))
# # Should return the string "Name: Voltaire"
#
# print(format_name("", ""))
# # Should return an empty string


# Should return an empty string

# def sum(x, y):
# 		return(x+y)
# print(sum(sum(1,2), sum(3,4)))

# print(((10 >= 5*2) and (10 <= 5*2)))

# def fractional_part(numerator, denominator):
# 	# Operate with numerator and denominator to
# # keep just the fractional part of the quotient
#     if denominator != 0:
#         return (numerator % denominator)/denominator
#     else:
#         return (0)
#
# print(fractional_part(5, 5)) # Should be 0
# print(fractional_part(5, 4)) # Should be 0.25
# print(fractional_part(5, 3)) # Should be 0.66...
# print(fractional_part(5, 2)) # Should be 0.5
# print(fractional_part(5, 0)) # Should be 0
# print(fractional_part(0, 5)) # Should be 0

# x = 0
# while x < 5:
#     print("Not there yet, x=" + str(x))
#     x = x + 1
# print("x=" + str(x))

# def attempts(n):
#     x = 1
#     while x <= n:
#         print("Attempt " + str(x))
#         x += 1
#     print("Done")
#
# attempts(int(input("Input the integer: ")))

# def count_down(start_number):
#   current = start_number
#   while (current > 0):
#     print(current)
#     current -= 1
#   print("Zero!")
#
# count_down(int(input("Input the integer: ")))

# def smallest_prime_factor(x):
#     """Returns the smallest prime number that is a divisor of x"""
#     # Start checking with 2, then move up one by one
#     n = 2
#     while n <= x:
#         if x % n == 0:
#             return n
#         n += 1
#
#
# print(smallest_prime_factor((int(input("Input the integer: "))))) # if 12 output should be 2
# print(smallest_prime_factor((int(input("Input the integer: "))))) # if 15 output should be 3

# def print_prime_factors(number):
#   # Start with two, which is the first prime
#   factor = 2
#   # Keep going until the factor is larger than the number
#   while factor <= number:
#     # Check if factor is a divisor of number
#     if number % factor == 0:
#       # If it is, print it and divide the original number
#       print(factor)
#       number = number / factor
#     else:
#       # If it's not, increment the factor by one
#       factor += 1
#   return "Done"

# print_prime_factors(int(input("Input the integer: ")))
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT

# def is_power_of_two(n):
#     # Check if the number can be divided by two without a remainder
#     while n != 0 and n % 2 == 0:
#         n = n / 2
#     # If after dividing by two the number is 1, it's a power of two
#     if n == 1:
#         return True
#     return False
#
#
# print(is_power_of_two(0))  # Should be False
# print(is_power_of_two(1))  # Should be True
# print(is_power_of_two(8))  # Should be True
# print(is_power_of_two(9))  # Should be False

# def sum_divisors(n):
#   sum = 0
#   # Return the sum of all divisors of n, not including n
#   for i in range(1,n-1):
#     if(n%i==0):
#         sum=sum+i
#   return sum
#
# print(sum_divisors(0))
# # 0
# print(sum_divisors(3)) # Should sum of 1
# # 1
# print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# # 55
# print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# # 114

# for i in range (5):
#     print(i)

# def square(n):
#     return n*n

# def sum_squares(x):
#     sum = 0
#     for n in range(x):
#         sum += n*n
#     return sum
#
# print(sum_squares(int(input("Input the integer: ")))) # Should be 285

# friends = ['Taylor', 'Alex', 'Pat', 'Ali']
# for friend in friends:
#     print(f'Hi, {friend}')

# values = [23, 52, 59, 37, 48]
# sum = 0
# length = 0
# for value in values:
#     sum += value
#     length += 1
# print(f'Total sum: {str(sum)} - Average: {str(sum/length)}')
# print('Total sum: ' + str(sum) + ' - Average: ' + str(sum/length))

# product = 1
# # for n in range(1, 10):
# #     product = product * n
# #
# # print(product)

# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
#
# print(factorial(int(input("Input the integer: ")))) # 4 should return 24
# print(factorial(int(input("Input the integer: ")))) # 4 should return 120

# def to_celsius(x):
#     return(x-32)*5/9
#
# for x in range(0, 101, 10):
#     print(x, round((to_celsius(x)), 2))

# for left in range(7):
#     for right in range(left, 7):
#         print("[" + str(left) + "|" + str(right) + "]", end=" " )
#     print()

# teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
# for home_team in teams:
#     for away_team in teams:
#         if home_team != away_team:
#             print(f"{home_team} vs {away_team}")

# def factorial(n):
#     result = 1
#     for x in range(1, n + 1):
#         result = result * x
#     return result
# print(factorial(int(input("Input the integer: "))))

# def factorial(n):
# #     result = 1
# #     for x in range(1, n + 1):
# #         result = result * x
# #     return result
# #
# # for n in range(0, 10):
# #     print(n, factorial(n))

# for i in range(1,11):
#   print(i, i**3)

# # Returns count of all numbers
# # smaller than or equal to n
# # and multples of 7
# def countMultiples(n):
#   result = 0;
#   for i in range(1, n + 1):
#     if i % 7 == 0:
#       result += 1;
#   return result;
# for n in range(0, 101):
#   if n % 7 == 0:
#     print(countMultiples(n), n)

# def retry(operation, attempts):
#   for n in range(attempts):
#     if operation():
#       print("Attempt " + str(n) + " succeeded")
#       break
#     else:
#       print("Attempt " + str(n) + " failed")
# retry(create_user, 3)
# retry(stop_service, 5)

# for n in range(0, 101):
#   if n % 7 == 0:
#     print(n)

# def factorial(n):
#   if n < 2:
#     return 1
#   return n * factorial(n - 1)
# print(factorial(int(input("Input the integer: "))))

# The function sum_positive_numbers should return the sum of all positive numbers between the number n received
# and 1. For example, when n is 3 it should return 1+2+3=6,
# and when n is 5 it should return 1+2+3+4+5=15. Fill in the gaps to make this work:

# def sum_positive_numbers(n):
#   # The base case is n being smaller than 1
#   if n <= 1:
#     return 1
#
#   # The recursive case is adding this number to
#   # the sum of the numbers smaller than this one.
#   return n + sum_positive_numbers(n - 1)
#
#
# print(sum_positive_numbers(3))  # Should be 6
# print(sum_positive_numbers(5))  # Should be 15

# def count_users(group):
#   count = 0
#   for member in get_members(group):
#     if is_group(member):
#       count += count_users(member)
#     else:
#       count += 1
#   return count
#
#
# print(count_users("sales"))  # Should be 3
# print(count_users("engineering"))  # Should be 8
# print(count_users("everyone"))  # Should be 18

# def is_power_of(number, base):
#   # Base case: when number is smaller than base.
#   if number < base:
#     return False
#     # If number is equal to 1, it's a power (base**0).
#   if number == 1:
#     return base == 1
#   else:
#     return True
#
#   # Recursive case: keep dividing number by base.
#   return is_power_of(number, base)
#
# print(is_power_of(8,2)) # Should be True
# print(is_power_of(64,4)) # Should be True
# print(is_power_of(70,10)) # Should be False

# x = 1
# # sum = 0
# # while x < 10:
# #   sum += x
# #   x += 1
# #
# # product = 1
# # while x < 10:
# #   product = product * x
# #   x += 1
# #
# # print(f' x= {x}, sum= {sum}, product= {product}')

# number = 1
# while number <= 7:
# 	print(number, end=" ")
# 	number += 1

# def show_letters(word):
# 	for w in word:
# 		print(w)
#
# print = show_letters("Hello")
# # Should print one line per letter

# def digits(n):
#     count = 0
#     if n == 0:
#         return 1
#     while (n != 0):
#         count += 1
#         n //= 10
#     return count


# print(digits(25))  # Should print 2
# print(digits(144))  # Should print 3
# print(digits(1000))  # Should print 4
# print(digits(0))  # Should print 1


# # 1 2 3
# # 2 4 6
# # 3 6 9
# # Should print the multiplication table shown above
# def multiplication_table(start, stop):
# 	for x in range(start, stop + 1):
# 		for y in range(start, stop + 1):
# 			print(str(x*y), end=" ")
# 		print(" ")
#
# multiplication_table(1, 3)

# def counter(start, stop):
# 	x = start
# 	if start > stop:
# 		return_string = "Counting down: "
# 		while x >= stop:
# 			return_string += str(x)
# 			if x != stop:
# 				return_string += ","
# 			x = x - 1
# 	else:
# 		return_string = "Counting up: "
# 		while x <= stop:
# 			return_string += str(x)
# 			if x != stop:
# 				return_string += ","
# 			x = x + 1
# 	return return_string
#
# print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
# print(counter(2, 1)) # Should be "Counting down: 2,1"
# print(counter(5, 5)) # Should be "Counting up: 5"

# def decade_counter():
# 	while year < 50:
# 		year += 10
# 	return year

# for x in range(1, 10, 3):
#     print(x)

# for x in range(10):
#     for y in range(x):
#         print(y)

# def votes(params):
# 	for vote in params:
# 	    print("Possible option:" + vote)
# votes(["yes","no","may be"])

# def loop(start, stop, step):
#     return_string = ""
#     if step == 0:
#         step = 1
#     if start > stop:
#         step = abs(step) * -1
#     else:
#         step = abs(step)
#     for count in range(start, stop, step):
#         return_string += str(count) + " "
#     return return_string.strip()
#
#
# print(loop(11, 2, 3))  # Should be 11 8 5
# print(loop(1, 5, 0))  # Should be 1 2 3 4
# print(loop(-1, -2, 0))  # Should be -1
# print(loop(10, 25, -2))  # Should be 10 12 14 16 18 20 22 24
# print(loop(1, 1, 1))  # Should be empty

# def double_word(word):
#     return word * 2 + str(len(word * 2))
#
# print(double_word("hello")) # Should return hellohello10
# print(double_word("abc"))   # Should return abcabc6
# print(double_word(""))      # Should return 0

# def first_and_last(message):
#     if message:
#         return message[0] == message[-1]
#     return True
#
# print(first_and_last("else"))
# print(first_and_last("tree"))
# print(first_and_last(""))

# pets = "lions tigers and bears"
# print(pets.index("g"))
# print(pets.index("bears"))
# print(pets.index("lions tigers and bears"))
# print("bears" in pets)
# print("dragons" in pets)

# answer = 'YES'
# if answer.lower() == 'yes':
# 	print(f'User answered yes')

# print(" yes ".strip())
# # print(" yes ".lstrip())
# # print(" yes ".rstrip())

# print("The fucking Indians scammed me".count("mm"))
# print("The fucking Indians scammed me".endswith("me"))
# print("Forest".isnumeric())# define a basic city class
# class City:
#     def __init__(self, name, country, elevation, population):
#         self.name = name
#         self.country = country
#         self.elevation = elevation
#         self.population = population
#
# # create a new instance of the City class and
# # define each attribute
# city1 = City("Cusco","Peru",3399,358052)
#
# # create a new instance of the City class and
# # define each attribute
# city2 = City("Sofia","Bulgaria",2290,1241675)
#
# # create a new instance of the City class and
# # define each attribute
# city3 = City("Seoul","South Korea",38,9733509)
#
# def max_elevation_city(min_population):
# # Initialize the variable that will hold
# # the information of the city with
# # the highest elevation
#     cities = [city1, city2, city3]
#     lowest = None
#     lowest_pop = 999999999
#     for city in cities:
#         if city.population > min_population:
#             if city.population < lowest_pop:
#                 lowest = city
#     if lowest != None:
#         return lowest.name
#     return ""
#
# print(max_elevation_city(100000)) # Should print "Cusco, Peru"
# print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
# print(max_elevation_city(10000000)) # Should print ""# define a basic city class
# class City:
#     def __init__(self, name, country, elevation, population):
#         self.name = name
#         self.country = country
#         self.elevation = elevation
#         self.population = population
#
# # create a new instance of the City class and
# # define each attribute
# city1 = City("Cusco","Peru",3399,358052)
#
# # create a new instance of the City class and
# # define each attribute
# city2 = City("Sofia","Bulgaria",2290,1241675)
#
# # create a new instance of the City class and
# # define each attribute
# city3 = City("Seoul","South Korea",38,9733509)
#
# def max_elevation_city(min_population):
# # Initialize the variable that will hold
# # the information of the city with
# # the highest elevation
#     cities = [city1, city2, city3]
#     lowest = None
#     lowest_pop = 999999999
#     for city in cities:
#         if city.population > min_population:
#             if city.population < lowest_pop:
#                 lowest = city
#     if lowest != None:
#         return lowest.name
#     return ""
#
# print(max_elevation_city(100000)) # Should print "Cusco, Peru"
# print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
# print(max_elevation_city(10000000)) # Should print ""
# print("1234567890".isnumeric())
# print(" ".join(["The", "string", "joined", "by", "spaces"]))
# print("This string is splitted into pieces".split())

# def main():
#     ## input the phrase
#     phrase = input("Enter the phrase: ")
#     ## split the phrase into substrings
#     phrase_split = phrase.split()
#     acronym = ""
#     ## iterate through every substring
#     for i in phrase_split:
#         acronym = acronym + i[0].upper()
#     print("The acronym for your phrase is ",acronym + ".")
# main()

# def initials(phrase):
# #     words = phrase.split()
# #     result = ""
# #     for word in words:
# #         result += word[0].upper()
# #     return result
# #
# # print(initials("Universal Serial Bus")) # Should be: USB
# # print(initials("local area network")) # Should be: LAN
# # print(initials("Operating system")) # Should be: OS

# name = "Manny"
# number = len(name) * 3
# print("Hello {}, your lucky number is {}".format(name, number))

# def student_grade(name, grade):
# 	return "{} received {}% on the exam".format(name, grade)
#
# print(student_grade("Reed", 80))
# print(student_grade("Paige", 92))
# print(student_grade("Jesse", 85))

# def is_palindrome(input_string):
#     # We'll create two strings, to compare them
#     new_string = ""
#     reverse_string = ""
#     # Traverse through each letter of the input string
#     for letter in input_string.strip():
#         # Add any non-blank letters to the
#         # end of one string, and to the front
#         # of the other string.
#         if letter !=' ':
#             new_string += letter
#             reverse_string = letter+reverse_string
#     # Compare the strings
#     if new_string.lower() == reverse_string.lower():
#         return True
#     return False
#
# print(is_palindrome("Never Odd or Even")) # Should be True
# print(is_palindrome("abc")) # Should be False
# print(is_palindrome("kayak")) # Should be True


# def convert_distance(miles):
# 	km = miles * 1.6
# 	result = "{} miles equals {:.1f} km".format(miles, km)
# 	return result
#
# print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
# print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
# print(convert_distance(11)) # Should be: 11 miles equals 17.6 km

# Weather = "Rainfall"
# print(Weather[:4])

# string = "Gurov_Vic_QA_AUT_CV_edited_23_march_2020"
# print(len(string))

# users = ["Mike", "Karen", "Jake", "Tasha"]
# print(users)
# print(type(users))
# print(len(users))
# print("Mike" in users)
# print("Penis" in users)
# print(users[0:])

# def group_list(group, users):
#     members = (f'"{group}: {str(users[0:])}"')
#     return members
#
# print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
# print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
# print(group_list("Users", "")) # Should be "Users:"

# def group_list(group, users):
#     members = ('"' + str(group) + ': ' + str(', '.join(users) + '"'))
#     return members
#
# print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
# print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
# print(group_list("Users", "")) # Should be "Users:"

# def format_address(address_string):
# # Declare variables
# 	house_number = ''
# 	street_name = ''
# # Separate the address string into parts
# 	spi = address_string.split()
# # Traverse through the address parts
# 	for ele in spi:
# 	# Determine if the address part is the
# 	# house number or part of the street name
# 		if ele.isdigit():
# 			house_number = ele
# 		else:
# 			street_name += ele
# 			street_name += ' '
# # Does anything else need to be done
# # before returning the result?
#
# # Return the formatted string
# 	return "house number {} on street named {}".format(house_number, street_name)
# print(format_address("123 Main Street"))
# # Should print: "house number 123 on street named Main Street"
#
# print(format_address("1001 1st Ave"))
# # Should print: "house number 1001 on street named 1st Ave"
#
# print(format_address("55 North Center Drive"))
# # Should print "house number 55 on street named North Center Drive"

# def highlight_word(sentence, word):
# 	return(sentence.replace(word,word.upper()))
#
# print(highlight_word("Have a nice day", "nice"))
# print(highlight_word("Shhh, don't be so loud!", "loud"))
# print(highlight_word("Automating with Python is fun", "fun"))

# def combine_lists(list1, list2):
# 	# Generate a new list containing the elements of list2
# 	# Followed by the elements of list1 in reverse order
# 	new_list = list2
# 	for i in reversed(range(len(list1))):
# 		new_list.append(list1[i])
# 	return new_list
#
#
# Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
# Drews_list = ["Mike", "Carol", "Greg", "Marcia"]
#
# print(combine_lists(Jamies_list, Drews_list))

# def squares(start, end):
# 	return [ (i * i) for i in range(start, end + 1) ]
#
# print(squares(2, 3)) # Should be [4, 9]
# print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
# print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# def car_listing(car_prices):
#   result = ""
#   for key, value in car_prices.items():
#     result += "{} costs {} dollars".format(key, value) + "\n"
#   return result
#
# print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

# def combine_guests(guests1, guests2):
#   # Combine both dictionaries into one, with each key listed
#   # only once, and the value from guests1 taking precedence
#   guests1.update(guests2)
#   return guests1
#
# Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
# Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}
#
# print(combine_guests(Rorys_guests, Taylors_guests))

# def combine_guests(guests1, guests2):
# 	# Combine both dictionaries into one, with each key listed
# 	# only once, and the value from guests1 taking precedence
# 	combined_dic = guests1
# 	for key2 in guests2:
# 		if key2 in guests1:
# 			pass
# 		else:
# 			combined_dic[key2] = guests2[key2]
#
# 	return combined_dic
#
#
# Rorys_guests = {"Adam": 2, "Brenda": 3, "David": 1, "Jose": 3, "Charlotte": 2, "Terry": 1, "Robert": 4}
# Taylors_guests = {"David": 4, "Nancy": 1, "Robert": 2, "Adam": 1, "Samantha": 3, "Chris": 5}
#
# print(combine_guests(Rorys_guests, Taylors_guests))

# def count_letters(text):
#   result = {}
#   # Go through each letter in the text
#   convert_text = text.lower()
#   for letter in convert_text:
#     # Check if the letter needs to be counted or not
#     if letter.isalpha():
#       if letter in result:
#     # Add or increment the value in the dictionary
#         result[letter] += 1
#       else:
#         result[letter] = 1
#   return result
#
# print(count_letters("AaBbCc"))
# # Should be {'a': 2, 'b': 2, 'c': 2}
#
# print(count_letters("Math is fun! 2+2=4"))
# # Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}
#
# print(count_letters("This is a sentence."))
# # Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}

# animal = "Hippopotamus"
# print(animal[3:6])
# print(animal[-5])
# print(animal[10:])

# colors = ["red", "white", "blue"]
# colors.insert(2, "yellow")
# print(colors)

# host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
# host_addresses.keys()
# print(host_addresses.keys())

# list = ['Apple', 'Pinapple', 'Mellon']
# list.append('Carrot') # append adds to the end
# print(list)
# list.insert(0, 'Kiwi') # insert adds to the index place
# print(list)
# list.insert(25, 'Peach') # if insert with index > than list has-it goes at the end
# print(list)
# list.remove('Mellon') # remove
# print(list)
# # list.remove('Pear')
# print(list)
# print(list)
# list.pop(1) # remove and returns elements from a list
# list[2] = 'Strawberry'
# print(list)
# print(list.pop(2))

# def skip_elements(elements):
# 	# Initialize variables
# 	new_list = []
# 	i = 0
#
# 	# Iterate through the list
# 	for i in range(0, len(elements), 2):
# 		# Does this element belong in the resulting list?
# 		if i >= 0:
# 			# Add this element to the resulting list
# 			new_list.append(elements[i])
# 		# Increment i
# 		i += 1
#
# 	return new_list
#
# print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
# print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
# print(skip_elements([])) # Should be []

# def get_word(sentence, n):
# 	# Only proceed if n is positive
# 	if n > 0:
# 		words = sentence.split(" ")
# 		# Only proceed if n is not more than the number of words
# 		if n <= len(words):
# 			return(words[n-1])
# 	return("")
#
# print(get_word("This is a lesson about lists", 4)) # Should print: lesson
# print(get_word("This is a lesson about lists", -4)) # Nothing
# print(get_word("Now we are cooking!", 1)) # Should print: Now
# print(get_word("Now we are cooking!", 5)) # Nothing

# def convert_seconds(seconds):
# 	hours = seconds // 3600
# 	minutes = (seconds - hours * 3600) // 60
# 	remaining_seconds = seconds - hours * 3600 - minutes * 60
# 	return hours, minutes, remaining_seconds
#
# result  = convert_seconds(5000)
# type(result)
# print(result)
# hours, minutes, seconds = result
# print(hours, minutes, seconds)
# hours, minutes, seconds = convert_seconds(1000)
# print(hours, minutes, seconds)

# def file_size(file_info):
# 	name, type, size = file_info
# 	return("{:.2f}".format(size / 1024))
#
# print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
# print(file_size(('Notes', 'txt', 496))) # Should print 0.48
# print(file_size(('Program', 'py', 1239))) # Should print 1.21

# animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
# chars = 0
# for animal in animals:
# 	chars += len(animal)
#
# print("Total charachters: {}, Average lenhgth: {}".format(chars, chars/len(animals)))

# winners = ["Ashley", "Dylan", "Reese"]
# for index, person in enumerate(winners):
# 	print("{} - {}".format(index + 1, person))

# for n in range(101):
#   if n % 7 == 0:
#     print(n)

# Write a script that prints the multiples of 7 between 0 and 100.
# Print one multiple per line and avoid printing any numbers that aren't multiples of 7.
# Remember that 0 is also a multiple of 7.
# nl=[]
# for x in range(101):
#     if (x % 7==0):
#         nl.append(str(x))
# print ("\n".join(nl))

# multiples = []
# for i in range(1,11):
#     multiples.append(i*7)
#
# print(multiples)

# multiples =[x*7 for x in range(1,11)]
# print(multiples)

# languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
# lengths = [len(language) for language in languages]
# print(lengths)

# z = [i for i in range(0, 101) if i%3 == 0]
# print(z, '\n', len(z))

# def odd_numbers(n):
# 	return [x for x in range(1, n + 1) if x % 2 != 0]
#
# print(odd_numbers(5))  # Should print [1, 3, 5]
# print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
# print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
# print(odd_numbers(1))  # Should print [1]
# print(odd_numbers(-1)) # Should print []

# def test_list(n):
#     return [ x for x in range(1, n + 1) if x % 10 == 0 ]
# print(test_list(101), '\n', len(test_list(101)))

# def skip_elements(elements):
#     new_list = []
#     for i, element in enumerate(elements):
#         if i % 2 == 0:
#             new_list.append(element)
#     return new_list
#
# print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
# print(skip_elements(
# ['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']']

# filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# # Generate newfilenames as a list containing the new filenames
# # using as many lines of code as your chosen method requires.
# newfilenames = []
# for i in range(len(filenames)):
#     prev_name = filenames[i]
#     if prev_name.endswith("hpp"):
#         new_name = prev_name.replace("hpp", "h")
#     else:
#         new_name = prev_name
#     newfilenames.append(new_name)

# def octal_to_string(octal):
#     result = ""
#     value_letters = [(4, "r"), (2, "w"), (1, "x")]
#     # Iterate over each of the digits in octal
#     for perm in [int(n) for n in str(octal)]:
#         # Check for each of the permissions values
#         for value, letter in value_letters:
#             if perm >= value:
#                 result += letter
#                 perm -= value
#             else:
#                 result += "-"
#     return result
#
#
# print(octal_to_string(755))  # Should be rwxr-xr-x
# print(octal_to_string(644))  # Should be rw-r--r--
# print(octal_to_string(750))  # Should be rwxr-x---
# print(octal_to_string(600))  # Should be rw-------

# def pig_latin(text):
#   words = text.split()
#   pigged_text = []
#
#   for word in words:
#     word = word[1:] + word[0] + 'ay'
#     pigged_text.append(word)
#
#   return ' '.join(pigged_text)
#
# print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
# print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

# def pig_latin(text):
#   say = []
#   # Separate the text into words
#   words = text.split()
#   for word in words:
#     # Create the pig latin word and add it to the list
#     word = word[1:] + word[0] + "ay"
#     say.append(word)
#     # Turn the list back into a phrase
#   return " ".join(say)
#
# print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
# print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay"

# sample_dict = {"key_1":1, "key_2":2, "key_3":3, "key_4":4}
# print(sample_dict, '\n', type(sample_dict))
# print(sample_dict["key_2"])
# print("key_3" in sample_dict)
# print("key_0" in sample_dict)
# sample_dict["key_4"] = 4
# print(sample_dict)
# sample_dict["key_1"] = 11
# print(sample_dict)
# del sample_dict["key_1"]
# print(sample_dict)
# sample_dict["key_1"] = 1
# print(sample_dict)

# cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
# for keys, values in cool_beasts.items():
#     print("{} have {}".format(keys, values))

# toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
# toc["Epilogue"] = 39 # Epilogue starts on page 39
# toc["Chapter 3"] = 24 # Chapter 3 now starts on page 24
# print(toc) # What are the current contents of the dictionary?
# print("Chapter 5" in toc)  # Is there a Chapter 5?
# for extensions in toc:
#   print(extensions)
# for part, page in toc.items():
#  print('There is "{}" part of the book on the "{}" page'.format(part, page))
# print(toc.keys())
# print(toc.values())
# for value in toc.values():
#     print(value)
# for keys in toc.keys():
#     print(keys)

# def count_letters(text):
#   result = {}
#   for letter in text:
#       if letter not in result:
#         result[letter] = 0
#       result[letter] += 1
#   return result
#
# print(count_letters(str(input("Input the string, please: "))))

# In Python, a dictionary can only hold a single value for a given key.
# To workaround this, our single value can be a list containing multiple values.
# Here we have a dictionary called "wardrobe" with items of clothing and their colors.
# Fill in the blanks to print a line for each item of clothing with each color,
# for example: "red shirt", "blue shirt", and so on.

# wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
# for __:
# 	for __:
# 		print("{} {}".format(__))

# wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
# for key, value in wardrobe.items():
# 	for i in value:
# 		print("{} {}".format(i, key))

# print(wardrobe.get("shirt", "red"))
# print(wardrobe.keys())
# print(wardrobe.values())

# d = {'x': 1, 'y': 2, 'z': 3}
# for key in d:
#     print(key, 'corresponds to', d[key])

# def email_list(domains):
# 	emails = []
# 	for key, users in domains.items():
# 	  for user in users:
# 	    emails.append(user + '@' + key)
# 	return(emails)
#
# print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

# def groups_per_user(group_dictionary):
#     user_groups = {}
#     # Go through group_dictionary
#     for group in group_dictionary:
#         # Now go through the users in the group
#         for user in group_dictionary[group]:
#             # Now add the group to the the list of
# # groups for this user, creating the entry
# # in the dictionary if necessary
#             if user not in user_groups:
#                 user_groups[user] = []
#             if group not in user_groups[user]:
#                 user_groups[user].append(group)
#     return user_groups
#
# print(groups_per_user({"local": ["admin", "userA"],
# 		"public":  ["admin", "userB"],
# 		"administrator": ["admin"] }))

# wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
# new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
# wardrobe.update(new_items)
# print(wardrobe)

# def add_prices(basket):
# 	# Initialize the variable that will be used for the calculation
# 	total = 0
# 	# Iterate through the dictionary items
# 	for key, value in basket.items():
# 		# Add each price to the total calculation
# 		# Hint: how do you access the values of
# 		# dictionary items?
# 		total += value
# 	# Limit the return value to 2 decimal places
# 	return round(total, 2)
#
# groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
# 	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}
#
# print(add_prices(groceries)) # Should print 28.44

# print(type(0))
# print(type(0.5))
# print(type(""))
# print(type(['1', '2']))
# print(type({"key_1": 1, "key_2":2}))
# print(dir(""))
# help("")

# class Apple:
#     pass

# class Apple:
#     color = ""
#     flavor = ""
#
# jonagold = Apple()
# jonagold.color = "red"
# jonagold.flavor = "sweet"
# print(jonagold.color,"\n", jonagold.flavor)
# print(jonagold.color.upper(),"\n", jonagold.flavor.upper())
#
# golden = Apple()
# golden.color = "Yellow"
# golden.flavor = "Soft"
# print(golden.color,"\n", golden.flavor)
# print(golden.color.upper(),"\n", golden.flavor.upper())

# class Flower:
#   color = 'unknown'
#
# rose = Flower()
# rose.color = 'red'
#
# violet = Flower()
# violet.color = 'blue'
#
# this_pun_is_for_you = 'I do not like you!'
#
# print("Roses are {},".format(rose.color))
# print("violets are {},".format(violet.color))
# print(this_pun_is_for_you)

# “If you have an apple and I have an apple and we exchange these apples then
# you and I will still each have one apple. But if you have an idea and I have
# an idea and we exchange these ideas, then each of us will have two ideas.”
# George Bernard Shaw

# class Person:
#     apples = 0
#     ideas = 0
#
#
# johanna = Person()
# johanna.apples = 1
# johanna.ideas = 1
#
# martin = Person()
# martin.apples = 2
# martin.ideas = 1
#
#
# def exchange_apples(you, me):
#     # Here, despite G.B. Shaw's quote, our characters have started with       #different amounts of apples so we can better observe the results.
#     # We're going to have Martin and Johanna exchange ALL their apples with #one another.
#     # Hint: how would you switch values of variables,
#     # so that "you" and "me" will exchange ALL their apples with one another?
#     # Do you need a temporary variable to store one of the values?
#     # You may need more than one line of code to do that, which is OK.
#     t_1 = johanna.apples
#     t_2 = martin.apples
#     you.apples = t_2
#     me.apples = t_1
#     return you.apples, me.apples
#
#
# def exchange_ideas(you, me):
#     # "you" and "me" will share our ideas with one another.
#     # What operations need to be performed, so that each object receives
#     # the shared number of ideas?
#     # Hint: how would you assign the total number of ideas to
#     # each idea attribute? Do you need a temporary variable to store
#     # the sum of ideas, or can you find another way?
#     # Use as many lines of code as you need here.
#     you.ideas += johanna.ideas
#     me.ideas += martin.ideas
#     return you.ideas, me.ideas
#
#
# exchange_apples(johanna, martin)
# print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
# exchange_ideas(johanna, martin)
# print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))


# The City class has the following attributes: name, country (where the city is located), elevation (measured in meters),
# and population (approximate, according to recent statistics). Fill in the blanks of the max_elevation_city function
# to return the name of the city and its country (separated by a comma), when comparing the 3 defined instances
# for a specified minimal population. For example, calling the function for a minimum population of 1 million:
# max_elevation_city(1000000) should return "Sofia, Bulgaria".

# define a basic city class
# class City:
#    name = ""
#    country = ""
#    elevation = 0
#    population = 0
#
# # create a new instance of the City class and
# # define each attribute
# city1 = City()
# city1.name = "Cusco"
# city1.country = "Peru"
# city1.elevation = 3399
# city1.population = 358052
#
# # create a new instance of the City class and
# # define each attribute
# city2 = City()
# city2.name = "Sofia"
# city2.country = "Bulgaria"
# city2.elevation = 2290
# city2.population = 1241675
#
# # create a new instance of the City class and
# # define each attribute
# city3 = City()
# city3.name = "Seoul"
# city3.country = "South Korea"
# city3.elevation = 38
# city3.population = 9733509
#
# def max_elevation_city(min_population):
#    # Initialize the variable that will hold
# # the information of the city with
# # the highest elevation
#    return_city = City()
#
#    # Evaluate the 1st instance to meet the requirements:
#    # does city #1 have at least min_population and
#    # is its elevation the highest evaluated so far?
#    if city1.population >= min_population and city1.elevation > return_city.elevation:
#       return_city = city1
#    # Evaluate the 2nd instance to meet the requirements:
#    # does city #2 have at least min_population and
#    # is its elevation the highest evaluated so far?
#    if city2.population >= min_population and city2.elevation > return_city.elevation:
#       return_city = city2
#    # Evaluate the 3rd instance to meet the requirements:
#    # does city #3 have at least min_population and
#    # is its elevation the highest evaluated so far?
#    if city3.population >= min_population and city3.elevation > return_city.elevation:
#       return_city = city3
#
#    #Format the return string
#    if return_city.name:
#       return ("{}, {}".format(return_city.name, return_city.country))
#    else:
#       return ""
#
# print(max_elevation_city(100000)) # Should print "Cusco, Peru"
# print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
# print(max_elevation_city(10000000)) # Should print ""

# define a basic city class
# class City:
#     def __init__(self, name, country, elevation, population):
#         self.name = name
#         self.country = country
#         self.elevation = elevation
#         self.population = population
#
# # create a new instance of the City class and
# # define each attribute
# city1 = City("Cusco", "Peru", 3399, 358052)
#
# # create a new instance of the City class and
# # define each attribute
# city2 = City("Sofia", "Bulgaria", 2290, 1241675)
#
# # create a new instance of the City class and
# # define each attribute
# city3 = City("Seoul", "South Korea", 38, 9733509)
#
#
# def max_elevation_city(min_population):
#     # Initialize the variable that will hold
#     # the information of the city with
#     # the highest elevation
#     cities = [city1, city2, city3]
#     lowest = None
#     lowest_pop = 10000001
#     for city in cities:
#         if city.population >= min_population and city.population <= lowest_pop:
#             if city.elevation >= city1.elevation or city.elevation >= city2.elevation or city.elevation >= city3.elevation:
#                 lowest = city
#         if lowest != None:
#             return ("{}, {}".format(lowest.name, lowest.country))
#     return ""
#
#
# print(max_elevation_city(100000))  # Should print "Cusco, Peru"
# print(max_elevation_city(1000000))  # Should print "Sofia, Bulgaria"
# print(max_elevation_city(10000000))  # Should print ""

# class Furniture:
# 	color = ""
# 	material = ""
#
# table = Furniture()
# table.color = "brown"
# table.material = "wood"
#
# couch = Furniture()
# couch.color = "red"
# couch.material = "leather"
#
# def describe_furniture(piece):
# 	return ("This piece of furniture is made of {} {}".format(piece.color, piece.material))
#
# print(describe_furniture(table))
# # Should be "This piece of furniture is made of brown wood"
# print(describe_furniture(couch))
# # Should be "This piece of furniture is made of red leather"

# class Piglet:
#     def speak(self):
#         print("Hru Blya Hru Nahuy")
# hamlet = Piglet()
# hamlet.speak()

# class Piglet:
#     def speak(self):
#         print("Hru Blya Hru Nahuy! I'm {}!".format(self.name))
# hamlet = Piglet()
# hamlet.name = "Hamlet"
# hamlet.speak()
#
# petunia = Piglet()
# petunia.name = "Petunia"
# petunia.speak()

# class Piglet:
#     years = 0
#     def pig_years(self):
#         return self.years * 18
#
# piggy = Piglet()
# print(piggy.pig_years())
#
# piggy.years = 2
# print(piggy.pig_years())

# class Dog:
#     years = 0
#     def dogs_years(self):
#         return self.years * 7
#
# sharik = Dog()
# print(sharik.dogs_years())
#
# sharik.years = 3
# print(sharik.dogs_years())

# class Apple:
#     def __init__(self, color, flavor):
#         self.color = color
#         self.flavor = flavor
#
# jonagold = Apple("red", "sweet")
# print(jonagold.color, jonagold.flavor)

# class Person:
#     def __init__(self, name):
#         self.name = name
#     def greeting(self):
#         # Should return "hi, my name is " followed by the name of the Person.
#         return "hi, my name is {}".format(self.name)
#
# # Create a new instance with a name of your choice
# some_person = Person("Fucker")
# # Call the greeting method
# print(some_person.greeting())

# class Person:
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#         # Should return "hi, my name is " followed by the name of the Person.
#         return "hi, my name is {}".format(self.name)
#
# # Create a new instance with a name of your choice
# some_person = Person("Fucker")
# # Call the greeting method
# print(some_person)
# help(Person)

# class Person:
#   def __init__(self, name):
#     self.name = name
#   def greeting(self):
#     """“Outputs a message with the name of the person”"""
#     print("Hello! My name is {name}.".format(name=self.name))
# help(Person)

# class MyLife:
#     def __init__(self, date_of_birth, full_name, current_year, years_lived):
#         self.date_of_birth = date_of_birth
#         self.full_name = full_name
#         self.current_year = current_year
#         self.years_lived = int(current_year) - 1970
#     def __str__(self):
#         return "Date of birth:{}, Full Name:{}, Curren year: {}, Age:{}".format(self.date_of_birth, self.full_name, self.current_year, self.years_lived)
#
# i_am = MyLife("03 July 1970", "Vic Gurov", "2020", "50")
#
# print(i_am)
#
# help(MyLife)


# def to_seconds(hours, minutes, seconds):
#     """ Returns the amount of seconds in the given hours, minutes, and seconds """
#     return hours*3600+minutes*60+seconds
# print(round(to_seconds(3,5,67), 2))
# help(to_seconds)

# def to_hours(seconds):
#     """ Returns the amount of seconds in the given hours, minutes, and seconds """
#     return seconds/3600
# print(round(to_hours(11167), 4))
# help(to_hours)

# The code below defines an Elevator class. The elevator has a current floor, it also has a top and a bottom floor
# that are the minimum and maximum floors it can go to.
# Fill in the blanks to make the elevator go through the floors requested.

# class Elevator:
#     def __init__(self, bottom, top, current):
#         """Initializes the Elevator instance."""
#         self.bottom = bottom
#         self.top = top
#         self.current = current
#     def up(self):
#         """Makes the elevator go up one floor."""
#         self.current = self.current + 1 if self.current < self.top else self.current
#     def down(self):
#         """Makes the elevator go down one floor."""
#         self.current = self.current - 1 if self.current > self.bottom else self.current
#     def go_to(self, floor):
#         """Makes the elevator go to the specific floor."""
#         assert floor <= self.top and floor >= self.bottom
#         self.current = floor
#     def __str__(self):
#          return '"Current floor: {}"'.format(self.current)
#
# elevator = Elevator(-1, 10, 0)
#
# elevator.up()
# elevator.current #should output 1
# print(elevator.current)
#
# elevator.down()
# elevator.current #should output 0
# print(elevator.current)
#
# elevator.go_to(10)
# elevator.current #should output 10
# print(elevator.current)
#
# # Go to the top floor. Try to go up, it should stay. Then go down.
# elevator.go_to(10)
# elevator.up()
# elevator.down()
# print(elevator.current) # should be 9
# # Go to the bottom floor. Try to go down, it should stay. Then go up.
# elevator.go_to(-1)
# elevator.down()
# elevator.down()
# elevator.up()
# elevator.up()
# print(elevator.current) # should be 1
#
# elevator.go_to(5)
# print(elevator)

# class Fruit: # Parent Class
#     def __init__(self, color, flavor): # def __init__ - constructor
#         self.color = color # color and flavor are attributes
#         self.flavor = flavor
#
# class Apple(Fruit): # Inherited Class - children class
#     pass
#
# class Grape(Fruit): # Inherited Class - children class
#     pass
#
# granny_smith = Apple("green", "tart")
# carnelian = Grape("purple", "sweet")
# print(granny_smith.flavor)
# print(carnelian.color)

# class Animals:
#     sound = ""
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         print("{sound} I'm {name} ! {sound}".format(name=self.name, sound=self.sound))
#
# class Piglet(Animals):
#     sound = "Hryu Blya !"
#
# hamlet = Piglet("Hamlet")
# hamlet.speak()
#
# class Cow(Animals):
#     sound = "Uebooouuu !!!"
#
# milky = Cow("Milky White")
# milky.speak()
#

# class Clothing:
#     material = ""
#     def __init__(self, name):
#         self.name = name
#     def checkmaterial(self):
#         print("This {} is made of {}".format(self.name, self.material))
# class Shirt(Clothing):
#     material = "Cotton"
# polo = Shirt("Polo")
# polo.checkmaterial()

# class Repository:
#     def __init__(self):
#         self.packages = {}
#     def ad_package(self,package):
#         self.packages[package.name] = package
#     def total_size(self):
#         result = 0
#         for package in self.packages.values():
#             result += package.size
#         return result

# Let’s expand a bit on our Clothing classes from the previous in-video question.
# Your mission: Finish the "Stock_by_Material" method and iterate over the amount of each item of a given material that is in stock.
# When you’re finished, the script should add up to 10 cotton Polo shirts.

# class Clothing:
#     stock = {'name': [], 'material': [], 'amount': []}
#
#     def __init__(self, name):
#         material = ""
#         self.name = name
#
#     def add_item(self, name, material, amount):
#         Clothing.stock['name'].append(self.name)
#         Clothing.stock['material'].append(self.material)
#         Clothing.stock['amount'].append(amount)
#
#     def Stock_by_Material(self, material):
#         count = 0
#         n = 0
#         for item in Clothing.stock['material']:
#             if item == material:
#                 count += Clothing.stock['amount'][n]
#                 n += 1
#         return count
#
# class shirt(Clothing):
#     material = "Cotton"
#
# class pants(Clothing):
#     material = "Cotton"
#
# polo = shirt("Polo")
# sweatpants = pants("Sweatpants")
# polo.add_item(polo.name, polo.material, 4)
# sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
# current_stock = polo.Stock_by_Material("Cotton")
# print(f'Current stock: current_stock')

# import random
#
# print(random.randint(1, 10))
# print(random.randint(1, 10))
# print(random.randint(1, 10))

# import datetime
# now = datetime.datetime.now()
# print(type(now))
# print(now)
# print(now.year)
# print(now, now + datetime.timedelta(days=28))

# class Animal:
#     name = ""
#     category = ""
#
#     def __init__(self, name):
#         self.name = name
#
#     def set_category(self, category):
#         self.category = category
#
# class Turtle(Animal):
#     category = 'reptile'
# print(Turtle.category)
#
# class Snake(Animal):
#     category = 'reptile'
# print(Snake.category)
#
# class Zoo:
#     def __init__(self):
#         self.current_animals = {}
#
#     def add_animal(self, animal):
#         self.current_animals[animal.name] = animal.category
#
#     def total_of_category(self, category):
#         result = 0
#         for animal in self.current_animals.values():  # here was the blank where current_animals
#             if category == category:
#                 result += 1
#         return result
#
#
# zoo = Zoo()
#
# turtle = Turtle("Turtle") #create an instance of the Turtle class
# snake = Snake("Snake") #create an instance of the Snake class
#
# zoo.add_animal(turtle)
# zoo.add_animal(snake)
#
# print('Total: ', zoo.total_of_category("reptile"), 'categories.') #how many zoo animal types in the reptile category

# # Assessment - Object-oriented programming
# # In this exercise, we'll create a few classes to simulate a server that's taking connections
# # from the outside and then a load balancer that ensures that there are enough servers to serve those connections.
# # To represent the servers that are taking care of the connections, we'll use a Server class.
# # Each connection is represented by an id, that could, for example, be the IP address of the computer connecting to the server.
# # For our simulation, each connection creates a random amount of load in the server, between 1 and 10.
# # Run the following code that defines this Server class.
#
# # Begin Portion 1#
# import random
#
# class Server:
#     def __init__(self):
#         """Creates a new server instance, with no active connections."""
#         self.connections = {}
#
#     def add_connection(self, connection_id):
#         """Adds a new connection to this server."""
#         connection_load = random.random() * 10 + 1
#         # Add the connection to the dictionary with the calculated load
#         if connection_id != None:
#             self.connections[connection_id] = connection_load
#
#     def close_connection(self, connection_id):
#         """Closes a connection on this server."""
#         # Remove the connection from the dictionary
#         if connection_id != None:
#             del self.connections[connection_id]
#
#     def load(self):
#         """Calculates the current load for all connections."""
#         total = 0
#         # Add up the load for each of the connections
#         for user in self.connections:
#             total += self.connections[user]
#         return total
#
#     def __str__(self):
#         """Returns a string with the current load of the server"""
#         return "{:.2f}%".format(self.load())
#
# # End Portion 1#
#
# server = Server()
# server.add_connection("192.168.1.1")
# print(server)
#
# server.add_connection("192.168.1.2")
# print(server)
#
# # server.add_connection("192.168.1.3")
# # print(server)
# #
# # server.add_connection("192.168.1.4")
# # print(server)
#
# server.close_connection("192.168.1.1")
# print(server)
#
# server.close_connection("192.168.1.2")
# print(server)
#
# # Alright, we now have a basic implementation of the server class. Let's look at the basic LoadBalancing class.
# # This class will start with only one server available.
# # When a connection gets added, it will randomly select a server to serve that connection,
# # and then pass on the connection to the server.
# # The LoadBalancing class also needs to keep track of the ongoing connections to be able to close them.
# # This is the basic structure:
#
# #Begin Portion 2#
# class LoadBalancing:
#     def __init__(self):
#         """Initialize the load balancing system with one server"""
#         self.connections = {}
#         self.servers = [Server()]
#
#     def add_connection(self, connection_id):
#         """Randomly selects a server and adds a connection to it."""
#         server = random.choice(self.servers)
#         # Add the connection to the dictionary with the selected server
#         server.add_connection(connection_id)
#         # Add the connection to the server
#         self.ensure_availability()
#
#     def close_connection(self, connection_id):
#         """Closes the connection on the the server corresponding to connection_id."""
#         # Find out the right server
#         # Close the connection on the server
#         # Remove the connection from the load balancerfor server in self.servers:
#         for server in self.servers:
#             if connection_id in server.connections:
#                 server.close_connection(connection_id)
#                 break
#
#     def avg_load(self):
#         """Calculates the average load of all servers"""
#         # Sum the load of each server and divide by the amount of servers
#         total_load = 0
#         total_server = 0
#         for server in self.servers:
#             total_load += server.load()
#             total_server += 1
#         return round((total_load/total_server), 2)
#
#     def ensure_availability(self):
#         """If the average load is higher than 50, spin up a new server"""
#         if self.avg_load() > 50:
#             self.servers.append(Server())
#
#     def __str__(self):
#         """Returns a string with the load for each server."""
#         loads = [str(server) for server in self.servers]
#         return "[{}]".format(",".join(loads))
# #End Portion 2#
#
# # As with the Server class, this class is currently incomplete.
# # You need to fill in the gaps to make it work correctly.
# # For example, this snippet should create a connection in the load balancer,
# # assign it to a running server and then the load should be more than zero:
#
# l = LoadBalancing()
# l.add_connection("fdca:83d2::f20d")
# print(l.avg_load())
#
# # After running the above code, the output is 0.
# # Fill in the missing parts for the add_connection and avg_load methods of the LoadBalancing
# # class to make this print the right load.
# # Be sure that the load balancer now has an average load more than 0 before proceeding.
#
# # What if we add a new server?
#
# l.servers.append(Server())
# print(l.avg_load())
#
# # The average load should now be half of what it was before.
# # If it's not, make sure you correctly fill in the missing gaps for the add_connection
# # and avg_load methods so that this code works correctly.
# # Fantastic! Now what about closing the connection?
# # Hint: You can iterate through the all servers in the self.servers list to get the total server load
# # amount and then divide by the length of the self.servers list to compute the average load amount.
#
# # Fantastic! Now what about closing the connection?
#
# l.close_connection("fdca:83d2::f20d")
# print(l.avg_load())
#
# # Fill in the code of the LoadBalancing class to make the load go back to zero once the connection is closed.
# #
# # Great job! Before, we added a server manually. But we want this to happen automatically when the average load is
# # more than 50%. To make this possible, fill in the missing code for the ensure_availability method and call it
# # from the add_connection method after a connection has been added. You can test it with the following code:
#
# for connection in range(20):
#     l.add_connection(connection)
# print(l)
#
# # The code above adds 20 new connections and then prints the loads for each server in the load balancer.
# # If you coded correctly, new servers should have been added automatically to ensure
# # that the average load of all servers is not more than 50%.
# #
# # Run the following code to verify that the average load of the load balancer is not more than 50%.
#
# print(l.avg_load(),'%')
#
# # Awesome! If the average load is indeed less than 50%, you are all done with this assessment.

# numbers = [4, 6, 2, 7, 1]
# numbers.sort() # sorted returns a new list, while sort returns the same list reorganized.
# print(numbers)
# print(sorted(numbers))
#
# names = ["Carlos", "Ray", "Alex", "Kelly"]
# print(names)
# print(sorted(names)) # sorted returns a new list, while sort returns the same list reorganized.
# print(sorted(names, key = len))
# names.sort()
# print(names)

# def get_event_date(event):
#     return event.date
#
# def current_users(events):
#     events.sort(key=get_event_date)
#     machines = {}
#     for event in events:
#         if event.machine not in machines:
#             machines[event.machine] = set()
#         if event.type == "login":
#             machines[event.machine].add(event.user)
#         elif event.type == "logout" and event.user in machines[event.machine]:
#             machines[event.machine].remove(event.user)
#     return machines
#
# def generate_report(machines):
#     for machine, users in machines.items():
#         if len(users) > 0:
#             user_list = ", ".join(users)
#             print("{}: {}".format(machine, user_list))
#
# class Event:
#     def __init__(self, event_date, event_type, machine_name, user):
#         self.date = event_date
#         self.type = event_type
#         self.machine = machine_name
#         self.user = user
#
# events = [
#     Event("2020-01-21 12:45:56", "login", "myworkstation.local", "jordan"),
#     Event("2020-01-22 15:53:42", "logout", "webserver.local", "jordan"),
#     Event("2020-01-21 18:53:21", "login", "webserver.local", "lane"),
#     Event("2020-01-22 10:25:34", "logout", "myworkstation.local", "jordan"),
#     Event("2020-01-21 08:20:01", "login", "webserver.local", "jordan"),
#     Event("2020-01-23 11:24:35", "logout", "mailserver.local", "chris"),
# ]
#
# users = current_users(events)
# print('Users:', users)
#
# generate_report(users)

# Here are all the installs and imports you will need for your word cloud script and uploader widget
# !pip install wordcloud
# !pip install fileupload
# !pip install ipywidgets
# !jupyter nbextension install --py --user fileupload
# !jupyter nbextension enable --py fileupload
# import wordcloud
# import numpy as np
# from matplotlib import pyplot as plt
# from IPython.display import display
# import fileupload
# import io
# import sys
#
# # Whew! That was a lot. All of the installs and imports for your word cloud script and uploader widget have been completed.
# # IMPORTANT! If this was your first time running the above cell containing the installs and imports, you will need save this notebook now.
# # Then under the File menu above, select Close and Halt. When the notebook has completely shut down, reopen it.
# # This is the only way the necessary changes will take affect.
# # To upload your text file, run the following cell that contains all the code for a custom uploader widget.
# # Once you run this cell, a "Browse" button should appear below it.
# # Click this button and navigate the window to locate your saved text file.
#
# # This is the uploader widget
#
# def _upload():
#
#     _upload_widget = fileupload.FileUploadWidget()
#
#     def _cb(change):
#         global file_contents
#         decoded = io.StringIO(change['owner'].data.decode('utf-8'))
#         filename = change['owner'].filename
#         print('Uploaded `{}` ({:.2f} kB)'.format(
#             filename, len(decoded.read()) / 2 **10))
#         file_contents = decoded.getvalue()
#
#     _upload_widget.observe(_cb, names='data')
#     display(_upload_widget)
#
# _upload()
#
# # Uploaded `Patton_Ron_software_testing.txt` (790.84 kB)
#
# # The uploader widget saved the contents of your uploaded file into a string object named file_contents that your word cloud script can process.
# # This was a lot of preliminary work, but you are now ready to begin your script.
# # Write a function in the cell below that iterates through the words in file_contents, removes punctuation,
# # and counts the frequency of each word. Oh, and be sure to make it ignore word case,
# # words that do not contain all alphabets and boring words like "and" or "the".
# # Then use it in the generate_from_frequencies function to generate your very own word cloud!
# # Hint: Try storing the results of your iteration in a dictionary before passing them into
# # wordcloud via the generate_from_frequencies function.
#
# def calculate_frequencies(file_contents):
#     # Here is a list of punctuations and uninteresting words you can use to process your text
#     punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#     uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
#                            "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
#                            "they", "them", \
#                            "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be",
#                            "been", "being", \
#                            "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when",
#                            "where", "how", \
#                            "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very",
#                            "can", "will", "just"]
#
#     # LEARNER CODE STARTS HERE
#     frequencies = {}
#     taken = []
#     for letter in punctuations:
#         file_contents = file_contents.replace(letter, '')
#     for word in uninteresting_words:
#         w = ' ' + word + ' '
#         file_contents = file_contents.replace(w, ' ')
#     for word in file_contents.split():
#         if word.lower() not in taken:
#             taken.append(word.lower())
#             if word not in frequencies:
#                 frequencies[word] = 1
#             else:
#                 frequencies[word] += 1
#
#                 # wordcloud
#     cloud = wordcloud.WordCloud()
#     cloud.generate_from_frequencies(frequencies)
#     return cloud.to_array()
#
# # If you have done everything correctly, your word cloud image should appear after running the cell below. Fingers crossed!
#
# # Display your wordcloud image
#
# myimage = calculate_frequencies(file_contents)
# plt.imshow(myimage, interpolation = 'nearest')
# plt.axis('off')
# plt.show()

# #class Solution(object):
# def fizzBuzz(n):
#     """
#     :type n: int
#     :rtype: List[str]
#     """
#     for i in range(1, n + 1):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(str(i))
#
#
# print(fizzBuzz(15))

# #!/bin/python3
# import math
# import os
# import random
# import re
# import sys
# #
# # Complete the 'findNumber' function below.
# #
# # The function is expected to return a STRING.
# # The function accepts following parameters:
# #  1. INTEGER_ARRAY arr
# #  2. INTEGER k
# #
# def findNumber(arr, k):
#     # Write your code here
#     if k in arr:
#         return "YES"
#     else:
#         return "NO"
#
# print(findNumber([1, 3, 4, 5], 2))

#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'oddNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

# def oddNumbers(l, r):
#     # Write your code here
#     result = []
#     for i in range(l, r + 1):
#         if i % 2 != 0:
#             result.append(i)
#     return result
#
# print(oddNumbers(2, 9))

#!/bin/python3

# import math
# import os
# import random
# import re
# import sys
# from collections import Counter
#
# # Complete the sockMerchant function below.
# def sockMerchant(n, ar):
#     pairs = 0
#     for val in Counter(ar).values():
#         pairs += val//2
#     return pairs
#
# print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))

# #!/bin/python3
#
# import math
# import os
# import random
# import re
# import sys
#
# # Complete the countingValleys function below.
# def countingValleys(n, s):
#     valley_num = 0
#     level = 0
#
#     for i in range(n):
#         if s[i] == 'U':
#             level += 1
#         else:
#             if level == 0:
#                 valley_num += 1
#             level -= 1
#     return valley_num
#
# print(countingValleys(8, "UDDDUDUU"))

#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'isPangram' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY pangram as parameter.

# def isPangramString(string):
#     # Write your code here
#     a = "abcdefghijklmnopqrstuvxyz"
#     for i in a:
#         if i not in string:
#             return False
#     return True
#
# def isPangram(pangram):
#     result = ''
#     for s in pangram:
#         if isPangramString(s):
#             result += str(1)
#         else:
#             result += str(0)
#
#     return result
#
# print(isPangramString('abcdefghijklmnopqrstuvxyzabcdefghijklmnopqrstuvxyz'))
# print(isPangram(' '))

# def checkPangram(s):
#     List = []
#     # create list of 26 charecters and set false each entry
#     for i in range(26):
#         List.append(False)
#     # converting the sentence to lowercase and iterating
#     # over the sentence
#     for c in s.lower():
#         if not c == " ":
#             # make the corresponding entry True
#             List[ord(c) -ord('a')]= True
#     # check if any charecter is missing then return False
#     for ch in List:
#         if ch == False:
#             return False
#
# print(checkPangram('abcdefghijklmnopqrstuvxyz'))

# #!/bin/python3
# import math
# import os
# import random
# import re
# import sys
#
# # Complete the jumpingOnClouds function below.
# def jumpingOnClouds(c):
#     step = 0
#     index = 0
#     top = len(c)
#     while(True):
#         if index + 2 >= top - 1:
#             step += 1
#             break
#         elif c[index + 2] == 0:
#             step += 1
#             index += 2
#         elif c[index + 1] == 0:
#             step += 1
#             index += 1
#     return step
#
# print(jumpingOnClouds([0, 0, 0, 0, 1, 0]))

#!/bin/python3
import math
import os
import random
import re
import sys

# # Complete the repeatedString function below:
# def repeatedString(s, n):
#     if s.count('a') == 0:
#         return 0
#     elif len(s) == 1 and s == 'a':
#         return n
#     else:
#         return s.count('a') * int(n/len(s)) + s[:n%len(s)].count('a')
#
# print(repeatedString('aa', 10))

# num = int(input("Enter the number: "))
# if num > 0:
#     print(num, 'is positive')
#     print(num, 'squared is: ', num * num)
# print('Bye')

# class Cars:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def car_presents_itself(self):
#         print('Make: {}; Model: {}; Year: {}.'.format(self.make, self.model, self.year))
#
# car_1 = Cars("Suzuki", "Forenza", 2008)
# #print(car_1.make, car_1.make, car_1.year)
# car_1.car_presents_itself()
#
# car_2 = Cars("Toyota", "CHR", 2018)
# #print(car_2.make, car_2.make, car_2.year)
# car_2.car_presents_itself()

class Animals:
    def __init__(self, name, age): #constructor
        self.name = str(input(f'Enter the animal name: '))
        self.age = int(input(f'Enter the {self.name} age: '))

    def animal_sucks(self):
        print(self.name, 'sucks', self.age, 'years.')

    def animal_jumps(self):
        if self.age < 100:
            print(self.name, 'jumps.')
        if self.age >= 100:
            print(self.name, 'is too old to jump.')


animal_1 = Animals("Sveta", 55) #substance

print(f'Animal name: {animal_1.name}.') # attribute
print(f'Animal age: {animal_1.age}.') # attribute
animal_1.animal_sucks() # method
animal_1.animal_jumps() # method

animal_2 = Animals("Dina", 100) #substance

print(f'Animal name: {animal_2.name}.') # attribute
print(f'Animal age: {animal_2.age}.') # attribute
animal_2.animal_sucks() # method
animal_2.animal_jumps() # method

