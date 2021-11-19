# # 1. bubble sort

# numbers = [6,7,8,9,3,4,5,1,2,0]
# print(f'Before sorting: {numbers}')
# for i in range(len(numbers)):
#     for j in range(len(numbers)-i-1):
#         if numbers[j] > numbers[j+1]:
#             numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
# print(f'After sorting: {numbers}')

# numbers = [6,7,8,9,3,4,5,1,2,0]
# print(f'Before sorting: {numbers}')
# swaps = True
# while swaps:
#     swaps = False
#     for j in range(len(numbers)-1):
#         if numbers[j] > numbers[j+1]:
#             swaps = True
#             numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
# print(f'After sorting: {numbers}')

# 2. factorial of the integer
# 2.1. Recursion, in Python no > 1000
# number = int(input('Enter the integer: ')) # 3
# def factor(n):
#     if n == 0:
#         return 1
#     return factor(n-1) * n
# print(f'Factorial of {number} = {factor(number)}')

# # 2.1. Loop
# number = int(input('Enter the integer: ')) # The simple answer is = is an assignment operator, == is a comparison operator
# def factorial(n):
#     if n == 0:
#         return 1
#     f = 1
#     i = 0
#     while i < n:
#         i += 1
#         f = f * i
#     return  f
# print(f'Factorial of {number} = {factorial(number)}')

# 3. fibonacci

# f1 = f2 = 1
# n = int(input('Enter the number: '))
# for i in range(1, n + 1):
#     f1, f2 = f2, f1 + f2 # summ of the two preceeding numbers
#     print(f1, end=' ') # end=' ' - In Python 3, "end =' '" appends space instead of newline.

# def fib():
#     f1, f2 = 0, 1
#
#     while True:
#         yield f1
#         f1, f2 = f2, f1 + f2
#
# for i, f in zip(range((int(input('Enter the number: ')))+1), fib()):
#     print("{i:1}:{f:1}".format(i=i,f=f))

# # Length of Levenstein
#
# def dist(a, b):
#     def rec(i, j):
#         if i == 0 or j == 0:
#             # if string is empthy, length is equal its length(n inserts)
#             return max(i, j)
#         elif a[i-1] == b[j-1]:
#             # if last characters are the same, just eat them up
#             return rec(i - 1, j - 1)
#         else:
#             # else we count the minimal variant
#             return  1 + min(
#                 rec(i, j-1), # deleting the character
#                 rec(i-1, j), # entering the character
#                 rec(i-1, j-1), # changing the character
#             )
#     return rec(len(a), len(b))
#
# str1 = input('Enter the string1: ')
# str2 = input('Enter the string2: ')
#
# lev = dist(str1, str2)
# bigger = max([len(str1), len(str2)])
# prcnt = round(((bigger - lev) / bigger) * 100, 2)
#
# print('Length of Levenstein: ' + str(lev))
# print(f"String #1: {str1}/nString #2: {str2}\n===Alikeness: {prcnt}".format(str1=str1, str2=str2,prcnt=prcnt))
#
# # Односвязный список
#
# class Node:
#     # ячейка списка
#     def  __init__(self, value=None, next=None):
#         self.value=value
#         self.next=next
#
# class LinkedList:
#     # односвязный список
#     def __init__(self):
#         self.head=None
#         self.tail=None
#         self.length=0
#
#     def __str__(self):
#         if self.head!=None:
#             c=self.head
#             out="LinkedList [" + str(c.value)
#             while c.next!=None:
#                 c=c.next
#                 out+=", " + str(c.value)
#             out+="]"
#             return out
#         else:
#             return "LinkedList[]"
#
#     def add(self, n):
#         self.length+=1
#
#         if self.head==None:
#             self.head=self.tail=Node(n, None)
#         else:
#             self.tail.next=self.tail=Node(n,None)
#
#     def reverse(self):
#         # Разворачивание односвязного списка
#         pNode=None
#         cNode=self.head
#         nNode=cNode.next
#
#         self.tail=cNode
#
#         while nNode!=None:
#             cNode.next=pNode
#             pNode=cNode
#             cNode=nNode
#             nNode=cNode.next
#
#         cNode.next=pNode
#         self.head=cNode
#
# L=LinkedList()
#
# L.add(1)
# L.add(2)
# L.add(3)
# L.add(4)
#
# print(L)
#
# L.reverse()
#
# print(L)

# Recursion  Functions

# 1 privet
# 2 privet n times
# 3 sum 0+1+2+3+4+5
# 4 factorial 5! = 1*2*3*4*5 =120
# 5 Fibonacci 0,1,1,2,3,5,8,13,21,34,55

# # 1 privet
# def privet():
#     print("Hello, world!")
#     privet()
#
# privet()

# # 2 privet n times
# def privet(x):
#     if x == 0:
#         return
#     else:
#         print("Hello, world!")
#         privet(x-1)
#
# privet(int(input("Enter how many times: ")))

# # 3 sum 0+1+2+3+4+5
# def sum(x):
#     if x == 0:
#         return 0
#     elif x == 1:
#         return 1
#     else:
#         return x + sum(x-1)
#
# z = sum(int(input("Enter the quantity: ")))
# print(z)

# # 4 factorial 5! = 1*2*3*4*5 =120
# def factorial(x):
#     if x == 0:
#         return 1
#     else:
#         return x * factorial(x - 1)
#
# z = factorial(int(input("Enter the quantity: ")))
# print(z)

# # 5 Fibonacci 0,1,1,2,3,5,8,13,21,34,55
# def fibonacci(x):
#     if x == 0:
#         return 0
#     elif x == 1:
#         return 1
#     else:
#         return fibonacci(x - 1) + fibonacci(x - 2)
#
# z = fibonacci(int(input("Enter the quantity: ")))
# print(z)

# Power
# def power(a,n):
#     if n == 0:
#         return 1
#     elif n % 2 == 1:
#         return power(a, n - 1) * a
#     else:
#         return power(a, n // 2) ** 2
# z = power((int(input("Enter the number: "))), (int(input("Enter the power: "))))
# print(z)

# Split list into two, with odd and even integers only
# def even_odd(message):
#     even = []
#     odd = []
#     for i in message:
#         if i.isdigit():
#             if int(i) % 2 == 0:
#                 even.append(str(i))
#             else:
#                 odd.append(str(i))
#     print(f'Total: {str(len(message))} in input: {message}')
#     print("Even: " + ','.join(even) + ', Total even: ' + str(len(even)))
#     print("Odd: " + ','.join(odd) + ', Total even: ' + str(len(odd)))
# print(even_odd(input("Enter the integers: ")))

# # Automation benefits
# n = int(input('Enter the builds number: ')) # 10, 20, 30, 40
# t_m = 30 #int(input('Enter the time for build manual: ')) # 30
# t_a = 5 # int(input('Enter the time for build automation: ')) # 5
# t_a_d = 300 # int(input('Enter the time for project automation development: ')) # 300
# effect = (n * t_a + t_a_d) - n * t_m
# if n * t_m >= n * t_a + t_a_d:
#     print(f'Time to start automation! Effect is : {n * t_m - (n * t_a + t_a_d)} hours') # 12 builds is the treshhold
# print(f'Time for manual: {n * t_m}')
# print(f'Time for automation: {n * t_a + t_a_d}')

# # Interview preparation
# l = [1,2,3,4,5,6,7] # Input
# def sum_list(l):
#     s_l = 0
#     for i in l:
#         s_l += i
#     return s_l # Output
# print(sum_list(l))

# # Interview preparation
# # Example 1:
# # Input: nums = [2,7,11,15], target = 9
# # Output: [0,1]
# # Output: Because nums[0] + nums[1] == 9, we return [0, 1].
#
# # Example 2:
# # Input: nums = [3,2,4], target = 6
# # Output: [1,2]
#
# nums = [2,7,11,15]
# target = 9
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i]  + nums[j] == target:
#             print(f'{nums[i]}"{i}"+{nums[j]}"{j}"={target}')

# def reverse(x = int(input('Enter the integer: '))):
#     if x >= 0:
#         num = int(str(x)[::-1])
#     else:
#         num = int(str(x)[1:][::-1]) * (-1)
#     if abs(num) > 2 ** 31 - 1:
#         return 0
#     else:
#         return num
# print(reverse())

# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
# Example 1:
# Input: 121
# Output: true

# def num_reversed(x = (input("Enter the integer: "))):
#     return int(x[::-1])
# print(f'{num_reversed()}, {type(num_reversed())}')

# def num_palyndrome(x = int(input("Enter the integer: "))):
#     x_s = str(x)
#     if x_s == (x_s[::-1]):
#         return 'It is a palyndrome'
#     else:
#         return 'It is not a palyndrome'
# print(f'{num_palyndrome()}, {type(num_palyndrome())}')


# def i_p(i=int(input('Enter the integer: '))):
# 	res = [int(x) for x in str(i)]
# 	if res==res[::-1]:
# 		return 'Palindrome'
# 	else:
# 		return 'Not palindrome'
# print(i_p(), type(i_p()))

# def isPalindrome(x: int) -> bool:
#     new_n=0
#     n=x
#     while n>0:
#         new_n=new_n*10+n%10
#         n=n//10
#         print(new_n)
#     return x == new_n
# print(isPalindrome(x=int(input('Enter the integer: '))))

# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i]  + nums[j] == target:
#             print(f'{nums[i]}"{i}"+{nums[j]}"{j}"={target}')

# Example 2:
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# Follow up:
# Could you solve it without converting the integer to a string?

# # Python program to find number
# # is palindrome or not without
# # using any extra space
# # Function to check if given number
# # is palindrome or not without
# # using the extra space
# def isPalindrome(n):
#     # Find the appropriate divisor
#     # to extract the leading digit
#     divisor = 1
#     while (n / divisor >= 10):
#         divisor *= 10
#
#     while (n != 0):
#
#         leading = n // divisor
#         trailing = n % 10
#
#         # If first and last digit
#         # not same return false
#         if (leading != trailing):
#             return False
#
#         # Removing the leading and
#         # trailing digit from number
#         n = (n % divisor) // 10
#
#         # Reducing divisor by a factor
#         # of 2 as 2 digits are dropped
#         divisor = divisor / 100
#
#     return True
#
# # Driver code
# if (isPalindrome(n = (int(input("Enter the integer: "))))):
#     print('Yes, it is palindrome')
# else:
#     print('No, not palindrome')
#     # This code is contributed by Danish Raza


# # Issue 1
# def sentenceMatchesPattern(pattern, sentence):
# 	pattern_list=list(pattern)
# 	sentence_list=sentence.split(" ")
# 	if len(pattern_list)!=len(sentence_list):
# 		return False
# 	associations={}
# 	associations[pattern_list[0]]=sentence_list[0]
# 	for i in range(1, len(pattern_list)):
# 		if pattern_list[i] in associations:
# 			if associations[pattern_list[i]]!=sentence_list[i]:
# 				return False
# 		else:
# 			if sentence_list[i] not in associations.values():
# 				associations[pattern_list[i]]=sentence_list[i]
# 			else:
# 				return False
#
# 	return True
#
# print(sentenceMatchesPattern('aa', 'bye bye'))


# # Issue 2
# #----------  problem 2  ----------#
# Given a list of all railroads connecting pairs of cities,
# output whether it's possible to travel from an origin city to a destination city by train

# #----------  method signature  ----------#
# public boolean canTravel(String[][] railroads, String originCity, String destinationCity)

# #----------  examples  ----------#
# String[][] railroads = {
#     {"Sydney", "Melbourne"},
#     {"Perth", "Sydney"},
#     {"Melbourne", "Brisbane"},
#     {"New York", "Seattle"},
#     {"New York", "San Francisco"},
#     {"San Francisco", "Portland"},
#     {"Seattle", "Portland"},
#     {"Austin", "Seattle"},
# };;

# originCity: "Seattle"
# destinationCity: "New York"
# ouput: true

# originCity: "San Francisco"
# destinationCity: "Seattle"
# ouput: true

# originCity: "Sydney"
# destinationCity: "Seattle"
# ouput: false

# originCity: "Seattle"
# destinationCity: "Melbourne"
# ouput: false

# originCity: "Perth"
# destinationCity: "Brisbane"
# ouput: true


# class treeNode:
#     def __init__(self, city, next):
#         self.city = city
#         self.next = next
#
#     def __repr__(self):
#         return "({} | {})".format(self.city, self.next)
#
#
# def canTravel(railroads, originCity, destinationCity):
#     if originCity in [road for roadlist in railroads for road in roadlist]:
#         tree = treeNode(originCity, list())
#     else:
#         return False
#     return add_new_nodes(tree, railroads, destinationCity)
#
#
# def add_new_nodes(tree, roads, destinationCity):
#     to_delete = []
#     for road in roads:
#         if road[0] == tree.city:
#             new_node = treeNode(road[1], list())
#             tree.next.append(new_node)
#             to_delete.append(road)
#
#         if road[1] == tree.city:
#             new_node = treeNode(road[0], list())
#             tree.next.append(new_node)
#             to_delete.append(road)
#
#     if len(to_delete) == 0:
#         return False
#
#     for item in to_delete:
#         roads.remove(item)
#
#     for node in tree.next:
#         if node.city == destinationCity:
#             return True
#         else:
#             return add_new_nodes(node, roads, destinationCity)
#
#
# railroads = [
#     ["Sydney", "Melbourne"],
#     ["Perth", "Sydney"],
#     ["Melbourne", "Brisbane"],
#     ["New York", "Seattle"],
#     ["New York", "San Francisco"],
#     ["San Francisco", "Portland"],
#     ["Seattle", "Portland"],
#     ["Austin", "Seattle"]]
#
# print(canTravel(railroads[:], "San Francisco", "New York"))
# print(canTravel(railroads[:], "San Francisco", "Seattle"))
# print(canTravel(railroads[:], "Sydney", "Seattle"))
# print(canTravel(railroads[:], "Seattle", "Melbourne"))
# print(canTravel(railroads[:], "Perth", "Brisbane"))

# ex_str = (str(input('Enter the string: ')))
# reversed_ex_str = ex_str[::-1]
# print(reversed_ex_str)

# # If 2 values are equal, then print EQUAL. If 2 values are not EQUAL print NOT. If
# # they are SAME, print SUCCESS.
# def compare(a, b):
#     if a is b:
#         return "SUCCESS!"
#     if a==b:
#         return "EQUAL"
#     if a!=b:
#         return "NOT"
#
# print(compare(5, 6))
# print(compare(5, 5))
# print(compare('c', 'c'))

# 10 oct 2020
# https://app.testdome.com/apply/2c54d53fdf234f8fbd10f3054dcdd3ed

# def isCentenarian(age):
#     if age >= 100:
#         return True
#     else:
#         return False
# print(isCentenarian(int(input('Enter the age: '))))

