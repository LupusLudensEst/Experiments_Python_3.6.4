# SELECT id FROM cars WHERE (price <= 50000 AND year >= 2018 AND condition = 'New')
# OR (price <= 20000 AND year >= 2010 AND condition = 'Used') ORDER BY id ASC;

# select max(price) from cars where price not in(select max(price) from cars))

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# def solution(message, K):
#     # write your code in Python 3.6
#     list_of_words = message.split() # split() method returns a list of all the words in the string, using str as the separator (splits on all whitespace if left unspecified), optionally limiting the number of splits to num.
#     print(list_of_words)
#     limit = 0 # counter of the length, can not end by the space
#     spaces = 0 # counter of the spaces
#     result = [] # array to where we gather limit and spaces
#     for word in list_of_words:
#         limit += len(word) # add by the whole words only
#         spaces += 1 # add spaces
#         if limit + spaces - 1 <= K: # if total string without the space at the end is less or equal to K
#             result.append(word) # add word to array to where we gather limit and spaces
#     return ' '.join(result)
# print(solution(input('Enter the phrase: '), int(input('Enter the length desired: '))))

def tesla(message, k):
    return(message[:message[:k].rfind(" ")] if message[:k].rfind(" ")>0 else "Empty string")
print(tesla(input("Enter the string: "), int(input("Enter the limit: "))))


# def truncate_string(message, K):
#     before_crop = message.split()
#     limit = 0
#     spaces = 0
#     after_truncation = []
#     for word in before_crop:
#         limit += len(word)
#         spaces += 1
#         if limit + spaces - 1 <= K:
#             after_truncation.append(word)
#     return ' '.join(after_truncation)
# print(truncate_string(input("Enter the string: "), int(input("Enter the limit: "))))

# def tesla(message, k):
#     return(message[:message[:k].rfind(" ")] if message[:k].rfind(" ")>0 else "Empty string")
# print(tesla(input("Enter the string: "), int(input("Enter the limit: "))))

# truncate the string to the given length-K, no space at the end of the string,
# no parts of the words-the whole words are only

# def truncate_phrase(message, K):
#     before_truncation = message.split()
#     limit = 0
#     spaces = 0
#     after_truncation = []
#     for word in before_truncation:
#         limit += len(word)
#         spaces += 1
#         if limit + spaces - 1 <= K:
#             after_truncation.append(word)
#     return ' '.join(after_truncation)
# print(truncate_phrase(input("Enter the phrase: "), int(input("Enter the limit: "))))

# integer = int(input('Inter integer: '))
# print(bin(integer)[2:])

# N = int(input('Enter the N: '))
# def solution(N):
#     # write your code in Python 3.6
#     bin(N)
# print(solution(N))

# def solution(N):
#     bin_rep = str(bin(N))[2:] # truncate two first characters
#     bin_gap = False
#     bin_max = 0
#     bin_counter = 0
#     for symbol in bin_rep:
#         if symbol == '1':
#             if bin_max < bin_counter:
#                 bin_max = bin_counter
#             bin_gap = True
#             bin_counter = 0
#         elif bin_gap:
#             bin_counter += 1
#     return bin_max
# NUM = int(input('Enter N: '))
# print(str(bin(NUM))[2:], solution(NUM))

# def solution(N):
#   return len(max(bin(N)[2:].strip('0').strip('1').split('1')))
# # O(N)
# NUM = int(input('Enter N: '))
# print(bin(NUM)[2:], solution(NUM))

# temperatures = [0] * 365
# temperatures[0] = 25
# print(len(temperatures), temperatures)
# def plus_temp(temperatures):
#   positive_temp_days = 0
#   N = len(temperatures)
#   for i in range(N):
#     if temperatures[i] <= 0:
#       positive_temp_days += 1
#   return positive_temp_days
# print(plus_temp(temperatures))

# 2.3: Reversing an array.
# def reverse(A):
#   N = len(A)
#   for i in range(N // 2):
#       k = N - i - 1
#       A[i], A[k] = A[k], A[i]
#   return A
# print(reverse(['1','2','3']))

