# ЛП0040 - Позиционные именованные обязательные необязательные аргументы функции в языке Python
# keyword argument/именованный, positional/позиционный argument, mandatory/required/обязательный argument, optional/non required/не обязательный argument
# return - приказ функции работать, что именно работать
# name = value

"""
def function_zero(a, b):
    return a, b
a = input("Enter the meaning of a, pls: ")
b = input("Enter the meaning of b, pls: ")
print(function_zero(a, b))
"""

"""
def function_one():
    pass
#a = input("Enter the meaning of a, pls: ")
#b = input("Enter the meaning of b, pls: ")
print(function_one())
"""

"""
def function_two(a):# a is required/mandatory argument
    return a
print(function_two())
"""

"""
def function_three(a, b, c):
    return a, b, c
a = input("Enter the meaning of a, pls: ")
b = input("Enter the meaning of b, pls: ")
c = input("Enter the meaning of b, pls: ")

print(function_three(a, b, c))
"""

"""
def function_four(a, b, c=8): # c is keyword/named argument
    return a, b, c
a = input("Enter the meaning of a, pls: ")
b = input("Enter the meaning of b, pls: ")
c = input("Enter the meaning of b, pls: ")# priority is here

print(function_four(a, b))# c is missed intentionally
"""

def function_five(a, b = 5, c, d = 13): 
    return a, b, c, d
print(function_five(3, 5, 8))