# def greet(bot_name, birth_year):
#     print('Hello! My name is ' + bot_name + '.')
#     print('I was created in ' + birth_year + '.')
#
#
# def remind_name():
#     print('Please, remind me your name.')
#     name = input('Enter the name: ')
#     print('What a great name you have, ' + name + '!')
#
#
# def guess_age():
#     print('Let me guess your age.')
#     print('Enter remainders of dividing your age by 3, 5 and 7.')
#
#     rem3 = int(input())
#     rem5 = int(input())
#     rem7 = int(input())
#     age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
#
#     print("Your age is " + str(age) + "; that's a good time to start programming!")
#
#
# def count():
#     print('Now I will prove to you that I can count to any number you want.')
#
#     num = int(input())
#     curr = 0
#     while curr <= num:
#         print(curr, '!')
#         curr = curr + 1
#
#
# def test(): #self, to_rep, te_decomp, to_determ, to_interr
#     print("\nLet's test your programming knowledge.\n")
#     # write your code here
#     print('Why do we use methods?\n')
#     print('1. To repeat a statement multiple times.')
#     print('2. To decompose a program into several small subroutines.')
#     print('3. To determine the execution time of a program.')
#     print('4. To interrupt the execution of a program.\n')
#     answer = str(input(f'Enter 1 if you choosen 1\n'
#                        f'Enter 2 if you choosen 2\n'
#                        f'Enter 3 if you choosen 3\n'
#                        f'Enter 4 if you choosen 4\n'))
#     if '2' in answer:
#         print('\nCompleted, have a nice day!\n')
#     else:
#         print('\nPlease, try again.\n')
#
# def end():
#     print('Congratulations, have a nice day!')
#
#
# greet('Aid', '2020')  # change it as you need
# remind_name()
# guess_age()
# count()
# test()
# # ...
# end()




# # 1.     С помощью команды input введите трехзначное число и найдите сумму его цифр.
#
# thr_dgits_nm=int(input('Enter the three digits number: '))
# def three_digits_sum(thr_dgits_nm):
#     if 99 < thr_dgits_nm < 1000:
#         print(f'You entered number: "{thr_dgits_nm}"')
#     else:
#         print(f'Wrong input, enter the three digits number!\n')
#         return False
#     tp_x = type(thr_dgits_nm)
#     y = thr_dgits_nm
#     summ = 0
#     while y >= 1:
#         rem = y%10 # modulus
#         y = y//10 # floor division
#         summ += rem
#     print (f'Sum of three digits number is: "{summ}"" and its type: "{tp_x}"\n')
# three_digits_sum(thr_dgits_nm)
#
# # 2.     С помощью команды input введите число сторон правильного многоугольника и найдите сумму его внутренних углов. Сумма углов n-угольника равна 180*(n-2).
# sds_plyngl = int(input('Enter the right poly angle quantity sides: '))
# if sds_plyngl >= 3:
#   sm_of_ngls = 180 * (sds_plyngl - 2)
#   print(f'Sum of internal angles of right poly angle with "{sds_plyngl}" sides is: "{sm_of_ngls}" degrees\n')
# else:
#   print(f'Wrong input, the poly angles can not have less than three angles!\n')
#
# # 3.     С помощью команды input запросите у пользователя количество миль (miles). Переведите это расстояние в километры и футы. 1 mile = 1.60934 km, 1 mile = 5280 feet.
# mls_frm_usr = float(input('Enter the miles quantity: '))
# mls_to_kms = round(mls_frm_usr * 1.60934, 2)
# mls_to_ft = round(mls_frm_usr * 5280, 2)
# print(f'"{mls_frm_usr}" mile/s = "{mls_to_kms}" km\nand "{mls_frm_usr}" mile/s = "{mls_to_ft}" feet\n')
#
# # 4.     С помощью команды input запросите у пользователя число градусов Фаренгейта (fahrenheit) и переведите это значение в градусы Цельсия (celsius). Для этого нужно от числа градусов Фаренгейта отнять 32, результат умножить на 5 и затем поделить на 9.
# frnht_frm_usr = float(input('Enter the Fahrenheit temperature: '))
# frnht_to_celsius = round((((frnht_frm_usr - 32) * 5) / 9), 2)
# print(f'Farenheit "{frnht_frm_usr}" = Celsius "{frnht_to_celsius}"\n')
#
# # 5.     С помощью команды input запросите у пользователя стоимость заказа (price), процент чаевых (tip_percent) и процент налогов (tax_percent). Найдите общую стоимость заказа (total_price).
# price = float(input('Enter the order price: '))
# tip_percent = float(input('Enter the tip percent: '))
# tax_percent = float(input('Enter the tax_percent: '))
# total_price = round((price + price * (tip_percent / 100) + (price + price * (tip_percent / 100)) * (tax_percent / 100)), 2)
# print(f'The total is: ${total_price}\n')
#
# # 6.     С помощью команды input введите цену товара со скидкой и процент скидки.
# Найдите цену товара до скидки (полную цену товара), результат округлите до 2-х знаков после запятой.
# Например, товар со скидкой стоит 40 долларов при скидке 50%.
# Тогда цена товара без скидки составляет 80 долларов. Если товар стоит 40 долларов при скидке 10 процентов,
# его полная цена составляет $ 44.44.
# itm_w_dscnt = float(input('Enter the price on item with discount: '))
# dscnt_itself = float(input('Enter the discount: '))
# itm_bfr_dscnt = round((itm_w_dscnt / ((100 - dscnt_itself) / 100)), 2)
# print(f'Item price before discount is ${itm_bfr_dscnt}')

# print('#3')
# string = (input('Enter the 10 digits number: '))
# processed_string = (f'(+{string[:3]}) {string[3:6]}-{string[6:]}')
# len_string = len(string)
# if len_string == 10:
#     print(f'{processed_string}\n')
# else:
#     print(f'Wrong input, enter the ten digits number!\n')

# # 1.    В переменную name введите имя. Определите, начинается ли имя с гласной буквы.
# print('#1')
# name = str(input('Enter the name: ')).lower()
# if name[:1] in 'aeuioу':
#   desc_name = 'Name starts from the vowel.\n'
# elif name[:1] in 'аоиеёэыуюя':
#   desc_name = 'Имя начинается с гласной буквы.\n'
# elif name[:1] in 'zxcvbnmsdfghjklqwrtp':
#   desc_name = 'Name starts from the consonant.\n'
# elif name[:1] in 'бвгджзйклмнпрстфхцчшщ':
#   desc_name = 'Имя начинается с согласной буквы.\n'
# else:
#   desc_name = 'Name starts from the wrong charachter.\n'
# print(desc_name)
# # 2.    С помощью команды input введите имя пользователя name. Если имя содержит более 5 букв, напечатайте "Your name is long!". В противном случае напечатайте "Your name is short!"
# print('#2')
# name = str(input('Enter the name: ')).lower()
# print('Your name is long!\n' if len(name) > 5 else 'Your name is short!\n')
# # 3.    С помощью команды input введите имя пользователя name и время time в часах от 0 до 24.
# # ·       Если время от 0 до 6 (включительно), напечатайте "Good night, name";
# # ·       если время от 7 до 11 (включительно), напечатайте "Good morning, name";
# # ·       если время от 12 до 18 (включительно), напечатайте "Good day, name";
# # ·       если время от 19 до 24 (включительно), напечатайте "Good night, name";
# # ·       иначе напечатайте "Wrong time".
# print('#3')
# name = str(input('Enter the name: '))
# time = int(float(input('Enter the time in hours from 0 to 24: ')))
# if 0 <= time <= 6:
#   desc_name = (f'Good night, {name}, it is {time}.\n')
# elif 7 <= time <= 11:
#   desc_name = (f'Good morning, {name}, it is {time}.\n')
# elif 12 <= time <= 18:
#   desc_name = (f'Good day, {name}, it is {time}.\n')
# elif 19 <= time <= 24:
#   desc_name = (f'Good night, {name}, it is {time}.\n')
# else:
#   desc_name = (f'Wrong time.\n')
# print(desc_name)
# # 4.    Введите цену товара price.
# # ·       Если price >= 300, вы получаете скидку 30%;
# # ·       иначе если price >= 200, вы получаете скидку 20%;
# # ·       иначе если price >= 100, вы получаете скидку 10%;
# # ·       если цена меньше 100, скидки нет. Найдите итоговую стоимость товара.
# print('#4')
# price = round(float(input('Enter the price: ')), 2)
# if price >= 300:
#   desc_price = (f'If price ${price}, your discount is 30%. Total price is ${round(price * 0.7, 2)}\n')
# elif price >= 200:
#   desc_price = (f'If price ${price}, your discount is 20%. Total price is ${round(price * 0.8, 2)}\n')
# elif price >= 100:
#   desc_price = (f'If price ${price}, your discount is 10%. Total price is ${round(price * 0.9, 2)}\n')
# elif price < 100:
#   desc_price = (f'If price ${price}, your discount is 0%. Total price is ${round(price, 2)}\n')
# else:
#   desc_price = (f'Wrong price format\n')
# print(desc_price)
# # 5.    Введите возраст человека age.
# # ·       Если age<16 напечатайте "children";
# # ·       иначе если age<50 напечатайте "young man";
# # ·       иначе напечатайте "senior".
# print('#5')
# age = (round(float(input('Enter the age: ')), 0))
# if 0 < (age) < 16:
#   desc_age = (f'Children.\n')
# elif 16 <= (age) <= 50:
#   desc_age = (f'Young man.\n')
# elif 50 < (age):
#   desc_age = (f'Senior.\n')
# else:
#   desc_age = (f'Error.\n')
# print(desc_age)
# # 6.    В переменную current_color введите цвет сигнала светофора ('red','yellow','green'). Напечатайте следующий цвет сигнала светофора (смена цветов такая: 'red' ---> 'green', 'green' ---> 'yellow', 'yellow' ---> 'red').
# print('#6')
# current_color = str(input("Enter the traffic light color: ")).lower()
# if current_color == 'red':
#   desc_color = (f'If current color is "{current_color}" next is "green".\n')
# elif current_color == 'green':
#   desc_color = (f'If current color is "{current_color}" next is "yellow".\n')
# elif current_color == 'yellow':
#   desc_color = (f'If current color is "{current_color}" next is "red".\n')
# else:
#   desc_color = (f'Wrong input\n')
# print(desc_color)
# # 7.    Дана переменная num_of_day, хранящая номер дня недели. Присвоить переменой day значение “ Weekend”, если номер дня 6 или 7, и “Work day” в противном случае. Выполните это задание с использованием тернарного оператора.
# print('#7')
# num_of_day = int(input('Enter the day number: ')) # (round(input('Enter the day number: ')), 0)).isdigit()
# # day = 'Weekend.' if num_of_day in range(6, 8) else 'Work day.'
# if 1 <= num_of_day <= 5:
#   output_day = 'Work day.'
# elif 6 <= num_of_day <= 7:
#   output_day = 'Weekend.'
# else:
#   output_day = 'Enter the day number from 1 to 7'
# print(f'{output_day}\n')
# # 8.    Дано число n. Число является "счастливым", если оно делится на 9. Присвойте переменной is_lucky значение "Lucky number", если число делится на 9, и "Not a lucky number" в противном случае. Выполните это задание с использованием тернарного оператора.
# print('#8')
# n = (round(float(input('Enter the integer: ')), 0))
# is_lucky = 'Lucky number.' if n % 9 == 0 else 'Not a lucky number.'
# print(f'{is_lucky}\n')
# print(f'The end')

# # Домашнее задание № 5. Тема: Функции работы со строками
# # 1. Создайте переменную phrase и присвойте ей значение "My eyes are green too!" С помощью команды input спросите у пользователя "What is your favorite color? " Замените слово "green" в переменной phrase на любимый цвет пользователя и напечатайте полученную фразу.
# print('#1')
# phrase = "My eyes are green too!"
# print(phrase)
# ask_user = str(input('What is your favorite color? '))
# print(phrase.replace("green", ask_user) + "\n")
# # 2. С помощью функции input введите first_name, middle_name, last_name. Выведите эти три слова в столбик, выравнивание по правому краю в строке с длиной, равной длине самого длинного из имен. Используйте функцию max для нахождения максимальной длины слов.
# #       Ava
# # Charlotte
# #     Smith
# print('#2')
# first_name = str(input('Enter the first name: '))
# middle_name = str(input('Enter the middle name: '))
# last_name = str(input('Enter the last name: '))
# max_len = max(len(first_name), len(middle_name), len(last_name))
# print(f'{first_name.rjust(max_len)}\n{middle_name.rjust(max_len)}\n{last_name.rjust(max_len)}\n')
# # 3. Создайте переменную s и присвойте ей значение произвольной строки. Удалите в этой строке все гласные буквы. Например, s = “We like Python”. Результат должен быть “W lk Pythn”.
# print('#3')
# s = str(input('Enter the all you want: '))
# vowels = ('a', 'e', 'i', 'o', 'u')
# for x in s.lower():
#   if x in vowels:
#     s = s.replace(x, "")
# print(f'{s}\n')
# # 4. С помощью команды input введите строку. Затем введите слово, которое надо заменить. Потом введите заменяющее слово. Выведите результат. Например, введены: строка "Have a good day", слово "good", слово "nice". Результат должен быть: "Have a nice day".
# print('#4')
# s = str(input('Enter the all you want: ')) # We love Python
# wrd_t_rplc = str(input('Enter the word you want to replace: ')) # love
# wrd_by_rplc = str(input('Enter the word by what to replace: ')) # hate
# print(f'{s.replace(wrd_t_rplc, wrd_by_rplc)}\n')
# # 5. Задана строка. В начале и конце строки есть некоторое количество пробелов. Получить строку, в которой каждое слово написано в заглавной буквы, пробелы в начале строки удалены, а пробелы в конце строки заменены на такое же количество восклицательных знаков. Например, s = "   I like summer  ". Получить "s = "I Like Summer!!!"
# print('#5')
# s = "   I like summer  "
# s_lstr = s.lstrip().title() # align to left and capitalize all words
# s_rstr = s_lstr.rstrip() # align to right
# s_r_spcs = s_lstr.count(" ") # count spaces at the right side
# print(s_rstr + s_r_spcs * "!")