# A = ['3', '2', '1']
# A.reverse()
# print(A)

# A = input("Enter the string: ")
# B = A[::-1]
# print(B)

# A = ['3', '2', '1']
# B = A[::-1]
# print(B)

# A = str(input("Enter the string: "))
# B = A[::-1]
# print(B)

# def solution(A, K):
#   if K == 0 or len(A) / K == 0:
#     return A
#   if K > len(A):
#     K = K % len(A)
#   A = A[len(A) - K:len(A)] + A[0:len(A) - K]
#   return A
# print(solution(['3', '2', '1'], int(input('Enter K: '))))
# # O(1)

# def solution(A, K):
#   if K == 0 or len(A) == 0 or K == len(A):
#     return A
#   K = -(K % len(A))
#   return A[K:] + A[:K]
# print(solution(['3', '2', '1'], int(input('Enter K: '))))
# # O(1)

# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# if a < b:
#   print('{} < {}'.format(a, b))
# elif a == b:
#   print('{} = {}'.format(a, b))
# else:
#   print('{} > {}'.format(a, b))

# import os, glob
# os.chdir(("C:\Everything\IT\Testing\Automation_08_09_2019\Info_files"))
# for file in glob.glob("*.bmp"):
#   print(file)

# # Fibonachi sequence
# a,b = 0,1
# for i in range(1,10):
#   a, b = b, a + b
#   print(a,b)

# for i in range(int(input(f'Input the Range: '))):
#   if i%3==0 and i%5==0:
#     print(f'{i} Fizz Buzz')
#   elif i%3==0:
#     print(f'{i} Fizz')
#   else:
#     print(f'{i} Buzz')

# def solution(A):
#   # write your code in Python 3.6
#   result = 0
#   for number in A:
#       result ^= number # число, не имеющее пары-Бинарный  "Исключительное ИЛИ" и бинарный "ИЛИ"
#   return result
# print(sorted([9, 3, 9, 3, 9, 7, 9]))
# print(solution([9, 3, 9, 3, 9, 7, 9]))

# def solution(A):
#   if len(A) == 1:
#     return A[0]
#   A = sorted(A)  # O(n*log(N) or N)
#   for i in range(0, len(A), 2):  # O(N)
#     if i + 1 == len(A):
#       return A[i]
#     if A[i] != A[i + 1]:
#       return A[i]
# # O(N*log(N) or O(N))
# print(sorted([9, 3, 9, 3, 9, 7, 9]))
# print(solution([9, 3, 9, 3, 9, 7, 9]))

# An array A consisting of N different integers is given.
# The array contains integers in the range [1..(N + 1)],
# which means that exactly one element is missing.
# Your goal is to find that missing element.
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# def solution(A):
#     # write your code in Python 3.6
#     n = len(A)+1
#     result = n * (n + 1)//2
#     return result - sum(A)
# print(solution([2, 3, 1, 5]))

# A non-empty array A consisting of N integers is given.
# A permutation is a sequence containing each element from 1 to N once, and only once.
# For example, array A such that:
#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
#     A[3] = 2
# is a permutation, but array A such that:
#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# def solution(A):
#     # write your code in Python 3.6
#     if len(A) == 0:
#         return 0
#     max_element = max(A)
#     if max_element - len(A) > 1:
#         return 0
#     actual_sum = sum(A)
#     check_sum = sum(range(1, len(set(A)) + 1))
#     if actual_sum != check_sum:
#         return 0
#     return 1
# print(solution([4, 1, 3, 2]))
# print(solution([4, 1, 3]))