# # Домашнее задание № 6. Циклы
# # 1.     Постройте строку “1 monkey 2 monkeys ... 10 monkeys”.
# print('\n#1\n')
# n = int(input('Enter the N positive integer monkeys quantity: '))
# for x in range(1, n + 1):
#   if n > 0:
#     while x == 1:
#       print(x, 'monkey', end = " ")
#       x += 1
#       while 1 < x <= n:
#         print(x, 'monkeys', end = " ")
#         x += 1
#     break
# else:
#   print(f'Enter the positive integer')
# print("\n")
# # 2.     Составьте строку, которая "отсчитывает" секунды до старта ракеты:
# # "10 seconds...9 seconds...8 seconds...7 seconds...6 seconds...5 seconds...4 seconds...3 seconds...2 seconds...1 second"
# print('#2\n')
# n = int(input('Enter the N positive integer for the final countdown: '))
# for x in range(n, 0, -1):
#   if n > 0:
#     while n >= x > 1:
#       print(x, 'seconds', end=" ")
#       x -= 1
#     while x == 1:
#       print(x, 'second', end=" ")
#       x -= 1
#     break
# else:
#   print(f'Enter the positive integer')
# print("\n")
# # 3.     Возведите число n в степень k, не используя операцию возведения в степень (n, k ввести с помощью input). Для того чтобы возвести число n в степень k, его необходимо k раз умножить на само себя.
# print('#3\n')
# n = float(input('Enter the number N to be powered: '))
# k = float(input('Enter the power K: '))
# n_n = 1
# k_k = 1
# while k_k <= k: # quantity of times n multiply by itself
#   n_n *= n
#   k_k += 1
# print(f'{n} in power of {k} = {round(n_n, 2)}')
# # 4.     В первый день тренировок спортсмен пробежал 5 км. В каждый последующий день он пробегал на 5% больше, чем в предыдущий день. Напечатайте, сколько километров спортсмен пробегал каждый день в течение 10 дней.
# print('\n#4\n')
# km_d = 5
# for days in range(1, 11):
#   km_d = km_d * 1.05
#   print(f'{days} day = {round(km_d, 2)} km')
# # 5.     Ученик к моменту начала обучения не знает ни одного английского слова.
# # В первый день занятий он выучил 5 английских слов.
# # В каждый последующий день он выучивал на 2 слова больше, чем в предыдущий.
# # Через сколько дней ученик будет знать не менее n английских слов?
# print('\n#5\n')
# n = int(input('Enter the quantity of English words: '))
# words_first_day = 5
# day = 0
# number_of_words = 0
# while number_of_words < n:
#   day += 1
#   number_of_words += words_first_day
#   words_first_day += 2
# print(f'{n} words would be learnt at the {day} day. And total {number_of_words} words would be learnt on {day} day.' )
# # 6.     Получите строку, содержащую лесенку. Число «ступенек» ввести командой input.
# # #
# #  #
# #   #
# #    #
# #     #
# print('\n#6')
# s = ""
# n = int(input('Enter the amount of layers: '))
# for x in range(1, n + 1):
#   s = s + " " * x + "#" + "\n"
# s = s[:-1]
# print(s)
# # 7.     Нарисуйте ромб. Ширину (нечетное число, в данном примере это 7) ввести командой input.
# # Используйте выравнивание строки по центру.
# #     *
# #    ***
# #   *****
# #  *******
# #   *****
# #    ***
# #     *
# print('\n#7\n')
# s = 0
# k = 1
# n = int(input('Enter the thickness: '))
# if n % 2 != 0:
#   for i in range(1, n + 1):
#     print(" " * ((n - k) // 2) + "*" * k + " " * ((n - k) // 2))
#     if k == n:
#       s = 1
#     if s == 0:
#       k += 2
#     else:
#       k -= 2
# else:
#   print(f'Enter the odd integer')
  
# # Домашнее задание № 7. Тема Циклы. Работа со строками
# # 1.     Посчитайте количество заглавных букв в строке.
# print('\n#1\n')
# s = str(input('Enter the string: '))
# count = 0
# for i in s:
#   if i.isupper():
#     count += 1
# print(f'There are "{count}" capital letters in the string.')
# print('\n#2\n')
# # 2.     Посчитайте общее количество гласных в строке (в верхнем и нижнем регистре).
# s = str(input('Enter the string: '))
# count = 0
# for i in s.lower():
#   if i in "aeuioаоиеёэыуюя":
#     count += 1
# print(f'There are "{count}"" vowels in the string.')
# # 3.     Задайте строку с произвольным значением (например, "Python"). Получите строку, в которой все буквы будут разделены звездочками ("P*y*t*h*o*n").
# print('\n#3\n')
# s = str(input('Enter the string: '))
# s_p = ""
# for x in range(len(s)):
#   s_p += s[x] + "*"
# print(f'String processed: "{s_p[:-1]}"')
# # 4.     Вставьте пробелы после всех неалфавитных символов строки (путем создания новой строки). Например, s = "Bananas,2apples,sweets and 8plums". Получить "Bananas, 2 apples, sweets and 8 plums".
# print('\n#4\n')
# s = "Bananas,2apples,sweets and 8plums"
# s_p = ""
# for x in range(len(s)):
#   s_p += s[x]
#   if not s[x].isalpha() and not s[x].isspace():
#     s_p += " "
# print(f'String processed: "{s_p[0:]}"')
#  # 5.     Задайте строку с произвольным значением (например, "summer"). Получите строку, в которой гласные буквы станут заглавными ("sUmmEr").
# print('\n#5\n')
# s = str(input('Enter the string: '))
# s_p = ""
# for x in s:
#   if x in "AaEeUuIiOoАаЕеЁёИиЙйОоУуЫыЭэЮюЯя":
#     s_p = s_p + x.upper()
#   else:
#     s_p = s_p + x
# print(f'Input: "{s}" VS output: "{s_p}"')
# # 6.     Дана строка. Получить две новые строки: одну - из символов с четными индексами, другую - из символов с нечетными индексами. Например, s = "separate". Новые строки: "sprt", "eaae".
# print('\n#6\n')
# s = str(input('Enter the string: '))
# t_ev = ''
# t_odd = ''
# for i, element in enumerate(s):
#   if i % 2 == 0:
#     t_ev += element
#   else:
#     t_odd += element
# print(f'Even: {t_ev}, odd: {t_odd}.')
# # 7.     Ввести строку, включающую строчные и прописные буквы. Вывести ту же строку в одном регистре, который зависит от того, каких букв больше. При равном количестве преобразовать в нижний регистр. Например, вводится строка "HeLLo World", она должна быть преобразована в "hello world", потому что в исходной строке малых букв больше.
# print('\n#7\n')
# s = str(input('Enter the string: '))
# s_p = ''
# count_low = 0
# count_upp = 0
# for x in range(len(s)):
#   if s[x].isupper():
#     count_upp += 1
#   else:
#     count_low += 1
# if count_upp <= count_low:
#   print(s.lower())
# else:
#   print(s.upper())


# # Домашнее задание № 8. Функции
# # 1. Напишите функцию с именем opposite, которая принимает число и возвращает противоположное по значению число.
# print("\n#1\n")
# n = float(input('Enter the integer: '))
# def opposite(n):
#   n_o = n * -1
#   return round(n_o, 2)
# print(f'Input "{n}", Output: "{opposite(n)}"')
# # 2. Сумма углов n-угольника равна 180 * (n − 2). Напишите функцию angles_of_polygon, которая принимает аргумент n (число углов) и возвращает сумму углов n-угольника.
# print("\n#2\n")
# def angles_of_polygon(n = int(input('Enter the quantity of the angles of the polygon: '))):
#   if n < 3:
#     return "Enter at least 3 angles!"
#   else:
#     q_a_p = 180 * (n - 2)
#   return (f'Polygon with "{str(n)}" angles has "{str(q_a_p)}" degrees of internal angles')
# print(angles_of_polygon())
# # 3. Напишите функцию с именем miles_to_feet, которая принимает число miles (количество миль) в качестве аргумента и возвращает это расстояние в футах. 1 миля = 5280 футов.
# print("\n#3\n")
# def miles_to_feet(n = float(input('Enter the miles quantity: '))):
#   m_t_f = n * 5280
#   return (f'"{n}" miles = "{str(round(m_t_f, 2))}" feet')
# print(miles_to_feet())
# # 4. Напишите функцию, которая принимает два параметра weight и height. Функция вычисляет индекс массы тела bmi по формуле: bmi = weight / height ** 2 и возвращает описание результата:
# # ·       если bmi <= 18.5, возвратить "Underweight";
# # ·       если bmi <= 25.0, возвратить "Normal";
# # ·       если bmi <= 30.0, возвратить "Overweight";
# # ·       если bmi > 30 , возвратить"Obese".
# print("\n#4\n")
# def weight_height():
#     weight = round(float(input('Enter the weight in kg: ')), 2)
#     height = round(float(input('height in cm: ')), 2)
#     bmi = weight / (height / 100) ** 2
#     if bmi <= 18.5:
#       return (f'Underweight')
#     elif bmi <= 25.0:
#       return (f'Normal')
#     elif bmi <= 30.0:
#       return (f'Overweight')
#     elif bmi > 30:
#       return (f'Obese')
# print(weight_height())
# # 5. Напишите функцию planet_name, которая принимает n - номер планеты от Солнца и возвращает name - название планеты:
# # ·       n = 1: name = "Mercury"
# # ·       n = 2: name = "Venus"
# # ·       n = 3: name = "Earth"
# # ·       n = 4: name = "Mars"
# # ·       n = 5: name = "Jupiter"
# # ·       n = 6: name = "Saturn"
# # ·       n = 7: name = "Uranus"
# # ·       n = 8: name = "Neptune"
# print("\n#5\n")
# class Planet_name:
#   def __init__(self,
#                n
#                ):  # constructor
#
#     self.n = int(input(f'Enter the planet number from 1 to 8: '))
#
#   def planet_number(self):
#     if self.n == 1:
#       print('\nPlanet #1 is: Mercury')
#     elif self.n == 2:
#       return ('\nPlanet #2 is: Venus')
#     elif self.n == 3:
#       return ('\nPlanet #3 is: Earth')
#     elif self.n == 4:
#       return ('\nPlanet #4 is: Mars')
#     elif self.n == 5:
#       return ('\nPlanet #5 is: Jupiter')
#     elif self.n == 6:
#       return ('\nPlanet #6 is: Saturn')
#     elif self.n == 7:
#       return ('\nPlanet #7 is: Uranus')
#     elif self.n == 8:
#       return ('\nPlanet #8 is: Neptune')
#     elif 1 > self.n or self.n > 8:
#       return ('\nEnter the correct number from 1 to 8!')
#     else:
#       return ('\nEnter the correct character!')
# planet_number_1 = Planet_name('')
# planet_number_1.planet_number()
# # 6. Напишите функцию square_of_triangle, которая принимает три аргумента a, b, c (стороны треугольника) и возвращает площадь треугольника, если треугольник существует, или сообщение "The triangle does not exist", в противном случае. Площадь треугольника находится по формуле Герона: area = (p * (p - a) * (p - b) * (p - c)) ** 0.5, где p = (a + b + c) / 2
# print("\n#6\n")
# def square_of_triangle():
#   a = float(input('Enter the length of the first side of the triangle: '))
#   b = float(input('Enter the length of the second side of the triangle: '))
#   c = float(input('Enter the length of the third side of the triangle: '))
#   if a == 0 or b == 0 or c == 0 or a + b < c or a + c < b or b + c  < a:
#     return ("The triangle does not exist")
#   else:
#     p = (a + b + c) / 2
#     area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
#     return (f'Trianlge with the sides "{a}", "{b}", "{c}" has an area "{round(area, 2)}"')
# print(square_of_triangle())
# # 7. Напишите функцию, которая принимает число n и возвращает количество делителей этого числа. Например, число 10 имеет 4 делителей : 1, 2, 5, 10. Число 12 имеет 6 делителей: 1, 2, 3, 4, 6, 12.
# print("\n#7\n")
# def dvdrs_n(n = int(input('Enter the number to divide: '))):
#     m = 0
#     for i in range(1, n+1):
#         if n % i == 0:
#             m += 1
#     return (f'Integer "{n}" has "{m}" dividers')
# print(dvdrs_n())


# # Домашнее задание № 9 Тема: Массивы (списки)
# # 1.     Дан массив, содержащий числа. Найти сумму четных элементов массива.
# print("\n#1\n")
# import array as arr
# a = arr.array('d', [1.8, 3.5, 4.5, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12])
# def ev_sum(a):
#   sum = 0
#   for i in range(len(a)):
#     if a[i] % 2 == 0:
#       sum += a[i]
#   return round(sum, 2)
# print(f'Sum of even numbers in "{a}"\nis "{ev_sum(a)}", quantity of numbers is "{len(a)}".')
# # 2.     Найти произведение нечетных элементов массива.
# print("\n#2\n")
# import array as arr
# b = arr.array('d', [1.8, 3.5, 4.5, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]) # Why repl thinks 1.8 is an odd?
# def odd_production(b):
#   production = 1
#   for i in range(len(b)):
#     if b[i] % 2 != 0:
#       production *= b[i]
#   return round(production, 2)
# print(f'Production of odd numbers in "{b}"\nis "{odd_production(b)}", quantity of numbers is "{len(b)}".')
# # 3.     Найти среднее арифметическое элементов массива.
# print("\n#3\n")
# import array as arr
# c = arr.array('d', [1.8, 3.5, 4.5, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12])
# def median(c):
#   sum = 0
#   for i in range(len(c)):
#     sum += c[i]
#     median = sum / len(c)
#   return round(median, 2)
# print(f'Median of numbers in "{c}"\nis "{median(c)}", quantity of numbers is "{len(c)}".')
# # 4.     Найти количество отрицательных элементов массива.
# print("\n#4\n")
# import array as arr
# d = arr.array('d', [-1.8, -3.5, -4.5, 2, 3, 4, 5, 6, 7, 8, -9, 10, -12])
# def negative(d):
#   sum = 0
#   for i in range(len(d)):
#     if d[i] < 0:
#       sum += d[i]
#   return round(sum, 2)
# print(f'Sum of negative numbers in "{d}"\nis "{negative(d)}", quantity of numbers is "{len(d)}".')
# # 5.     Дан массив, содержащий слова. arr = ["apple", "appricot", "pineapple", "banana", "grape", "plum"].
# # Найдите количество слов длиной 5.
# print("\n#5\n")
# e = ["apple", "appricot", "pineapple", "banana", "grape", "plum"]
# def five_letters(e):
#   sum = 0
#   for i in range(len(e)):
#     if len(e[i]) == 5:
#       sum += 1
#   return sum
# print(f'There are "{five_letters(e)}" words with the length of "5" characters between "{len(e)}" words.')
# # 6.     Дан массив, содержащий слова. arr = ["apple", "appricot", "pineapple", "banana", "grape", "orange"].
# # Найдите количество слов, которые начинаются с гласной буквы.
# print("\n#6\n")
# f = ["apple", "appricot", "pineapple", "banana", "grape", "orange"]
# def starts_from_vowel(f):
#   sum = 0
#   for i in f:
#     if i[0].lower() in "aeuioаоиеёэыуюя":
#       sum += 1
#   return sum
# print(f'There are "{starts_from_vowel(f)}" words starting from the vowel between "{len(f)}" words.')
# # 7.     Создайте массив, заполненный десятью нулями: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0].
# print("\n#7\n")
# n = 10 # int(input('Enter the quantity of zeros: '))
# def ten_zeros(n):
#     arr_ten_zeros = []
#     for i in range(0,n):
#         arr_ten_zeros.append(0)
#     return arr_ten_zeros
# print(f'Array from "{n}" zeros: "{ten_zeros(n)}"')
# # 8.     Создайте массив из 10 первых натуральных чисел: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
# print("\n#8\n")
# n = 10 # int(input('Enter the quantity of numbers: '))
# def first_ten_integers(n):
#     first_ten_integers = []
#     for i in range(0, n):
#         i += 1
#         first_ten_integers.append(i)
#     return first_ten_integers
# print(f'Array from "{n}" first integers: "{first_ten_integers(n)}"')
# # 9.     Создайте массив из 10 первых четных чисел: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18].
# print("\n#9\n")
# n = 10 # int(input('Enter the quantity of numbers: '))
# def first_ten_even_integers(n):
#     first_ten_even_integers = []
#     for i in range(-1, n * 2 - 1):
#       if i % 2 != 0:
#         i += 1
#         first_ten_even_integers.append(i)
#     return first_ten_even_integers
# print(f'Array from "{n}" first even integers: "{first_ten_even_integers(n)}"')
# # 10.   Создайте массив из 10 первых нечетных чисел: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19].
# print("\n#10\n")
# n = 10 # int(input('Enter the quantity of numbers: '))
# def first_ten_odd_integers(n):
#     first_ten_odd_integers = []
#     for i in range(-1, n * 2 - 1):
#       if i % 2 == 0:
#         i += 1
#         first_ten_odd_integers.append(i)
#     return first_ten_odd_integers
# print(f'Array from "{n}" first odd integers: "{first_ten_odd_integers(n)}"')
# # 11.   Создайте массив, содержащий десять чисел,
# # являющихся степенями числа 2: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512].
# print("\n#11\n")
# n = 10 # int(input('Enter the quantity of numbers: '))
# def first_ten_powers_of_two(n):
#     arr_first_ten_powers_of_two = []
#     for i in range(0, n):
#         k = 2 ** i
#         arr_first_ten_powers_of_two.append(k)
#     return arr_first_ten_powers_of_two
# print(f'First ten powers of number 2 are: "{first_ten_powers_of_two(n)}"')
# # 12.   Введите строку. Получите массив из слов строки, которые начинаются с гласной буквы.
# print("\n#12\n")
# words = str(input('Enter the string: '))
# def words_to_arr(words):
#   arr_vowels = []
#   for i in words.split():
#     if i[0].lower() in "aeuioаоиеёэыуюя":
#       arr_vowels.append(i)
#   return arr_vowels
# print(f'Array from words starting from the vewels: "{words_to_arr(words)}".')
# # 13.   Задан массив arr, хранящий значение температуры в градусах Цельсия.
# # arr = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35].
# # Получите массив, содержащий значения температуры в градусах Фаренгейта.
# print("\n#13\n")
# arr = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
# def cel_far(arr):
#   cel_far = []
#   for i, elem in enumerate(arr):
#     cel_far.append(int(elem *  9/5 + 32))
#   return cel_far
# print(cel_far(arr))
# # 14.   Заполните массив 10 числами Фибоначчи. Первые два числа этой последовательности равны 0 и 1.
# # А каждое следующее число, начиная с третьего, равно сумме двух предыдущих чисел: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# print("\n#14\n")
# n = 10 # int(input('Enter the quantity of numbers: '))
# def first_fibb_integers(n):
#     arr = [0, 1]
#     for i in range(1, n - 1):
#       k = arr[-1] + arr[-2]
#       arr.append(k)
#     return arr
# print(first_fibb_integers(n))

# #2 - Сумма углов n-угольника равна 180 * (n − 2).
# # Напишите функцию angles_of_polygon,
# # которая принимает аргумент n (число углов) и возвращает сумму углов n-угольника.
# n = int(input("Enter the number of angles: "))
# def angles_of_polygon(n):
#     res = 180 * (n - 2)
#     return res
# print(angles_of_polygon(n))

# #3 - Напишите функцию с именем miles_to_feet, которая принимает число miles (количество миль) в качестве аргумента и возвращает это расстояние в футах. 1 миля = 5280 футов.
# miles = int(input("Enter the number of miles: "))
# length_foot = 5280
# def miles_to_feet (miles):
#   return f'{miles} * {length_foot} = {miles * length_foot} miles.'
# print(miles_to_feet(miles))

# #4 - Напишите функцию, которая принимает два параметра weight и height.
# Функция вычисляет индекс массы тела bmi по формуле:
# bmi = weight / height ** 2 и возвращает описание результата:
# # ·       если bmi <= 18.5, возвратить "Underweight";
# # ·       если bmi <= 25.0, возвратить "Normal";
# # ·       если bmi <= 30.0, возвратить "Overweight";
# # ·       если bmi > 30 , возвратить"Obese".
#
# weight = int(input('Enter the weight in kg: '))
# height = int(input('Enter the height in cm: '))
# def func (weight,height):
#   bmi = height ** 2 / weight
#   if bmi <= 18.5:
#     return "Underweight"
#   if bmi <= 25.0:
#     return "Normal"
#   if bmi <= 30.0:
#     return "Overweight"
#   if bmi > 30:
#     return "Obese"
# print(func(weight,height))


# # 4. Напишите функцию, которая принимает два параметра weight и height. Ф
# # ункция вычисляет индекс массы тела bmi по формуле:
# # bmi = weight / height ** 2 и возвращает описание результата:
# # ·       если bmi <= 18.5, возвратить "Underweight";
# # ·       если bmi <= 25.0, возвратить "Normal";
# # ·       если bmi <= 30.0, возвратить "Overweight";
# # ·       если bmi > 30 , возвратить"Obese".
# print("\n#4\n")
# def weight_height():
#     weight = round(float(input('Enter the weight: ')), 2)
#     height = round(float(input('height: ')), 2)
#     bmi = (weight / height) ** 2
#     if bmi <= 18.5:
#       return f'Underweight'
#     elif bmi <= 25.0:
#       return f'Normal'
#     elif bmi <= 30.0:
#       return f'Overweight'
#     elif bmi > 30:
#       return f'Obese'
# print(weight_height())

# # 2.     Найти произведение нечетных элементов массива.
# print("\n#2\n")
# import array as arr
# b = arr.array('i', [18, 35, 45, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]) # Why repl thinks 1.8 is an odd?
# def odd_production(b):
#   production = 1
#   for i in range(len(b)):
#     if b[i] % 2 != 0:
#       production *= b[i]
#   return round(production, 2)
# print(f'Production of odd numbers in "{b}"\nis "{odd_production(b)}", quantity of numbers is "{len(b)}".')

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# def result(arr):
#   add = 1
#   for i in arr:
#     if i % 2 != 0:
#       add *= i
#   return add
# print(result(arr))

# import array as arr
# a = arr.array([4, 8, 20, 16])
# b = a / 4
# print(b)

# ##########
# import random
# from hw_2_modules import *
#
# arc = ArcherMain('Sniper')
# med = MedicMain('Aibolit')
# fighter = InfantrymanMain('Rambo')
#
# # ------------- Testing -------------------
# # print(arc.get_name())
# # print(arc.get_position())
# # print(arc.get_health())
# #
# # arc.health_down(20)
# # print(arc.get_health())
# # # arc.health_up()
# # # print(arc.get_health())
# #
# # arc.moved()
# # print(arc.get_position())
# #
# # arc.set_position(50)
# # print(arc.get_position())
# #
# # arc.moved()
# # print(arc.get_position())
# #
# # print(fighter.get_name())
# #
# # arc.health_down(fighter_damage)
# # print(arc.get_health())
# #
# # arc.health_up(med_heal)
# # arc.health_up(med_heal)
# # arc.health_down(fighter_damage)
# # arc.health_up(med_heal)
# # print(arc.get_health())
#
#
# # ----------- Variables -------------------------
# arc_name = arc.get_name()
# arc.set_position(50)
# arc_pos = arc.get_position()
# arc_damage = arc.get_attack()
# arc_health = arc.get_health()
# arc_dist = arc.get_attack_dist()
#
# fighter_name = fighter.get_name()
# fighter_pos = fighter.get_position()
# fighter_damage = fighter.get_attack()
# fighter_health = arc.get_health()
# fighter_dist = fighter.get_attack_dist()
#
# med_heal = med.get_heal()
#
# # ----------- Game Start -------------------------
# print(f'-----$$$$ Fight {arc_name} vs {fighter_name} $$$$-----')
# print('Arc health >', arc_health)
# print('Fighter health >', fighter_health)
# print('Archer position >', arc_pos)
# print('Fighter position >', fighter_pos)
#
# count = 0
# while arc_health > 0 or fighter_health > 0:
#     count += 1
#     if arc_pos - fighter_pos >= 1:
#         fighter.moved()
#         fighter_pos = fighter.get_position()
#         print(f'{count}. {fighter_name} moved to position {fighter_pos}')
#     if abs(arc_pos - fighter_pos) <= arc_dist:
#         fighter.health_down(arc_damage)
#         fighter_health = fighter.get_health()
#
#     if abs(arc_pos - fighter_pos) <= fighter_dist:
#         arc.health_down(fighter_damage)
#         arc_health = arc.get_health()
#         print(f'{count}. {arc_name} -->. {fighter_name} health: {fighter_health} >< {fighter_name} |/. {arc_name} health: {arc_health}')
#     # print(count, f'{fighter_name} |/. {arc_name} health: {arc_health}')
#


##########
# # 1 Sorting
# nums = [5,7,6,9,8,4,3,1,0]
#
# print(f'It was: {nums}')
#
# for i in range(len(nums)):
#     lowest = i # 1th element acepted as a lowest
#
#     for j in range(i+1, len(nums)):
#         if nums[j] < nums[lowest]:
#             lowest = j # the lowest element is found in the right slice
#
#         nums[i], nums[lowest] = nums[lowest], nums[i]
#
# print(f'Now: {nums}')

# # 2 Brute force = linear search
# names = ["Vlad", "Serge", "Vic", "Peter", "Luke", "Matthew", "Kayafa", "Saul"]
# print(names)
# search_for = str(input(f'Enter what to search: '))
#
# def linear_search(where, what):
#     for v in enumerate(where):
#         if v[1] == what:
#             return v[0]
#
#     return None
#
# print("Searched element", search_for, "found under index", linear_search(names, search_for))

# # 3 Binary search
# nums = [5,7,6,9,8,4,3,1,0]
# nums.sort() # sorting
# print(nums)
#
# search_for = int(input("Enter what to search: "))
#
# lowest = 0
# highest = len(nums) - 1
# index = None
#
# while(lowest+highest) and (index is None):
#     # repeat till found
#     mid = (lowest+highest) // 2 # middle
#
#     if nums[mid] == search_for:
#         # found on the middle
#         index = mid
#     else:
#         if search_for < nums[mid]:
#             # search in the left part of the list
#             highest = mid - 1
#         else:
#             # search in the right part of the list
#             lowest = mid + 1
#
# print("Searched element", search_for, "found under index", index)

# # 4 Evklide algorithm, searchind for the greatest common divider
# # Большее число делим на меньшее.
# # Если делится без остатка, то меньшее число и есть НОД (следует выйти из цикла).
# # Если есть остаток, то большее число заменяем на остаток от деления.
# # Переходим к пункту 1.
# # Пример:
# # Найти НОД для 30 и 18.
# # 30 / 18 = 1 (остаток 12)
# # 18 / 12 = 1 (остаток 6)
# # 12 / 6 = 2 (остаток 0)
# # Конец: НОД – это делитель 6.
# # НОД (30, 18) = 6
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
#
# def gcd(a, b):
#     while a != 0 and b != 0:
#         if a > b:
#             a = a % b
#         else:
#             b = b % a
#     return a + b
#
# print("Greatest common divider of", a, "and", b, "is: ",  gcd(a, b))

# import math
# print("Greatest common divider of", a, "and", b, "is:", math.gcd(a, b))

# 5 Reverse the string
# string = str(input("Enter the string: "))

# def reverse_string(s):
#     chars = list(s) # split string to charachters
#
#     for i in range(len(s) // 2):
#         # till the middle
#         temp = chars[i]
#         chars[i] = chars[len(s) - i -1]
#         chars[len(s) - i - 1] = temp
#
#     return  ''.join((chars))
#
# print(string)
# print(reverse_string(string))
#
# # Most quick and easy method in Python
# print(string[::-1])

# reversed_string = ''.join(reversed(string))
# print(reversed_string)

# a = 2
# b = 4
# print(a, b)
# a, b = b, a
# print(a, b)

# class MyClass:
#     variable = "blah"
#
#     def function(self):
#         print("This is a message inside the class.")
#
# myobjectx = MyClass()
# myobjecty = MyClass()
#
# myobjecty.variable = "yackity"
#
# # Then print out both values
# print(myobjectx.variable)
# print(myobjecty.variable)
#
# myobjectx.function()
#
# print(myobjectx.function())

# # define the Vehicle class
# class Vehicle:
#     name = ""
#     kind = "car"
#     color = ""
#     value = 100.00
#     def description(self):
#         desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
#         # desc_str = f"{self.name} is a {self.color} {self.kind} worth {self.value}"
#         return desc_str
# # your code goes here
# car1 = Vehicle()
# car1.name = "Fer"
# car1.color = "red"
# car1.kind = "convertible"
# car1.value = 60000.00
#
# car2 = Vehicle()
# car2.name = "Jump"
# car2.color = "blue"
# car2.kind = "van"
# car2.value = 10000.00
#
# # test code
# print(car1.description())
# print(car2.description())

# Write Python3 code here

# class car():
#
#     # init method or constructor
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color
#
#     def show(self):
#         print("Model is", self.model)
#         print("color is", self.color)
#
#     # both objects have different self which
#
#
# # contain their attributes
# audi = car("audi a4", "blue")
# ferrari = car("ferrari 488", "green")
#
# audi.show()  # same output as car.show(audi)
# ferrari.show()  # same output as car.show(ferrari)

# Behind the scene, in every instance method
# call, python sends the instances also with
# that method call like car.show(audi)

# # Перевернуть строку
# string = str(input("Ввести строку: "))
# # rev_string = string[::-1]
# rev_string  = ''.join(reversed(string))
# print(rev_string)