# A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.
# Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ...,
# A[P − 1] and A[P], A[P + 1], ..., A[N − 1].
# The difference between the two parts is the value of:
# |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|
# In other words, it is the absolute difference between the sum of the first part and the sum of the second part.
# For example, consider array A such that:
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# def solution(A):
#     # write your code in Python 3.6
#     left = A[0]
#     right = sum(A[1::])
#     diff = abs(left - right)
#
#     for p in range(1, len(A)):
#         ldiff = abs(left - right)
#         if ldiff < diff:
#             diff = ldiff
#         left += A[p]
#         right -= A[p]
#
#     return diff
# print(solution([3, 1, 2, 4, 3]))


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# I RESOLVED IT MYSELF!!!
# def solution(X, Y, D):
#     # write your code in Python 3.6
#     if (Y - X)%D == 0:
#         return (Y - X)//D
#     else:
#         return (Y - X)//D + 1
# print(solution(10, 185, 50))

# def solution(X, Y, D):
#     # write your code in Python 3.6
#   return (Y-X)//D if (Y-X)%D == 0 else (Y-X)//D + 1
# print(solution(10, 185, 50))

# def solution(A):
#   # write your code in Python 3.6
#   print(sorted(A))
#   for i in range(len(A)):
#     return (len(A) + 1) * (len(A) + 2) // 2 - sum(A)
# print(sum([6, 3, 1, 5, 4, 7]), solution([6, 3, 1, 5, 4, 7]))

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# def solution(A):
#     # write your code in Python 3.6
#     N = len(A)
#     fib = [0] * 27
#     fib[1] = 1
#     for i in range(2, 27):
#         fib[i] = fib[i-1] + fib[i-2]
#
#     sum = []
#     count = 0
#     for a in A:
#         if a == 1:
#             sum.append(count)
#         count += 1
#     sum.append(count)
#     sum.reverse()
#
#     result = 0
#     position = -1
#     i = len(sum)
#     while position != N:
#         go = False
#         for idx, s in enumerate(sum[:i]):
#             d = s - position
#             if d in fib:
#                 position += d
#                 result += 1
#                 i = idx
#                 go = True
#                 break
#         if not go: return -1
#
#     return result
# print(solution([0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]))

#     A.append(1)
#     N = len(A)
#     fib = [0] * 27
#     fib[1] = 1
#     for i in range(2, 27):
#         fib[i] = fib[i - 1] + fib[i - 2]
#         if fib[i] > N:
#             fib = fib[2:i]
#             break
#
#     reachable = [-1] * N
#     for jump in fib:
#         if A[jump - 1] == 1: reachable[jump - 1] = 1
#
#     for i in range(N):
#         if A[i] == 1 and reachable[i] < 0:
#             min = N + 1
#             minidx = -1
#             for jump in fib:
#                 pre = i - jump
#                 if pre < 0 or reachable[pre] < 0:
#                     continue
#                 if min > reachable[pre]:
#                     min = reachable[pre]
#                     minidx = pre
#             if minidx != -1:
#                 reachable[i] = min + 1
#
#     return reachable[-1]
# print(solution([0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]))

# a = [1, 'two', 3, 'four']
# print(a)
# a.append('5')
# print(a)
# b = a
# print(b)
# b.extend("six")
# print(b)

# a = [1, 'two', 3, 'four', 5, 'six']
# a.remove(1) # removes element by value
# print(a, len(a))
# del a[2] # removes element by index
# print(a, len(a))
# a.pop(-1)
# print(a, len(a)) # removes element by index

# from numpy import array
# a = array([4,8,20,16])
# a = a / 4
# print(a)

# b = [4,8,20,16]
# b = b / 4

# # Difference Between
# # LIST - square braces(BRACKETS) # []
# # TUPLE - round braces(PARENHTESES), immutable(can not changed since created) # ()
# # SET - should be declared. output is in curly braces(BRACES) # {}.  is an unordered collection of items.
# # every set element is unique (no duplicates) and must be immutable (cannot be changed).
# # however, a set itself is mutable. We can add or remove items from it.
# # DICTIONARY - curly braces(BRACES). Indexed by key/s. # {} made up from key:value pairs. keys are immutable since declared.
# # values are mutable.
#
# list1 = ["Computer", "Printer", "TV", "Camera", "Notebook", 89, 88.5]
# list1[0] = "PC"
# print(f'list1: {list1}\n')
#
# tuple1 = ("Computer", "Printer", "TV", "Camera", "Notebook", 89, 88.5)
# # tuple1[0] = "PC" # does not work. TypeError: 'tuple' object does not support item assignment
# print(f'tuple1: {tuple1}\n')
#
# set1 = set(["Computer", "Printer", "TV", "Camera", "Notebook", 89, 88.5])
# print(f'set1: {set1}\n')
#
# dictionary1 = {
# 1:"Monday",
# 2:"Tuesday",
# 3:"Wednsday",
# 4:"Thursday",
# 5:"Friday",
# 6:"Saturda",
# 7:"Sunday"
# }
# print(f'{dictionary1}\n')