# # Binary gap
# n = int(input("Enter the integer: "))
# def solution(n):
#     # write your code in Python 3.6
#     n_bin = (bin(n))[2:]
#     str_n_bin = str(n_bin)
#     print(n_bin)
#     print(str_n_bin)
#     c = len(max(str_n_bin.strip('0').strip('1').split('1')))
#     print(c)
#
# print(solution(n))


# OOP in Python
# x = 'Hello'
# print(type(x))
#
# y = 44
# print(type(y))

# def some_solution(x):
#     return type(x)
# print(some_solution(int(input(f'Enter the string: '))))
# print(type(some_solution))

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print(name, age)
#
#     def myayu(self):
#         print(f'{self.name} of {self.age} years tells: Myayu')
#
#     def rrr_yu(self):
#         print(f'{self.name} of {self.age} years tells: Rrr_yu')
#
# a = Cat("Zuchka", 2)
# a.myayu()
# print(type(a))
# b = Cat("Laska", 3)
# b.rrr_yu()
# print(type(b))
#
# a1 = Cat("Murzick", 4)
# b1 = Cat("Banyka", 5)

# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade # 1 - 100
#
#     def get_grade(self):
#         return self.grade
#
# class Course:
#     def __init__(self, name, max_students):
#         self.name = name
#         self.max_students = max_students
#         self.students = []
#         self.is_active = False
#
#     def add_student(self, student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return True
#         return False
#
#     def get_average_grade(self):
#         value = 0
#         for student in self.students:
#             value += student.get_grade()
#
#         return value / len(self.students)
#
#
# s1 = Student("Tim", 19, 95)
# s2 = Student("Bill", 19, 75)
# s3 = Student("Jill", 19, 65)
#
# course = Course("Science", 2)
# course.add_student(s1)
# course.add_student(s2)
# print(course.students[0].name)
# print(course.get_average_grade())


# class Pet:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show(self):
#         print(f'I am {self.name} and I am {self.age} years old')
#
#     def speak(self):
#         print(f'I do not know what to say')
#
# class Cat(Pet):
#     def __init__(self, name, age, color):
#         super().__init__(name, age)
#         # self.name = name
#         # self.age = age
#         self.color = color
#
#     def speak(self):
#         print("Meow")
#
#     def show(self):
#         print(f'I am {self.name} and I am {self.age} years and I am {self.color}')
#
# class Dog(Pet):
#     # def __init__(self, name, age):
#         # self.name = name
#         # self.age = age
#
#     def speak(self):
#         print("Bark")
#
# class Fish(Pet):
#     pass
#
# p = Pet("Tim", 19)
# p.speak()
# # p.show()
# c = Cat("Bill", 34, "Brown")
# c.speak()
# c.show()
# d = Dog("Jill", 25)
# d.speak()
# f = Fish("Bubbles", 10)
# f.speak()

# class Person:
#     number_of_people = 0
#     GRAVITY = -9.8
#
#     def __init__(self, name):
#         self.name = name
#         # Person.number_of_people += 1
#         Person.add_person()
#
#     @classmethod
#     def number_of_people_(cls):
#         return cls.number_of_people
#
#     @classmethod
#     def add_person(cls):
#         cls.number_of_people += 1
#
# p1 = Person("Tim")
# # print(Person.number_of_people)
# p2 = Person("Jill")
# # print(Person.number_of_people)
# p3 = Person("Bill")
# # print(Person.number_of_people)
# print(Person.number_of_people_())
#
# # Person.number_of_people = 8
# # print(p2.number_of_people)
# # print(p1.number_of_people)


# class Math:
#
#     @staticmethod
#     def add5(x):
#         return x + 5
#
#     @staticmethod
#     def add10(x):
#         return x + 10
#
#     @staticmethod
#     def pr():
#         print("Run")
#
# print(Math.add5(5))
# print(Math.add10(5))
# # print(Math.pr())
# Math.pr()


# class User:
#     def log(self):
#         print(self)
#
# class Teacher(User):
#     def log(self):
#         print("I am a teacher!")
#
# class Customer(User):
#     # def log(self):
#     #     print("I am a customer!")
#     def __init__(self, print_out, name, member_type):
#         self.print_out = print_out
#         self.name = name
#         self.member_type = member_type
#
#     @property
#     def name(self):
#         # print("Getting name")
#         return self._name
#
#     @name.setter
#     def name(self, name):
#         # print("Setting name")
#         self._name = name
#
#     @name.deleter
#     def name(self):
#         # print("Deleting name")
#         del self._name
#
#     def update_membership(self, new_membership):
#         self.member_type = new_membership
#
#     def __str__(self):
#         return self.print_out + "; " + self.name + "; " + self.member_type + "; "
#
#     def print_all_customers(customers):
#         for customer in customers:
#             print(customer)
#
#     def __eq__(self, other):
#         if self.name == other.name and self.member_type == other.member_type:
#             return True
#         return False
#
#
#     __hash__ = None
#     __repr__ = __str__
#
#
#
# customers =[Customer("Customer created", "Caleb", "Gold"), Customer("Customer created", "Brad", "Bronze"), Teacher()]
# for customer in customers:
#     customer.log()
# # customers[0].update_membership("Irridium")
# # customers[1].update_membership("Platinum")
# # Customer.print_all_customers(customers)
# # del customers[0].name
#
# # print(f'{customers[0].print_out}, {customers[0].name}, {customers[0].member_type}\n')
# # print(f'{customers[1].print_out}, {customers[1].name}, {customers[1].member_type}\n')
#
# # print(f'{customers[0]}\n')
# # print(f'{customers[1]}\n')
#
# print(customers[0] == customers[1])
# # data = {customers[0]}
# # print(customers)
# # customers[2].log()


# permutations
# from itertools import permutations
# string_permutate = str(input("Enter the string: "))
# string_permutated = ["".join(p) for p in permutations(string_permutate)]
# print(string_permutated)
# print(len(string_permutated))

# from itertools import permutations
# c = [''.join(p) for p in permutations('dune')]
# print(c)

# string_permutated = str(input("Enter the string: "))
# def permutations(string, step = 0):
#     if step == len(string):
#         # we've gotten to the end, print the permutation
#         print("".join(string))
#     for i in range(step, len(string)):
#         # copy the string (store as array)
#         string_copy = [c for c in string]
#          # swap the current index with the step
#         string_copy[step], string_copy[i] =string_copy[i], string_copy[step]
#          # recurse on the portion of the string that has not been swapped yet
#         permutations(string_copy, step + 1)
# print(permutations(string_permutated))

# from itertools import permutations
# perms = [''.join(p) for p in permutations(str(input("Enter the string: ")))]
# print(perms, len(perms))

# def permute(data, i, length):
#     if i==length:
#         print(''.join(data))
#     else:
#         for j in range(i, length):
#             #swap
#             data[i], data[j] = data[j], data[i]
#             permute(data, i+1, length)
#             data[i], data[j] = data[j], data[i]
#
# string = str(input("Enter the string: "))
# n = len(string)
# data = list(string)
# permute(data, 0, n)

# def permutations(string):
#     if len(string) == 1:
#         return string
#
#     recursive_perms = []
#     for c in string:
#         for perm in permutations(string.replace(c, '', 1)):
#             recursive_perms.append(c+perm)
#
#     return set(recursive_perms)
#
# print(permutations(str(input("Enter the string: "))))

# fact = int(input("Enter fact: "))
# total = int(input("Enter total: "))
# conversion = round(fact / total * 100, 2)
# print(conversion)
# print(type(fact), type(conversion))

# bookCost = 24.95
# numBooks = 60.0
#
# def cost(numBooks):
#     bulkBookCost = ((bookCost * 0.60) * numBooks)
#     shippingCost = (3.0 + (0.75 * (numBooks - 1)))
#     totalCost = bulkBookCost + shippingCost
#     print('The total cost is: $', totalCost)
#
# cost(numBooks)

# SECONDS = 1
# MINUTES = 60 * SECONDS
# HOURS = 60 * MINUTES
#
# # All these results are in seconds
#
# time_left_house = 6 * HOURS + 52 * MINUTES
#
# miles_run_easy_pace = 2 * (8 * MINUTES + 15 * SECONDS)
#
# miles_run_fast_pace = 3 * (7 * MINUTES + 12 * SECONDS)
#
# total_time_run = miles_run_easy_pace + miles_run_fast_pace + time_left_house
#
# # So we now have a big number of seconds to split into hours/minutes/seconds
#
# hours = total_time_run // HOURS
#
# # the left over part is minutes and seconds (still in seconds)
#
# part_hour = total_time_run % HOURS
# minutes = part_hour // MINUTES
# seconds = part_hour % MINUTES
#
# print("Total time run: {}, Hours: {}, Minutes: {}, Seconds: {}".format(
#     total_time_run, hours, minutes, seconds))


# name = 'Bob'
# print("Hello, {}".format(name))


# def print_lyrics():
#     print("\nI'm a lumberkack, and I'm okay")
#     return ("I sleep all day night and I work all day\n")
#
# print(print_lyrics())
# print(type(print_lyrics))
#
# def repeat_lyrics():
#     print(print_lyrics())
#     print(type(print_lyrics))
#
# print(repeat_lyrics())

# import math
# a = math.pi
# def print_twice(a):
#     print(f'1th: {round(a, 4)}')
#     print(f'2d: {round(a, 4)}')
#
# print(print_twice(math.pi))

# def print_twice(argum):
#     print(argum)
#     print(argum)
#
# def cat_twice(part1, part2):
#     cat = part1 + ' ' + part2
#     return print_twice(cat)
#
# print(cat_twice(str(input("Enter part1: ")), str(input("Enter part2: "))))


# # Download and install Python not older than 3d version https://www.python.org/downloads/
# # Download and install PyCharm https://www.jetbrains.com/pycharm/download/#section=windows
# # Create hw_1_installation_dt_08_march_2021.py
# # Write and play with the code below
# a = "Hello, world!!!"
# print(a)
# print('The value of a is:' + ' ' + a)
# print(f'The value of a is: {a}')
# print("The value of a is: {}".format(a))
# # Understand how to use comments by "#" for single strings and at the start/top """ and """ at the end/bottom
# """
# multy strings are for those who will work with the code after you making it understandable
# """
# # Write and play with the code below
# # Undertand what are types of data in Python: str, int, float
# # Undertand what is the formatted string (f'Some text: {placeholder}')
# # Understand what are the reserved words, variables
# a = 2
# b = 3
# summ = a + b
# diff = a - b
# mult = a * b
# divis = round(a / b, 2)
# power = a ** b
# print(f'\na = {a}, b = {b};\nsumm: {summ};\ndifference: {diff};\nmultiplication: {mult};\ndivision: {divis};\npower: {power}')
# print(f'\ntype a: {type(a)};\ntype b: {type(b)};\ntype summ: {type(summ)};\ntype multiplication: {type(mult)};\ntype difference: {type(diff)};'
#       f'\ntype division: {type(divis)};\ntype power: {type(power)}')


# a = """
# ____88888888___________________________
# ___8888888888__________________________
# __888888888888_________________________
# __8888111188888________________________
# _888881111188888___11__________________
# _8888811111188888_11___________________
# _8888811111188888_11___________________
# _8888811111118888_11___________________
# _8888881111118888_11___11__8888888_____
# _8888881111118888__1__11__88888888888__
# _8888888111111888____11__8888888888888_
# __888888111111888_111___88888888888888_
# __8888888111118881111__888881111118888_
# ___888888811188881111_8888811111111888_
# ____8888888188881111188888111111118888_
# _____88888888888111118888111111118888__
# ______888888888111118888811111188888___
# ______8888888881111188888888888888_____
# _____888888888811111888888888888_______
# ____88888888888111118888888888_________
# ___88881111888811111888888888___________
# __8888111111888111118888888888__________
# _888881111118881111188811118888_________
# _8888881111888811111881111118888________
# _8888888118888811111888111188888________
# __888888888888_1111888881188888_________
# ___8888888888___111_8888888888__________
# ____88888888_____1___88888888___________
# _____888888___________888888____________
# _______________________8888_____________
# """
#
# print(a)

# import math
# a = math.sqrt(5)
# print(round(a, 2))

# # Exercise 3.3. Python provides a built-in function called len that returns the length of a string, so
# # the value of len('allen') is 5.
# # Write a function named right_justify that takes a string named s as a parameter and prints the
# # string with enough leading spaces so that the last letter of the string is in column 70 of the display.
# # >>> right_justify('allen')
# def right_justify(s):
#     print(" " * (70 - len(s)) + s)
# right_justify('allen')
#
#
# def right_justify(s):
#     print("%70s" % s)
# right_justify('allen')

# # Exercise 3.4. A function object is a value you can assign to a variable or pass as an argument. For
# # example, do_twice is a function that takes a function object as an argument and calls it twice:
# # 1. Type this example into a script and test it.
# # 2. Modify do_twice so that it takes two arguments, a function object and a value, and calls the
# # function twice, passing the value as an argument.
# # 3. Write a more general version of print_spam, called print_twice, that takes a string as a
# # parameter and prints it twice.
# # 4. Use the modified version of do_twice to call print_twice twice, passing 'spam' as an
# # argument.
# # 5. Define a new function called do_four that takes a function object and a value and calls the
# # function four times, passing the value as a parameter. There should be only two statements in
# # the body of this function, not four.
# a = str(input('Enter the 1th string: '))
# b = str(input('Enter the 2d string: '))
# def do_twice(f, a, b):
#     f()
#     f()
#
# def do_four(f, a, b):
#     do_twice(f, a, b)
#     do_twice(f, a, b)
#
# def print_spam():
#     print(f'{a}, {b}')
#
# do_twice(print_spam, a, b)
# do_four(print_spam, a, b)

# Exercise 3.5. This exercise can be done using only the statements and other features we have learned
# so far.
# 1. Write a function that draws a grid like the following:
# 30 Chapter 3. Functions
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# Hint: to print more than one value on a line, you can print a comma-separated sequence:
# print '+', '-'
# If the sequence ends with a comma, Python leaves the line unfinished, so the value printed
# next appears on the same line.
# print '+',
# print '-'
# The output of these statements is '+ -'.
# A print statement all by itself ends the current line and goes to the next line.

# a = '+' + ' - ' * 4 + '+' + ' - ' * 4 + '+'
# b = '|' + '   ' * 4 + '|' + '   ' * 4 + '|'
# print(f'{a}\n{b}\n{b}\n{b}\n{b}\n{a}\n{b}\n{b}\n{b}\n{b}\n{a}')
#
# a = '+' + ' - ' * 4 + '+' + ' - ' * 4 + '+' + ' - ' * 4 + '+' + ' - ' * 4 + '+'
# b = '|' + '   ' * 4 + '|' + '   ' * 4 + '|' + '   ' * 4 + '|' + '   ' * 4 + '|'
# print(f'{a}\n{b}\n{b}\n{b}\n{b}\n{a}\n{b}\n{b}\n{b}\n{b}\n{a}\n{b}\n{b}\n{b}\n{b}\n{a}\n{b}\n{b}\n{b}\n{b}\n{a}\n')

# a, b = '+'+' - '*4+'+'+' - '*4+'+', '|'+'   '*4 + '|'+'   '*4+'|'
# print(f'{a}\n{b}\n{b}\n{b}\n{b}\n{a}\n{b}\n{b}\n{b}\n{b}\n{a}')

# weight = int(input("Enter your weight in KG: "))
# height = float(input("Enter your height in METERS: "))
# BMI = weight / (height ** 2)
# if BMI < 18.5:
#     print("Underweight")
# if BMI >= 18.5 and BMI < 25:
#     print("Normal")
# if BMI >= 25 and BMI < 30:
#     print("Overweight")
# if BMI >= 30:
#     print("Obesity")

# weight = int(input("Enter your weight in KG: "))
# height = float(input("Enter your height in METERS: "))
# bmi = weight / (height ** 2)
# if bmi < 18.5:
#     print("Underweight")
# if bmi >= 18.5 and BMI < 25:
#     print("Normal")
# if bmi >= 25 and BMI < 30:
#     print("Overweight")
# if bmi >= 30:
#     print("Obesity")

# weight = int(input("Enter your weight in KG: "))
# height = float(input("Enter your height in METERS: "))
# bmi = round(weight / (height ** 2), 1)
# if bmi < 18.5:
#     print(f"BMI: {bmi}. You are underweighted")
# elif 18.5 <= bmi < 25:
#     print(f"BMI: {bmi}. You are normal")
# elif 25 <= bmi < 30:
#     print(f"BMI: {bmi}. You are overweighted")
# elif 30 <= bmi:
#     print(f"BMI: {bmi}. You have obesity")

# a = 2 # lenght between holes horizontally
# b = 1 # lenght between holes vertically
# l = 3 # free end of lace
# n = 4 # quantity of the holes in the one row
# two_free_ends = 2 * l
# length_between_holes_horizont = a * 2 * n
# lenghts_summed_between_holes_vert = b * n
# lenght = two_free_ends + length_between_holes_horizont + lenghts_summed_between_holes_vert
# print(lenght)

# if 5 > 2:
#     print("Five is greater than two!")

# list2 =[1, 2, 3, 4, -2, 10, 0, 0, 10]
# print(list2)
# print(list2.count(2))
# print(list2[0], list2[-1], list2[-2], list2[:-1], list2[len(list2)-1])
# a = list2.pop(list2[0])
# print(list2)
# print(''.join(reversed(str(list2))), list2[::-1])
# print(list2.sort())

# # List [] - brackets, mutable
# print("List []")
# list_1 = [1, 2, 3, 4, 'String', [5, 6, 7, 8], 'Alfa']
# print(f'1. Type of list_1: "{type(list_1)}"')
# print(f'2. List list_1: "{list_1}, has "{len(list_1)}" members')
# print(f'3. List list_1 can be reversed via slicing: {list_1[::-1]}')
# list_1.append('Append')
# print(f'4. To list can be added additional member: "{list_1}"')
# print(f'5. 1th element of list a: "{list_1[0]}" and last element of list a: "{list_1[-1]}"')
# for i in range(0, len(list_1)):
#     print(f'#{i+1}: Element: "{list_1[i]}"')
#     if 'a' in str(list_1[i]).lower():
#         print(f'"a" in "{str(list_1[i])}"')
#     else:
#         print(f'"a" not in "{str(list_1[i])}"')
# print('\n')
#
# # Tuple/кортеж () - parentheses, immutable, used for locators keeping in Automation like: CONTACT_TEXT = (By.XPATH, "(//div[@class='review-block__content'])[1]")
# print("Tuple/кортеж ()")
# tuple_1 = (1, 2, 3, 4, "Tuple", [1, 2, 3], "Ulyana")
# print(f'1. Type of tuple_1: "{type(tuple_1)}"')
# # tuple_1.append('Append')
# # print(f'2. Tuple is immutable: "{tuple_1}"') # AttributeError: 'tuple' object has no attribute 'append'
# print(f'2. Tuple tuple_1 has length: "{len(tuple_1)}"')
# print(f'3. Tuple tuple_1 can be reversed via slicing: "{tuple_1[::-1]}"')
# for i in range(0, len(tuple_1)):
#     print(f'#{i+1}: Element: "{tuple_1[i]}"')
#     if 'u' in str(tuple_1[i]).lower():
#         print(f'"u" in "{str(tuple_1[i])}"')
#     else:
#         print(f'"u" not in "{str(tuple_1[i])}"')
# print('\n')
#
# # Dictionary {} - braces
# print("Dictionary {}")
# dict_1 = {
#     "key_0": "value_0",
#     "key_1":"value_1",
#     "key_2":"value_2",
#     "key_3":"value_3",
#     "key_4":"value_4",
# }
#
# print(f'1. Length of dictionary c: "{len(dict_1)}"')
# print(f'2. Value of 1th key: "{dict_1["key_0"]:}", value of last key: "{dict_1["key_4"]:}"')
# for key in dict_1:
#     print(f'#{key}: Element: "{dict_1[key]}"')
#     if 'u' in str(dict_1[key]):
#         print(f'"u" in "{dict_1[key]}"')
#     else:
#         print(f'"u" not in "{dict_1[key]}"')
# print('\n')
#
# # Set {} is used to store multiple items in a single variable
# print("Set {}")
# set_1 = {"Uno", "Des", "Tres", "Argentum", "Para"}
# print(f'1. Length of set_1 "{set_1}": "{len(set_1)}"')
# print(f'2. Type of set_1: "{type(set_1)}"')
# set_1_list = list(set_1)
# print(f'3. Length of set_1_list "{set_1_list}": "{len(set_1_list)}"')
# print(f'4. Type of set_1_list: "{type(set_1_list)}"')
# print('\n')

# nums_1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# some_nums = nums_1[2:7] # 2 is taken, but 7 is not. start:stop:step. nums[:5] is equivalent to nums[0:5].
# print(nums_1)
# print(some_nums)

# nums_2 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# print(nums_2)
# # Negative indexes allow us to easily take n-last elements of a list
# print(nums_2[-3:])
# # We can freely mix negative and positive indexes in start and stop positions
# print(nums_2[1:-1])
# print(nums_2[-3:8])
# print(nums_2[-5:-1])
# # Taking all but n last elements of a list
# print(nums_2[:-2])
# # Taking every nth-element of a list
# print(nums_2[::2])
# # By providing start we can skip some elements
# print(nums_2[1::2])
# # And if we don’t want to include some elements at the end, we can also add the stop parameter
# print(nums_2[1:-3:2])
# # We can use a negative step to obtain a reversed list
# print(nums_2[::-1])
# # if you want to have a reversed list which starts from 80
# print(nums_2[-2::-1])
# # We can use stop value to stop taking before some element. E.g., let’s not include 20 and 10 values
# print(nums_2[-2:1:-1])
# # It’s a bit baffling that with a negative step, stop index is located before start. Negative step turns everything upside down.
# # Of course, we can use an arbitrary negative step
# print(nums_2[-2:1:-3])


# Sort dictionary by values
# and get keys only
# employees = {
# "John" : 30 ,
# "Jane" : 29 ,
# "Jake" : 25 ,
# "April" :28 ,
# "Joe" : 27
# }

# def sort_dict(employees):
#     return {k: v for k, v in sorted(employees.items(), key=lambda item: item[1])}
# print(sort_dict(employees))

# def sort_dict(employees):
#     sorted_dict = {}
#     sorted_keys = sorted(employees, key = employees.get)
#     for i in sorted_keys:
#         sorted_dict[i] = employees[i]
#     return sorted_dict
# print(sort_dict(employees))
#
# def sort_dict(employees):
#     sorted_employees = dict(sorted((value, key) for (key, value) in employees.items()))
#     return sorted_employees
# print(sort_dict(employees))
#
# def getList(employees):
#     return employees.keys()
# print(getList(employees))

# # lambda function
# # A square lambda function
# square = lambda n : n*n
# num = square(5)
# print(num)
#
# # A substraction lambds function with multiple arguments
# sub = lambda x, y : x - y
# print(sub(5, 3))
#
# # Map with lambda
# myList = [10, 25, 17, 9, 30, -5]
# # Double the value of each element
# myList2 = map(lambda n : n*2, myList)
# print( myList2)
#
# # Filter with lambda
# myList = [10, 25, 17, 9, 30, -5]
# # Filters the elements which are not multiples of 5
# myList2 = filter(lambda n : n%5 == 0, myList)
# print(myList2)

# addition = lambda a, b : a + b
# print(addition(3, 4))
#
# mult = lambda a, b : a * b
# print(mult(3, 4))
#
# substr = lambda a, b : a - b
# print(substr(8, 4))
#
# divis = lambda a, b : a / b
# print(round(divis(9, 3), 2))
#
# power = lambda a, b : a ** b
# print(power(2, 2))
#
# square_root = lambda a: a ** 0.5
# print(square_root(81))

# # Sort dictionary
# dictionary = {
#     "Debil":45,
#     "Idiot":43,
#     "Microcefal":54,
#     "Degenerat":32,
#     "Gandon":31
# }
#
# def sort_dict(dictionary):
#     sort_dict = {}
#     sorted_keys = sorted(dictionary, key = dictionary.get)
#     for i in sorted_keys:
#         sort_dict[i] = dictionary[i]
#     return f'Sorted dictionary: {sort_dict}\n'
# print(sort_dict(dictionary))
#
# def getlist(dictionary):
#     return f'Sorted dictionary keys: {sorted(dictionary.keys())}\n'
# print(getlist(dictionary))
#
# def sort_dict(dictionary):
#     sort_dict = {}
#     sorted_keys = sorted(dictionary, key = dictionary.get)
#     for i in sorted_keys:
#         sort_dict[i] = dictionary[i]
#     return f'Sorted dictionary: {sort_dict}\n'
# print(sort_dict(dictionary))


# # Input: 2 arrays. Print any that apear in both.
# a1 = ['c', 'a', 'b', 'c']
# a2 = ['b', 'c', 'd']
# # print(sorted(a1), type(a1), '\n')
# # print(sorted(a2), type(a2), '\n')
#
# def common_member(a1, a2):
#     a1_set = set(a1)
#     a2_set = set(a2)
#
#     if a1_set & a2_set:
#         return (f'Common elements are: {a1_set & a2_set}\n')
#     else:
#         return ('No common elements', '\n')
#
# print(common_member(a1, a2))

# # Given a list of strings and a specific strung, find out many times
# # the string appears in the list
# i = ['abc', 'def', 'abc', 'ghi', 'abc']
# s = 'abc'
# # output 2
# def hmt_str_lst(i, s):
#     count = 0
#     for x in i:
#         if s == x:
#             count += 1
#     return f'String "{s}" is "{count}" times in the "{i}"'
# print(hmt_str_lst(i, s))

# Task
# Given an integer, n, perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of  6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

# n = int(input("Enter the integer: "))
# def a_math(n):
#     if n % 2 == 1:
#         return f'Weird'
#     elif n % 2 == 0 and 2 <= n <= 5:
#         return f'Not Weird'
#     elif n % 2 == 0 and 6 <= n <= 20:
#         return f'Weird'
#     else:
#         return f'Not Weird'
#
# print(a_math(n))

# An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

# In the Gregorian calendar, three conditions are used to identify leap years:

# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.
# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.

# year = int(input("Enter the year: "))
#
#
# def is_leap(year):
#     leap = False
#
#     # Write your logic here
#     if year % 400 == 0:
#         leap = True
#     elif year % 100 == 0:
#         leap = False
#     elif year % 4 == 0:
#         leap = True
#
#     return f'Is year "{year}" leap? "{leap}"\n'
#
#
# print(is_leap(year))

# dictionary = {
#     'One':'one',
#     'Two':'two',
#     'Three':'three'
# }
#
# print(type(dictionary), dictionary)
#
# print(dictionary.items())
#
# print(dictionary.keys())
#
# print(dictionary.values())

# test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
# print(set(test))
# print(max(set(test), key = test.count))
# print(min(set(test), key = test.count))

# # # Skillbox lesson https://www.youtube.com/watch?v=ygOiHzZigwI&t=1149s
# # with open("some-file-name.txt") as my_file:
# #     for line in my_file:
# #         print(line)
# # pip install simple_draw
# import simple_draw as sd
# sd.set_screen_size(600, 400)
# point = sd.get_point(300, 300)
# # sd.circle(point, radius=200,width=5)
# # sd.pause()
#
# # arm_length = 200
# def draw_flake(point, arm_length=30):
#     delta_angle = sd.random_number(30, 90)
#     dactor_a = sd.random_number(30, 90) / 100
#     for angle in range(0, 360, 60):
#        arm = sd.get_vector(point, angle=angle, length=arm_length)
#        arm.draw(color=sd.COLOR_WHITE)
#        arm2 = sd.get_vector(point, angle=angle, length=arm_length * .6)
#        sub_arm1 = sd.get_vector(arm2.end_point, angle=angle + delta_angle, length=arm_length * dactor_a)
#        sub_arm1.draw(color=sd.COLOR_WHITE)
#        sub_arm2 = sd.get_vector(arm2.end_point, angle=angle - delta_angle, length=arm_length * dactor_a)
#        sub_arm2.draw(color=sd.COLOR_WHITE)
#
# for _ in range(30):
#     point = sd.random_point()
#     length = sd.random_number(10, 50)
#     draw_flake(point=point)
#
# sd.pause()


# # If we list all the natural numbers below 10 that are multiples of 3 or 5,
# # we get 3, 5, 6 and 9. The sum of these multiples is 23.
# # Find the sum of all the multiples of 3 or 5 below 1000.
# def findSum():
#     a = int(input('Integer: '))
#     sum = 0
#     for i in range(a):
#         if (i % 3 ==0) or (i % 5 == 0):
#             sum += i
#     return sum
#
# print(findSum())

# Each new term in the Fibonacci sequence is generated by adding
# the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values
# do not exceed four million, find the sum of the even-valued terms.
# def fib(number):
#     series = [1,1]
#     lastnum = (series[len(series)-1] + series[len(series)-2])
#     _sum = 0
#     while lastnum < number:
#         if lastnum % 2 == 0:
#             _sum += lastnum
#         series.append(lastnum)
#         lastnum = (series[len(series)-1] + series[len(series)-2])
#     return series,_sum
#
# print(fib(4000000))
# number = int(input('Integer: '))
# def fibEven(number):
#     f1 = f2 = 1
#     total = 0
#     while f1 <= number:
#         if f1 % 2 == 0:
#             total += f1
#         f1, f2 = f2, f1 + f2
#     return total
#
# print(fibEven(number))