# Palindrome Program In Python
# def palindrome(num):
#     x1 = num[::-1] # it starts from the end towards the first taking each element. So it reverses a. This is applicable for lists/tuples as well.
#     if x1 == num:
#         print(f'"{x1}" is a palindrome')
#     else:
#         print(f'"{x1}" is not a palindrome')
# print(palindrome(input('Enter the string: ').lower()))

# # Palindrome
# a=input("Enter the string: ")
# b=a[::-1]
# if b==a:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

# # Palindrome
# a = str(input('Enter the string: '))
# a_rev = a[::-1]
# if a == a_rev:
#     print('Palindrome')
# else:
#     print('Not a palindrome')

# # Factorial Program In Python
# def factorial(num):
#     if num == 1:
#         return num
#     else:
#         return num * factorial(num - 1)
# print(factorial(int(input('Enter the number: '))))

# # Fibonacci Series Program In Python
# a = int(input('Enter the 1th number: '))
# b = int(input('Enter the 2d number: '))
# n = int(input('Enter the number of elements: '))
#
# print(a, b, end = " ")
# while n - 2:
#     c = a + b
#     a = b
#     b = c
#     print(c, end = " ") # end=" ")  # Appends a space instead of a newline in Python 3
#     n = n - 1

# # Armstrong Number Program In Python
# num = int(input('Enter the number: '))
# s = 0
# temp = num
# while temp > 0:
#     c = temp % 10
#     s += c**3
#     temp //= 10
# if num == s:
#     print(f'{num}: is an armstrong number')
# else:
#     print(f'{num}: is not an armstrong number')

# # Calculator Program In Python
# def add(a, b):
#     return a + b
#
#
# def substraction(a, b):
#     return a - b
#
#
# def multiplication(a, b):
#     return a * b
#
#
# def division(a, b):
#     return a / b
#
#
# def si(p, r, t): # simple interest
#     return round((p * r * t) / 100, 2)
#
#
# def ci(P, R, T): # cumulative interest
#     return round(P * pow((1 + R / 100), T), 2)
#
#
# def sqr(num):
#     return num ** 2
#
#
# def st(num):
#     return num ** 0.5
#
# print(si(10000, 10, 5))

# # Pattern Program In Python
# num = int(input('Enter the number: '))
# m = (2 * num) - 2
# for i in range(0, num):
#     for j in range(0, m): # nested loop for
#         print(end = " ")
#     m = m - 1
#     for j in range(0, i + 1):
#
#         print("*", end = " ")
#     print("")

# # Leap Year Program In Python
# year = int(input('Enter the year: '))
#
# if year % 400 == 0:
#     print(f'{year}: is a leap year')
# elif year % 4 == 0:
#     print(f'{year}: is a leap year')
# elif year % 100 == 0:
#     print(f'{year}: is not a leap year')
# else:
#     print(f'{year}: is not a leap year')

# # Prime Number Program In Python. Can be devided by itself and 1 only
# number = int(input('Enter the number to be checked: '))
#
# for i in range(2, number):
#     if number % i == 0:
#         print(f'{number}: is not a prime number')
#         break
#     else:
#         print(f'{number}: is  a prime number')
#         break