# # This is my shopping list
# shoplist = ['apple', 'mango', 'carrot', 'banana']
# print(f'I have "{len(shoplist)}" items to purchase.')
# print('These items are:',)
# for item in shoplist:
#     print(item, end = '; ')
# print(f'\nI also have to buy rice.')
# shoplist.append('rice')
# print(f'My shopping list is now "{shoplist}"')
# print(f'I will sort my list now')
# shoplist.sort()
# print(f'Sorted shopping list is "{shoplist}"')
# print(f'The first item I will buy is "{shoplist[0]}"')
# olditem = shoplist[0]
# del shoplist[0]
# print(f'I bought the "{olditem}"')
# print(f'My shopping list is now "{shoplist}"')

# # to indicate start and end of tuple
# # even though parentheses are optional.
# # Explicit is better than implicit.
# zoo = ('python', 'elephant', 'penguin')
# print(f'Number of animals in the zoo is  "{len(zoo)}"')
# new_zoo = ('monkey', 'camel', zoo)
# print(f'Number of cages in the new zoo is "{len(new_zoo)}"')
# print(f'All animals in new zoo are "{new_zoo}"')
# print(f'Animals brought from old zoo are "{new_zoo[2]}"')
# print(f'Last animal brought from old zoo is "{new_zoo[2][2]}"')
# print(f'Number of animals in the new zoo is "{len(new_zoo)-1+len(new_zoo[2])}"')

# # 'ab' is short for 'a'ddress'b'ook
# ab = {
# 'Swaroop' : 'swaroop@swaroopch.com',
# 'Larry' : 'larry@wall.org',
# 'Matsumoto' : 'matz@ruby-lang.org',
# 'Spammer' : 'spammer@hotmail.com'
# }
# print(f'Swaroop address is {ab["Swaroop"]}')
# # Deleting a key-value pair
# del ab['Spammer']
# print(f'\nThere are "{len(ab)}" contacts in the address-book\n')
# for name, address in ab.items():
#     print(f'Contact "{name}" at "{address}"')
# # Adding a key-value pair
# ab['Guido'] = 'guido@python.org'
# if 'Guido' in ab:
#     print(f"\nGuido's address is {ab['Guido']}")

# # aplle more expensive than pinapple for $1, together their price is $1,1
# # find price of aplle and pinapple
#
# total_price = round(float(input("Enter the total price in $: ")), 2)
# prs_dfrnc = round(float(input(('Enter for how much apple is more expensive than pinapple in $: '))), 2)
# pinapple = round(((total_price - prs_dfrnc) / 2), 2)
# apple = total_price - pinapple
# print(f'Pinapple price: ${pinapple},\n apple price: ${apple},\n total price: ${total_price}')

# Write a function to check whether two given strings are anagram of each other or not.
# An anagram of a string is another string that contains the same characters, only the order of characters can be different.
# For example, “abcd” and “dabc” are an anagram of each other

# sm_str_1 = str(input('Enter the string 1: '))
# sm_str_2 = str(input('Enter the string 2: '))

# def is_angrm(sm_str_1, sm_str_2):
#     n = len(sm_str_1)
#     m = len(sm_str_2)
#     if n != m:
#         return 0
#
#     sm_str_1 = sorted(sm_str_1)
#     sm_str_2 = sorted(sm_str_2)
#
#     for i in range(0, n):
#         if sm_str_1[i] != sm_str_2[i]:
#             return 0
#
#     return 1
#
# if is_angrm(sm_str_1, sm_str_2):
#     print('Anagram')
# else:
#     print
#     ('Not anagram')

# x = 10
# if x > 5:
#     raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

# import sys
# assert ('linux' in sys.platform), "This code runs on Linux only."

# print('###')
# import sys
# def linux_interaction():
#     assert ('linux' in sys.platform), "Function can only run on Linux systems."
#     print('Doing something.')
#
# try:
#     linux_interaction()
# except AssertionError as error:
#     print(error)
#     print('The linux_interaction() function was not executed')
# else:
#     print('Executing the else clause.')
#
# print('###')
# try:
#     with open('C:\Python\\file.log') as file:
#         read_data = file.read()
#         print(read_data)
# except FileNotFoundError as fnf_error:
#     print(fnf_error)
# except AssertionError as error:
#     print(error)
#     print('Linux linux_interaction() function was not executed')
# finally:
#     print('Cleaning up, irrespective of any exceptions.')

# # Anagram
# str_1 = str(input(('Enter 1th: ')))
# str_2 = str(input(('Enter 2d: ')))
#
# def isAnagram(str_1, str_2):
#     str1_list = list(str_1)
#     str1_list.sort()
#     str2_list = list(str_2)
#     str2_list.sort()
#     if str1_list == str2_list:
#        return 'Anagram'
#     else:
#        return 'Not anagram'
# print(isAnagram(str_1, str_2))

# # slices
# list_1 = [100, -1, 1, 250, 10, 5] # 100, 250, 10, print number > 4
# print(list_1[0], list_1[3], list_1[3])
# def mult_lst(list_1):
#    k = 4
#    for i in list_1:
#       if i >= k:
#          print(i, end = '; ')
# mult_lst(list_1)

# #
# print( False == False in [False])
# #
# n1='214'
# n_list=list(n1)
# n_list.reverse()
# n2="".join(n_list)
# print(n2)
# #
# n='3456'
# a=int(n[0])
# b=int(n[1])
# c=int(n[2])
# print(a+b+c)
# #
# a=float()
# for i in range(len(str(a))):
#    try:
#       print(str(a)[i], end = '')
#       if str(a)[i] == '.':
#          print(0, end = '')
#    except Exception:
#       continue
# #
# str_1 = str(input('Enter the str_1: '))
# print(str_1)
# str_2 = str_1.replace('a', 'b')
# print(str_2)
#
# find max in from list
# lst = [1, 2, 3, 4, 5, 6, 88]
# def lst_mx(lst):
#     max = lst[0]
#     for i in lst:
#         if i > max:
#             max = i
#     return max
# print(f'Max: {lst_mx(lst)}')

# find 2 max in from list
# lst = [1, 2, 3, 4, 5, 6, 88]
# def lst_mx(lst):
#     if lst[0] > lst[1]:
#         max = lst[0]
#         s_max = lst[1]
#     else:
#         max = lst[1]
#         s_max = lst[0]
#     for i in lst:
#         if i > max:
#             s_max = max
#             max = i
#         else:
#             s_max = i
#     return max, s_max
# print(f'Max: {lst_mx(lst)}')

# post & get
# get does not have a body;
# if HTTPS and get, data would be in URL and can not be secured-RED FLAG;
# token/s in client side (RSA-coding technic) key=private(расшифровать) and key=public(зашифровать), посылаются только паблик кийс, прайвет на машинах;
# cross browserness. decide based on the popularity of browser among our clients
# css as a language is part of the language of browser-that is why it is quicker than xpath
# # absence of locator. on every test verifying absence-there should be positive.
# # where(real fields) in sql before having(counted dynamically fields)
# # git reset(hard/soft) "commit"-откатить закоммиченные файлы

# strParam = str('Zalupa')
# def FirstReverse(strParam):
#     rev_strParam = strParam[::-1]
#     return rev_strParam
#
# print(FirstReverse(strParam))
##
# lst=[100,1,2,3,4,5,6,7,8,88,101]
# def max_i(lst):
#     max=lst[0]
#     for i in lst:
#         if i > max:
#             max = i
#     return max
# print(max_i(lst))
# #
# def s_max_i(lst):
#     if lst[0] > lst[1]:
#         max = lst[0]
#         s_max = lst[1]
#     else:
#         max = lst[1]
#         s_max = lst[0]
#     for i in lst:
#         if i > max:
#             s_max = max
#             max = i
#         else:
#             s_max=i
#     return max, s_max
# print(s_max_i(lst), type(s_max_i(lst)))
# #
# str_1 = str(input('Enter the str_1: '))
# def rev_str_1(str_1):
#     rev_str_1 = str_1[::-1]
#     return rev_str_1
# print(rev_str_1(str_1))
# #
# str_1 = str(input('Enter the str_1: '))
# str_2 = str(input('Enter the str_2: '))
# def is_str_eq(str_1, str_2):
#     list_str_1 = list(str_1)
#     list_str_1.sort()
#     list_str_2 = list(str_2)
#     list_str_2.sort()
#     if list_str_1 == list_str_2:
#         return 'Str_1 = Str_2'
#     else:
#         return 'Str_1 != Str_2'
# print(is_str_eq(str_1, str_2))
#
# # SQL task from geturgently.com dt 23 June 2021
# /* write your SQL query below */
#
# /*1SELECT * FROM maintable_CN1FJ*/
#
# SELECT
# ReportsTo,
# COUNT(ReportsTo) AS 'Members',
# ROUND(AVG(Age)) AS 'Average Age'
# FROM maintable_CN1FJ
# WHERE ReportsTo IS NOT NULL
# GROUP BY ReportsTo
# ORDER BY ReportsTo ASC
#
# SELECT
# ReportsTo,
# COUNT(ReportsTo) AS 'Members',
# CEIL(AVG(Age)) AS 'Average Age'
# FROM maintable_CN1FJ
# WHERE ReportsTo IS NOT NULL
# GROUP BY ReportsTo
# ORDER BY ReportsTo


# LindenLab code task dt 23 June 2021
# Given two arrays containing numbers,
# return true if the sums of the numbers in each array are equal to one another.
# For example:
# arrays_are_equal([1,2,3], [6]) # returns true
# arrays_are_equal([1], [0]) # returns false

# lst_1 = [1, 2, 3]
# lst_2 = [6]
# def if_lsts_eql(lst_1, lst_2):
#     lst_1_cntr = 0
#     for i in lst_1:
#         lst_1_cntr += i
#     lst_2_cntr = 0
#     for i in lst_2:
#         lst_2_cntr += i
#     if lst_1_cntr == lst_2_cntr:
#         return 'Lists are equal'
#     else:
#         return 'Lists are not equal'
# print(if_lsts_eql(lst_1, lst_2))
# def arrays_are_equal(lst_1, lst_2): return sum(lst_1) == sum(lst_2)
# print(arrays_are_equal(lst_1, lst_2))
# dict_1={
#     'id':1,
#     'name':'John',
#     'id':1,
#     'name':'John',
#     'id':2,
#     'name':'Johnna',
# }
# set_dict_1 = set(dict_1)
# print(f'{dict_1}, {type(dict_1)};\n{set_dict_1}, {type(set_dict_1)}')
#
# a = 'Marina'
# b = 'Dorka'
# print(f'{a} {b}')
# print(type(a), type(b))
#
# c = 2
# d = 5
# sum = c + d
# quotent = c / d
# diff = c - d
# print(sum, quotent, diff)
# print(type(c), type(d), type(sum), type(quotent), type(diff))
#
# lst_1 = [1, 2, 3, 4]
# print(lst_1)
# for i in lst_1:
#     print(i, end = '; ')
#     print(type(lst_1))
#
# lst_2 = ['one','two', 'three', 'four']
# print(lst_1)
# for i in lst_2:
#     print(i, end = '; ')
#     print(type(lst_2))
#
# xx=50
# def var_test():
#     xx=100
#     return xx
# print(var_test())
#
# def var_test():
#     xx=99
#     return xx
# var_test()
# print(xx)
#
# var_test="Jhons"*3*2
# print(var_test)
#
# xx=15
# if True:
#     xx=25
# print(xx)
#
# xx=25
# if False:
#     xx=75
# def var_test():
#     if True:
#         xx=35
# print(var_test())
#
# var1=15
# var2=25
# var3="30"
# print(var1+var2+var3)
#
# a=75
# def var_test():
#     return a
# print(var_test())
#
# x=15
# x="Python"
# print(x)
#
# xx=15
# def var_test():
#     xx=25
# var_test()
# print(xx)
#
# def var_test():
#     b=63
#     return b
# print(var_test())
#
# print(f"Python {3 + .2}")
#
# abc = 100, 'python'
# print(abc)
#
# a b c = 1 00
# print(a b c)
#
# n1=5
# n2=13
# while n2>n1:
#     print(n2)
#     n2-=2
#
# n = int(input('Enter the integer: '))
# for i in range(1, n+1):
#     print(i,end='')
#
# from itertools import groupby
# list_1=list(input('Enter the list: '))
# for number, quantity in groupby(list_1):
#     print(tuple([len(list(quantity)),int(number)]), end=' ')
#
# import random as r
# ph_no = []
#
# # the first number should be in the range of 6 to 9
# ph_no.append(r.randint(6, 9))
#
# # the for loop is used to append the other 9 numbers.
# # the other 9 numbers can be in the range of 0 to 9.
# for i in range(1, 10):
#     ph_no.append(r.randint(0, 9))
#
# # printing the number
# for i in ph_no:
#     print(str(i), end="")
#
# from random import randint
# password = str(randint(1000000000, 9999999999))
# ph_no = str("(" + password[::4] + ")" + password[3:6:] + "-" + password[4:8:]).strip()
# ph_no = str(password[::4] + password[3:6:] + password[4:8:]).strip()
# print(ph_no)
#
# def say_hello():
#     print('Hello, World')
#
# for i in range(5):
#     say_hello()
#
# st = "Communication"
# part = st[7:10]
# print(part)
#
# st = "Communication"
# part = st[0:3]
# print(part)
#
# s = "This is your time,\nyou have to win,\nyou have to conquer."
# print(s)
#
# price = float(input("Enter price of one toy: "))
# number_of_toys = int(input("Enter number of toys: "))
# total_price = price * number_of_toys
# print(f"Total price of toys is {total_price}")
#
# b = True
# st = str(b)
# print(st)
#
# num = 5.234
# b = bool(num)
# print(b)
#
# st = ""
# b = bool(st)
# print(b)
#
# print('Twinkle, twinkle, little star,')
# print('How I wonder what you are!')
# print('Up above the world so high,')
# print('Like a diamond in the sky')
#
# x = 1
# y = 1
# z = 1
# n = 2
# rez = []
# for i1 in range(0, x+1):
#     # print(i1)
#     for i2 in range(0, y+1):
#         # print(i2)
#         for i3 in range(0, z + 1):
#             if i1 + i2 + i3 != n:
#                 rez.append([i1, i2 , i3])
# print(rez)
#
# import itertools
# x = 1
# y = 1
# z = 2
# n = 3
#
# x1 = list(range(0, x + 1))
# y1 = list(range(0, y + 1))
# z1 = list(range(0, z + 1))
#
# rez = []
# for i in list(itertools.product(x1,y1,z1)):
#     if sum(i) != n:
#         rez.append(list(i))
# print(rez)
#
# arr = [3,3,3,3,5,5,5,2,2,7]
# arr_set = set(arr)
# print(arr, list(arr_set))
# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# if a < b:
#   print("a is less than b!")
# elif a == b:
#     print("b = a!")
# else:
# 	print("a is greater than b!")
#
# Given a provided test word and a list of potential anagrams, identify the number of items in the list which are valid
# anagrams of the provided word. Two words are anagrams of each other if they both contain exactly the same letters
# (and number of letters, when a letter appears more than once).
# def solution(word, words): # word - is what is compared, words - is with what we compare and it is list
#     rez = 0 # declare counter
#     print(type(rez))
#     for i in words:
#         print(sorted(i), sorted(word))
#         if sorted(i) == sorted(word): # sorted is embedded function of Python
#             rez += 1
#     return f'We have {rez} anagram'
# print(solution('listen', ['silent', 'silent']))
#
# word = 'listen'
# words = ['listen', 'silent', 'dfghjkjhgf', 'dfgggf']
# def is_anagr(word, words):
#     count = 0
#     for i in words:
#         if sorted(i) == sorted(word):
#             count+=1
#     return f'There are {count} anagrams'
#
# print(is_anagr(word, words))

# Write a function to reverse a string. How would you test it? Write down as many test cases as you can.
# str_1 = 'Write a function to reverse a string. How would you test it? Write down as many test cases as you can.'
# print(f'Str_1: {str_1}')
# rev_str_1 = str_1[::-1]
# print(f'Reversed Str_1: {rev_str_1}')


# С помощью цикла создайте массив, заполненный числами:
# //   1,-2,3,-4,5,-6,7,-8,9,-10. Выведите полученный массив в консоль.
# def func_1_10():
#     l1 = list(range(1,11))
#     for i in range(len(l1)+1):
#         if i % 2 == 0:
#             l1[i-1] = -i
#         else:
#             continue
#     return l1
# print(func_1_10())

# Objects in Python
# print(isinstance(4, float), type(4))
# print(isinstance(4, int), type(4))
# print(isinstance(4, object), type(4))

# class Car:
#     model = 'BMW'
#     engint = 1.8
#
# a = Car()
# print(a, isinstance(a, Car), type(a))
#
# b = Car()
# print(b, isinstance(b, Car), type(b))
#
# c = Car()
# print(c, isinstance(c, Car), type(c))

# Public protected private attr and methods
# class BankAccount:
#
#     def __init__(self, name, balance, passport):
#         # self.name = name
#         # self.balance = balance
#         # self.passport = passport
#         # self._name = name # not protected private __
#         # self._balance = balance
#         # self._passport = passport
#         self.__name = name # protected private __
#         self.__balance = balance
#         self.__passport = passport
#
#     def print_public_data(self):
#         self.__print_private_data()
#
#     def print_protected_data(self):
#         print(self._name, self._balance, self._passport)
#
#     def __print_private_data(self):
#         print(self.__name, self.__balance, self.__passport)
#
# account1 = BankAccount('Bob', 100000, 12345678901234)
# account1._BankAccount__print_private_data()
# # account1.print_public_data()
# # account1.print_protected_data()
# # account1.print_private_data()
# # print(dir(account1))
# # print(account1.__name)
# # print(account1.__balance)
# # print(account1.__passport)

# arr_1 = [2, 13, 7, 6, 41, -7, 12, -4, 89, 5]
# for i in arr_1:
#     print(i ** 2, end = '; ')

# c = [x**2 for x in range(10)]
# print ([x for x in c if x % 2 == 0])

# Palyndrome
# a = "1234"
# b = 12321
# # 12321  == 12321
# # 12345  == 54321
# a_r = a[::-1]
# print(a_r)
# if a == b:
#     print('Palyndrome')
# else:
#     print('Not a palyndrome')

# # Fibonacchi Generator
# def fib(num):
#     a,b=1,2
#     for i in range(0,num):
#         yield "{}:{}".format(i+1,a)
#         a,b=b,a+b
# for item in fib(10):
#     print(item, end = "; ")

# lst = [1,2,2,3,3,4,4,5,5]
# print(len(lst), type(lst))
# set_lst = set(lst)
# print(set_lst)
# print(len(set_lst), type(set_lst))

# lst = ['zalupa', 1, 3, 5, 'her']
# rez = 0
# for i in range(0, len(lst)):
#        if isinstance(lst[i], str):
#         rez+=1
# print(rez, type(lst))

# # Fibonacci linear
# first = 0
# second = 1
# length = int(input('Enter the Fib seq length: '))
# for i in range(first, length):
#     first, second = second, first+second
#     print(first, end = ' ')

# # Fibonacci recursive for N-th number
# n = int(input('Enter the number of Fib consequence: '))
# def fib_n_seq(n):
#     if n == 0:
#         return 0
#     if n == 1 or n == 2:
#         return 1
#     if n < 0:
#         return 'Wrong input'
#     else:
#         return fib_n_seq(n-1)+fib_n_seq(n-2)
# print(fib_n_seq(n))

# # Fibonacci function for whole sequence
# n=int(input('Enter the Fib len: '))
# def fib_len(n):
#     a,b=0,1
#     for i in range(a,n):
#         a,b=b,a+b
#         yield i+1, a
# for i in fib_len(n):
#     print(i,end=' ')

# # Fibonacci for one N-th element
# n=int(input('Enter N: '))
# def f_n(n):
#     a,b=0,1
#     for i in range(a,n):
#         a,b=b,a+b
#     yield i+1, a
# for i in f_n(n):
#     print(i)

# Reverse string
# str_to_rev = str(input('Enter the string: '))
# str_reversed = ''.join(reversed(str_to_rev))
# print(str_reversed)

# str_to_reverse = str(input('Enter the string: '))
# str_reveresed = str_to_reverse[::-1]
# print(str_reveresed)

# str_to_reverse = str(input('Enter the string: '))
# str_reversed = ''
# for i in str_to_reverse:
#     str_reversed = i + str_reversed
# print(str_reversed)

# str_to_reverse = 'Zalupa'
# str_reversed = ''
# for i in str_to_reverse:
#     str_reversed = i + str_reversed
# print(str_reversed)

# num=float(input('Enter the number: '))
# def add_even(num):
#     if type(num) != float:
#         return 'Wrong input'
#     if float(num) == 0:
#         return 'Zero is not even nor odd'
#     elif float(num) % 2 == 0:
#         return 'Even'
#     elif float(num) % 2 != 0:
#         return 'Odd'
# print(add_even(num))

# from difflib import SequenceMatcher
# expected = 'Font-family -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,' \
#         '"Noto Sans",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji"'
# actual = 'font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,' \
#         '"Noto Sans",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji"'
# print(f'Expected len: {len(expected)}; Actual len: {len(actual)}')
# def similar(expected, actual):
#     return SequenceMatcher(None, expected, actual).ratio()
# print(similar(expected, actual))

# price = 150
# price = float(price * (100-15)/100)
# print(price)

# a = [12, 10, 50, 100, 24]
# minimum = a[0]
# for number in a:
#     if minimum > number:
#        minimum = number
# print(minimum)

# a = [12, 10, 50, 100, 24]
# minimum = a[0]
# for number in range(len(a)):
#     if minimum > a[number]:
#        minimum = a[number]
# print(minimum)

# lst_1=[1,2,3,4,5,6,7,88,999,-11]
# def min_el(lst_1):
#     min = lst_1[0]
#     for i in lst_1:
#         if i<min:
#             min=i
#     return min
# print(min_el(lst_1))

# str = '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890_'
# ln_str = len(str)
# print(ln_str)


# https://codecollab.io/@dpatrakov/Example#
# Напишите функцию, которая удаляет заданную букву из всех строк в массиве.
# Тип данных в массиве не регламентирован

# char = 'i'
# array = ["class", "collobarate", "click", "hope", "black", "free", 0, []]
# def remove_char(char: str, array: list) -> list:
#     res = []
#     for i in array:
#         if type(i) == str:
#             x = i.replace(char, '')
#             res.append(x)
#         else:
#             res.append(i)
#     return res
# print(remove_char(char, array))

# a="W"*65
# print(a)

# x = 3
# dict ={}
# dict["a"] = x
# print(dict["a"])
# print(dict.items())
# for k, v in dict.items():
#     print(k, v)

# Python program showing a use
# of get() and set() method in
# normal function

# class Geek:
#     def __init__(self, age=0):
#         self._age = age
#
#     # getter method
#     def get_age(self):
#         return self._age
#
#     # setter method
#     def set_age(self, x):
#         self._age = x
#
#
# raj = Geek()
#
# # setting the age using setter
# raj.set_age(21)
#
# # retrieving age using getter
# print(raj.get_age())
#
# print(raj._age)


# l = (1,2,3,4,)
# def get_one(l):
#     yield l
# print(get_one(l))
#
# new_l = [i*2 for i in l]
# new_gen = (i*2 for i in l)
# print(new_l, new_gen)

# lst1=[1,2,3,4,5,6,7,8,9]
# for i in lst1:
#     if i % 2 == 0:
#         print(i, end=';')

# lst1=[1,2,3,4,5,6,7,8,9]
# for i in range(len(lst1)):
#     if lst1[i] % 2 == 0:
#         print(lst1[i], i, end=';')

# a = float(input('Enter the 1th number: '))
# b = float(input('Enter the 2d number: '))
# c = float(input('Enter the 3d number: '))
# def find_middle_from_three_num(a,b,c):
#     if b<a<c:
#         return round(a, 2)
#     elif a<b<c:
#         return round(b, 2)
#     else:
#         return round(c, 2)
# print(find_middle_from_three_num(a,b,c))

# a = int(input('Enter the 3digits number: '))
# def find_middle_dig_from_three_dig_num(a):
#     return (str(a)[1])
# print(find_middle_dig_from_three_dig_num(a))

# c = 'aA2!@_)(_АвЫГав' * 10
# print(c)

# # Example: UDP Server using Python
# import socket
#
# localIP = "127.0.0.1"
#
# localPort = 20001
#
# bufferSize = 1024
#
# msgFromServer = "Hello UDP Client"
#
# bytesToSend = str.encode(msgFromServer)
#
# # Create a datagram socket
#
# UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
#
# # Bind to address and ip
#
# UDPServerSocket.bind((localIP, localPort))
#
# print("UDP server up and listening")
#
# # Listen for incoming datagrams
#
# while (True):
#     bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
#
#     message = bytesAddressPair[0]
#
#     address = bytesAddressPair[1]
#
#     clientMsg = "Message from Client:{}".format(message)
#     clientIP = "Client IP Address:{}".format(address)
#
#     print(clientMsg)
#     print(clientIP)
#
#     # Sending a reply to client
#
#     UDPServerSocket.sendto(bytesToSend, address)

# # Example: UDP Client using Python
# import socket
#
# msgFromClient = "Hello UDP Server"
#
# bytesToSend = str.encode(msgFromClient)
#
# serverAddressPort = ("127.0.0.1", 20001)
#
# bufferSize = 1024
#
# # Create a UDP socket at client side
#
# UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
#
# # Send to server using created UDP socket
#
# UDPClientSocket.sendto(bytesToSend, serverAddressPort)
#
# msgFromServer = UDPClientSocket.recvfrom(bufferSize)
#
# msg = "Message from Server {}".format(msgFromServer[0])
#
# print(msg)

# def arr_app (arr):
#     arr2 = []
#     for value in arr:
#         try:
#             arr2.append(int(value))
#         except ValueError:
#             continue
#     return arr2
# print(arr_app ([10, 2, 30, -15, 5, -33, 'abc', True, False, 'de']))

# Automation
# import csv
# import uuid
#
# languages = input("Languages: ").split(",")
#
# with open('languages.csv', 'w', newline='') as csvfile:
#     filewriter = csv.writer(csvfile, quotechar=',', quoting=csv.QUOTE_MINIMAL)
#     lines = [['#', "ID"]]
#     for i in range(len(languages)):
#         lines.append([i, uuid.uuid4().hex])
#     filewriter.writerows(lines)

# # Ввод переменных
# t_m = int(input('Enter the time for build testing manual: '))  # 30
# t_a = int(input('Enter the time for build testing automation: '))  # 5 five time quicker than manually
# t_a_d = int(input('Enter the time for project automation development: '))  # 300
# number_of_builds = int(input('Enter the builds number: ')) # 12
# # Функция
# def is_aut_worth(t_m, t_a, t_a_d, number_of_builds):
#     tm_fr_mnl = number_of_builds * t_m
#     tm_fr_autmtn = number_of_builds * t_a + t_a_d
#     effect = tm_fr_autmtn - tm_fr_mnl
#     if tm_fr_mnl >= tm_fr_autmtn:
#         return f'Time to start automation! Effect is : "{-effect}" hours'  # 12 builds is the treshhold
#     else:
#         print(f'Manual is still efficient')
#     return f'Time for manual: "{tm_fr_mnl}" hours\nTime for automation: "{tm_fr_autmtn}" hours'
# # Вывод функции
# print(is_aut_worth(t_m, t_a, t_a_d, number_of_builds))

# def solution(message, K):
#     list_of_words = message.split()
#     limit = 0
#     spaces = 0
#     result = []
#     for word in list_of_words:
#         limit += len(word)
#         spaces += 1
#         if limit + spaces - 1 <= K:
#             result.append(word)
#     return ' '.join(result)
# print(solution(input('Enter the phrase: '), int(input('Enter the "K"-length: '))))


# a = '1'*256
# print(a)
# print(f'a: {len(a)}')
#
# b = '1'*512
# print(b)
# print(f'b: {len(b)}')
#
# c = len('Curious, I dug around and found some answers for the ideal lengths of tweets and titles and everything in between. Many of these could have been answered with “it depends,” but where’s the fun in that? Solid research exists to show the value and everething')
# print(c)

# Convert to string
# a = 'Some string'
# str_a_f_l = repr(a)[1:-1]
# str_a = str(a)
# print(str_a_f_l, type(str_a_f_l))
# print(str_a, type(str_a))
# num = 10
# # check  and print type of num variable
# print(num, type(num))
# # convert the num into string and print
# converted_num = "% s" % num
# print(converted_num, type(converted_num))
# v3_init_yandex = 'something to test'
# result, synth_phrase_list, logs_dict, dialog_id = v3_init_yandex
# print(v3_init_yandex)
# str_fl_nm = repr(r"upload_dialogs_for_vgurov_26Oct2021.xlsx")[1:-1]
# print(str_fl_nm, type(str_fl_nm))