# # Program To Find Area In Python
# # Area of a circle = 3.142 * r * r
# # Area of a cube = 6 * a * a
# # Area of a cylinder = 2 * 3.142 * r * h + 2 * 3.142 * r * r
# import math
#
# pi = math.pi
#
#
# def circle(radius):
#     return pi * (radius ** 2)
#
#
# def cube(side):
#     return 6 * side * side
#
#
# def cylinder(radius, height):
#     return 2 * pi * radius + 2 * pi * height
#
#
# def sphere(radius):
#     return 2 * pi * (radius ** 2)
#
#
# print(cylinder(10, 12))

# # Program To Reverse A List In Python
# a = [1, 'edurika', 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(a[::-1])
#
# # Function reversing string
# def rev_str(x):
#     return x[::-1]
# str_reverse1 = rev_str(str(input('Enter the string to be reversed: ')))
# print(str_reverse1)

# # Set
# thisset = {"apple", "banana", "cherry"}
# print(f'Set: {thisset}\n')
#
# for i in thisset:
#     print(f'{i}\n')
#
# print("banana" in thisset)
#
# thisset.add("orange")
# print(thisset)
#
# thisset.update(["orange", "mango", "grapes"])
# print(thisset)
# print(len(thisset))
#
#
# thisset.remove("banana")
# print(thisset)
# print(len(thisset))
#
# thisset.discard("banana")
# print(thisset)
# print(len(thisset))
#
#
# thisset.clear()
# print(thisset)
# print(len(thisset)) # thisset is deleted
#
# del thisset
# print(thisset)
# print(len(thisset))

# # sum_integers_args.py
# def my_sum(*args):
#     result = 0
#     # Iterating over the Python args tuple
#     for x in args:
#         result += x
#     return result
#
# print(my_sum(1, 2, 3, 4))

# # **kwargs
# # concatenate_keys.py
# def concatenate(**kwargs):
#     result = ""
#     # Iterating over the keys of the Python kwargs dictionary
#     for arg in kwargs.values():
#         result += arg
#     return result
# print(concatenate(a="Real ", b="Python ", c="Is ", d="Great", e="!"))

# # print_list.py
# my_list = [1, 2, 3]
# print(my_list)
#
# # print_unpacked_list.py
# my_list = [1, 2, 3]
# print(*my_list)

# # unpacking_call.py
# def my_sum(a, b, c):
#     print(a + b + c)
# my_list = [1, 2, 3]
# my_sum(*my_list)

# def my_sum(a, b, c):
#     print(a + b + c)
# my_list = [1, 2, 3, 4] # intentional mistake
# my_sum(*my_list)

# # sum_integers_args_3.py
# def my_sum(*args):
#     result = 0
#     for x in args:
#         result += x
#     return result
#
# list1 = [1, 2, 3]
# list2 = [4, 5]
# list3 = [6, 7, 8, 9]
#
# print(my_sum(*list1, *list2, *list3))

# my_list = [1, 2, 3, 4, 5, 6]
# a, *b, c = my_list
# print(a)
# print(b)
# print(c)

# # string_to_list.py
# a = [*"RealPython"]
# print(a)

# # mysterious_statement.py
# *a, = "RealPython"
# print(a)

# def solution(message, K):
#     before_cut = message.split()
#     limit = 0
#     spaces = 0
#     result = []
#     for word in before_cut:
#         limit += len(word)
#         spaces += 1
#         if limit + spaces - 1 <= K:
#             result.append(word)
#     return ' '.join(result)
# print(solution(input('Enter the phrase: '), int(input('Enter the length desired: '))))

# def sol_bin(N):
#     return len(max(bin(N)[2:].strip('0').strip('1').split('1')))
# print(sol_bin(int(input('Enter N: '))))

# # Remove any duplicates from a List:
# mylist = ["a", "b", "a", "c", "c"]
# mylist = list(dict.fromkeys(mylist))
# print(dict.fromkeys(mylist), mylist)

# # Practice how reverse the string
# a = str(input('Enter the string: '))
# a_rev = a[::-1]
# print(a_rev)

# # Practice how reverse the string
# a=str(input("Enter the string: "))
# b=''.join(reversed(a))
# print(b)

# # Practice how reverse the list
# a = [1,2,3,4,5,6,7,8,9]
# a_rev = a[::-1]
# print(a_rev)




