# $ pip2 install gevent


# #it works
# import gevent
# from gevent import socket
# hosts = ['www.crappytaxidermy.com', 'www.walterpottertaxidermy.com', 'www.antique-taxidermy.com']
# jobs = [gevent.spawn(gevent.socket.gethostbyname, host) for host in hosts]
# gevent.joinall(jobs, timeout=5)
# for job in jobs:
#     print(f'Job value: {job.value}')


# #it works
# clishes = [
#     "At the end of the day",
#     "Having said that",
#     "The fact of that matter is",
#     "Be that as it may",
#     "The bottom line is",
#     "If you will",
#     ]
# print(clishes[3])



# #it works
# for countdown in 5, 4, 3, 2, 1, "Hey!":
#     print(countdown)



# #it works
# quotes = [
#     "Moe"':' "A wise guy, huh?",
#     "Larry"':' "Ow!",
#     "Curly"':' "Nyuk nyuk!",
#     ]
# stooge = "Curly"
# print(stooge, "says:", quotes[2])


# #does not work
# import requests
# url = "https://gdata.youtube.com/feeds/api/standardfeeds/top_rated?alt=json"
# responce = requests.get(url)
# data = responce.json()
# for video in data['feed']['entry'][0:6]:
#     print(video['title']['$t'])


# array = ["Bob", "Alex", "Bob", "John"]
# # print(array)
# array.count("Bob")
# array.count("John")
# dict((x, array.count(x)) for x in set(array) if array.count(x) > 1)
# {'Bob': 2}
# print(dict)


# array = input('Enter the string, please: ')
# print(array)


# array = ["Bob", "Alex", "Bob", "John", "Bob", "Bob", "Bob", "Bob", "Bob", "Bob", "Bob", "Bob", "Bob"]
# array_d = {}.fromkeys(array, 0)
# for a in array:
#     array_d[a] += 1
# print(array_d)
#
# array_d = {}
# for a in array:
#     try: array_d[a] += 1
#     except KeyError: array_d[a] = 1
#
# print(array_d)


# array = ["Bob", "Alex", "Bob", "John"]
# result = {i: array.count(i) for i in array}
# print(result)

# x = int(input('Введите число от 1 до 9: '))
# if 1 <= x <= 3:
#     s = f'{x} is between 1 and 3'
#     print(s)
# elif 4 <= x <= 6:
#     s = f'{x} is between 4 and 6'
#     print(s)
# else:
#     print("Else")

# number=int(input('input NUMBER from 1 to 9: '))
# if number <= 3:
#     s=input('input string ')
#     n=int(input('input numbs replays of string: '))
#     for element in range(n):
#         print(s)
# elif number>=4 and number <=6:
#     m=int(input('input degree of number: '))
#     print(number**m)
# elif number>=7 and number<=9:
#     for num in range(10):
#         print(number+num)
#         num=num+1
# else:
#     print('get over here dud')



# c = divmod(9, 5)
# print(c)



# a = int(True)
# print(a)
# print('-' * 25)
#
# a = int(False)
# print(a)
# print('-' * 25)
#
# a = int(1.987654)
# print(a)
# print('-' * 25)
#
# a = int(1.5e4)
# print(a)
# print('-' * 25)
#
# a = int('99')
# print(a)
# print('-' * 25)
#
# a = int('-123')
# print(a)
# print('-' * 25)
#
# a = float(1.5e4)
# print(a)
# print('-' * 25)
#
# a = float(9.5123456789) * float(1.5123456789)
# print(a)
# print('-' * 25)
#
# b = "We are "
# c = "the champions!"
# a = b + c
# print(a)


# a = '''
# 77 советов, как раскрыть возможности мозга.
# Можете начинать выполнять их прямо с сегодняшнего дня.
# Советы:
# 1. Решайте загадки и головоломки.
# 2. Развивайте амбидекстрию (двуправорукость, способность одинаково хорошо владеть
# правой и левой рукой). Старайтесь чистить зубы, расчесывать волосы, манипулировать
# компьютерной мышью своей не основной рукой. Пишите обеими руками одновременно.
# Меняйте руки во время еды при пользовании ножом и вилкой.
# 3. Работайте с двусмысленностью, неопределенностью. Научитесь наслаждаться такими
# вещами, как парадоксы.
# 4. Изучайте интеллект-карты.
# 5. Блокируйте одно или несколько ощущений. Ешьте с завязанными глазами, затыкайте на
# время уши тампонами, принимайте душ с закрытыми глазами.
# 6. Развивайте сравнительные вкусовые ощущения. Учитесь полноценно чувствовать,
# смаковать вино, шоколад, пиво, сыр и что-нибудь еще.
# 7. Ищите области пересечения между на первый взгляд не связанными между собой
# вещами.
# 8. Учитесь пользоваться клавиатурами с разным расположением клавиш (научитесь
# печатать вслепую).
# 9. Придумывайте новые способы применения для обычных предметов. Сколько разных
# способов вы можете придумать, например, для гвоздя? Десять? Сто?
# 10. Изменяйте свои привычные представления на противоположные.
# 11. Изучайте техники развития творчества.
# 12. Не останавливайтесь на очевидном, устремляйтесь мысленно дальше первого,
# «верного» ответа на вопрос.
# 13. Изменяйте установленный порядок вещей. Задавайте себе вопрос «А что если?..»
# 14. БЕГАЙТЕ, РЕЗВИТЕСЬ!
# 15. Переверните картины, фотографии вверх ногами.
# 16. Развивайте критическое мышление. Опровергайте распространенные заблуждения.
# 17. Изучайте логику. Решайте логические задачи.
# 18. Изучите научный способ мышления.
# 19. Рисуйте, чертите автоматически. Вам не нужно быть для этого художником.
# 20. Мыслите позитивно.
# 21. Займитесь каким-нибудь видом искусства – скульптурой, живописью, музыкой – или
# испытайте себя в каком-либо другом творчестве.
# 22. Изучайте искусство показывать фокусы, развивайте ловкость рук.
# 23. Ешьте продукты, полезные для мозга.
# 24. Стремитесь к тому, чтобы постоянно испытывать легкое чувство голода.
# 25. Занимайтесь физическими упражнениями!
# 26. Сидите прямо.
# 27. Пейте много воды.
# 28. Глубоко дышите.
# 29. Смейтесь!
# 30. Разнообразьте виды деятельности. Выберите для себя увлечение, хобби.
# 31. Заботьтесь о хорошем сне.
# 32. Практикуйте короткий сон.
# 33. Слушайте музыку (не абы что, учтите!).
# 34. Объявите войну своей склонности к отсрочкам, промедлению.
# 35. Ограничивайте себя в применении техники.
# 36. Изучайте материалы по изучению мозга.
# 37. Смените одежду. Ходите босиком.
# 38. Совершенствуйтесь в беседах с самим собой.
# 39. Станьте проще!
# 40. Играйте в шахматы или другие настольные игры.
# 41. Играйте в игры для ума – Судоку, кроссворды и бесчисленное множество других игр к
# вашим услугам.
# 42. Будьте непосредственны, как дети!
# 43. Играйте в видео игры.
# 44. Развивайте чувство юмора! Пишите или сочиняйте шутки.
# 45. Составьте Список 100 (прим.: техника для генерации идей, обнаружения скрытых
# проблем или принятия решений).
# 46. Используйте метод Квота Идей (Idea Quota) ( прим.: метод составления в течение дня
# предварительного списка идей).
# 47. Рассматривайте каждую идею, приходящую к вам. Составьте банк идей.
# 48. Позвольте своим идеям развиваться. Возвращайтесь к каждой из них через
# определенные промежутки времени.
# 49. Проводите «тематическое наблюдение». Постарайтесь, например, отмечать предметы
# красного цвета как можно чаще в течение дня. Отмечайте автомобили конкретной марки.
# Выберите тему и концентрируйтесь на ней.
# 50. Ведите дневник.
# 51. Изучайте иностранные языки.
# 52. Ешьте в разных ресторанах – предпочтение национальным ресторанам.
# 53. Изучайте компьютерное программирование.
# 54. Читайте длинные слова наоборот. !еинеджуборП
# 55. Измените свое окружение – измените место расположения предметов, мебели,
# переезжайте куда-нибудь.
# 56. Пишите! Пишите рассказы, поэзию, заведите блог.
# 57. Изучайте язык символов.
# 58. Изучайте искусство игры на музыкальных инструментах.
# 59. Посещайте музеи.
# 60. Изучайте функционирование мозга.
# 61. Изучайте технику динамического чтения.
# 62. Определите свой стиль обучения.
# 63. Учитесь методу определения дней недели для любой даты!
# 64. Старайтесь по ощущениям оценивать промежутки времени.
# 65. «Приблизительный расчѐт». Чего больше – листьев в лесах Амазонки или нейронных
# связей в мозгу? (ответ)
# 66. Подружитесь с математикой. Боритесь с «неумением считать».
# 67. Стройте Дворцы Памяти.
# 68. Изучайте систему образного мышления для развития памяти.
# 69. Занимайтесь сексом (Извините, здесь без комментариев!).
# 70. Запоминайте имена людей.
# 71. Медитируйте. Тренируйте концентрацию внимания и полное отсутствие мыслей.
# 72. Смотрите фильмы разных жанров.
# 73. Откажитесь от телевизора.
# 74. Учитесь концентрироваться.
# 75. Будьте в контакте с природой.
# 76. Мысленно решайте математические задачи.
# 77. Откажитесь от спешки.
# '''
#
# c = len(a)
# #print(c)
# print(a[0:len(a)], '\n')

# text = ['Fuck', 'your', 'self']
# print(text[::-1])

"""
print(text)
print('-' * 25)

text[0] = 'Love'
print(text)
print('-' * 25)

text[2] = 'neigbour'
print(text)
print('-' * 25)
"""

"""
print(text[::1])
print(text[::-1])
"""


# import tkinter

"""
print('*' * 25)
a = input("Enter the text, pls: ") # This is an achivement! 03 January 2018.
print(a)
text=a
un=set(text.upper())
max=0
fav=''

for u in un:
    c=text.upper().count(u)
    if c>max and u.isalpha():
        max=c
        fav=u
print('Most used symbol is:', fav, '.') 
print('Max used symbol met here:', max, 'times.')

print('*' * 25)
"""
# функции в python являются объектами, соответственно,
# их можно возвращать из другой функции или передавать в качестве аргумента.

"""
# This is an achivement! Dt. 03 January 2018!!!
print('*' * 30)
a = input("Enter the text, pls: ") 
print(a)
text = a
ab = set(text.upper())
max = 0
fav = ''

for a in ab:
    c = text.upper().count(a)
    if c > max and a.isalpha():
        max = c
        fav = a
print('Most used symbol is:', fav,'.') 
print('Max used symbol met here:', max, 'times.')
print('*' * 30)
"""

# homework, make the same but for circle, triangle, hexagon

""" 
class circle_class: 
radius = 0 
constant_pi = 3.141592653589793238 
def area (self): 
return int(self.radius) ** 2 * self.constant_pi 
circle_1 = circle_class() 
circle_1 
a = input("Enter the radius of circle, pls: ") 
print(int(a)) 
circle_1.radius = a 
circle_1.area 
circle_1.area() 
print("-" * 25) 
print(round(circle_1.area())) 
"""

""" 
class triangle_class: 
side_a = 0 
side_b = 0 
side_c = 0 
def area (self): 
return ((self.side_1 + self.side_2 + self.side_3) / 2 * (int(self.side_1 + self.side_2 + self.side_3) / 2 - self.side_1) * (int(self.side_1 + self.side_2 + self.side_3) /2 - self.side_2) * (int(self.side_1 + self.side_2 + self.side_3) / 2 - self.side_3)) ** 0.5 
triangle_1 = triangle_class() 
triangle_1 
a = input("Enter the side one, pls: ") 
print(int(a)) 
triangle_1.side_1 = int(a) 
b = input("Enter the side two, pls: ") 
print(int(b)) 
triangle_1.side_2 = int(b) 
c = input("Enter the side one, pls: ") 
print(int(c)) 
triangle_1.side_3 = int(c) 
triangle_1.area 
triangle_1.area() 
print("-" * 25) 
print(round(triangle_1.area())) 
"""

"""
class hexagone_class:
        side_a = 0
        constant_1 = 3
        constant_2 = 0.5
        constant_3 = 2
def area (self):
return ((self.constant_1 * (self.constant_1 ** (1 / self.constant_3))) / self.constant_3) * (self.side_a ** self.constant_3)
        hexagone_1 = hexagone_class()
        hexagone_1
        a = input("Enter the side lenght, pls: ")
        print(int(a))
        hexagone_1.side_a = int(a)
        hexagone_1.area
        hexagone_1.area()
    print("-" * 25)
    print(round(hexagone_1.area()))
"""
"""
class hexagone_class
    side_a = 0
    constant_1 = 3
    constant_2 = 0.5
    constant_3 = 2
    def area (self):
        return ((self.constant_1 * (self.constant_1 ** (1 / self.constant_3))) / self.constant_3) * (
                self.side_a ** self.constant_3)

    hexagone_1 = hexagone_class()
    hexagone_1
    a = input("Enter the side lenght, pls: ")
    print((a))
    hexagone_1.side_a = int(a)
    hexagone_1.area()
    print("-" * 25)
    print(round(hexagone_1.area()))
"""

"""
 class rectangle_class:
    height = 0
    width = 0
    def area(self):
        return self.height * self.width

    rectangle_1 = rectangle_class()

    rectangle_1.height = 2
    rectangle_1.width = 2

    rectangle_1.area()

    rectangle_1.area
    print(rectangle_1.area())
"""
"""
c = input('Enter something, pls')
print(c)
"""

"""
e = input('Enter meaning of b: ')
d = input ('Enter meaning of a: ')
b = int(e)
a = int(d)
c = b + a
print(int(c))
"""

"""
from tkinter import *
import math

root = Tk()
root.title('Developing of function chart y = sin(x)')
root.geometry('1020x620')

canvas = Canvas(root, width = 1020, height = 620, bg ='#002' )
# lines of grid on vertical
for y in range(21):
    k = 50 * y
    canvas.create_line(10 +  k, 610, 10 + k, 10, width = 1, fill = '#191938')
    
# lines of grid on horizontal
for x in range(13):
    k = 50 * x
    canvas.create_line(10, 10 +  k, 1010, 10 + k, width = 1, fill = '#191938')

# lines coordinates x and y
canvas.create_line(10, 10, 10, 610, width = 1, arrow = FIRST, fill = 'white') # y axle
canvas.create_line(0, 310, 1010, 310, width = 1, arrow = LAST, fill = 'white') # x axle

# x(t) = Asin(wt + phi)


 
w = 0.0209 # cicle frequency
phi = 10 # moving chart on x axle
A = 200 # amplitude
dy = 310 # moving chart on y axle

xy = []
for x in range(1000):
    y = math.sin(x * w)
    xy.append(x + phi)
    xy.append(y * A +dy)

    
sin_line = canvas.create_line(xy, fill = 'blue')
    


canvas.pack()
root.mainloop()
"""

"""
# Just practice 01 09 2018
a = input('Enter the first number , please: ')
print(float(a))
b = input('Enter the second number , please: ')
print(float(b))
if float(a) > float(b):
    print(float(b))
else:
        print('Try again')
"""

"""
from math import *
# if key == "√x":
sqrt_root = input("Enter the number extract square root, please: ")
print(sqrt(float(sqrt_root)))

# if key == "x^2":
power_two = input("Enter the number to rise to power two, please: ")
print(float(power_two) ** 2)
"""

''' Program make a simple calculator that can add, subtract, multiply and divide using functions '''

# This function adds two numbers 
# def add(x, y):
#    return x + y
#
# # This function subtracts two numbers
# def subtract(x, y):
#    return x - y
#
# # This function multiplies two numbers
# def multiply(x, y):
#    return x * y
#
# # This function divides two numbers
# def divide(x, y):
#    return x / y
#
# # This function rise number into power
# def pow(x, y):
#    return x ** y
# # This function extract root of value Y from X
# def root(x, y):
#     c = 1 / y
#     return(x ** c)
# # This function counts length of circle based on radius
# def circle_lenght(x):
#     return(3.141592653589793238462643383279  * x)
#
# print("Select operation, please")
# print("*" * 25)
# print("1.Add")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Divide")
# print("5.Rise X into power Y")
# print("6.Extract root of value Y from X")
# print("7.Length of circle based on radius as first number")
# # Take input from the user
# choice = input("Enter choice(1/2/3/4/5/6/7):")
#
# num1 = round(float(input("Enter first number: ")), 2)
# num2 = round(float(input("Enter second number: ")), 2)
#
# if choice == '1':
#    print(num1,"+",num2,"=", add(num1,num2))
#
# elif choice == '2':
#    print(num1,"-",num2,"=", subtract(num1,num2))
#
# elif choice == '3':
#    print(num1,"*",num2,"=", multiply(num1,num2))
#
# elif choice == '4':
#    print(num1,"/",num2,"=", divide(num1,num2))
#
# elif choice == '5':
#     print(num1, "**", num2, "=", pow(num1,num2))
#
# elif choice == '6':
#     print(num2, "√ ", num1, "=", root(num1, num2))
#
# elif choice == '7':
#     print("Circle lenght is: ", "=", circle_lenght(num1), ", if radius is: ", num1, ".")
#
# else:
#    print("Invalid input")

# Arrays

# cities = ['Moscow', 'New_York', 'washington', 'Novosibirsk', 'Orlando', 'Miami', 'Miramar', 'Fort_Lauderdale']
# length = len(cities)
# print(f' \nArray: {cities}.\nLength of the array is:  {length}.')
# print(cities[0],',',cities[-1],'.', cities[2].title(),'.', cities[2].upper(),'.')
# cities[2] = 'Tula'
# print(cities[0],',',cities[-1],'.', cities[2].title(),'.', cities[2].upper(),'.')
# cities.append('Dallas')
# length = len(cities)
# print(f' \nArray: {cities}.\nLength of the array is:  {length}.')
# cities.insert(2, 'Buffalo')
# print(f'{cities},\n{len(cities)}.')
# del cities[-1]
# print(f'{cities}.\n{len(cities)}')
# cities.remove('Miami')
# print(f'{cities}.\n{len(cities)}')
# deleted_city = cities.pop()
# print(f'Deleted city is: {deleted_city},\n{cities},\n{len(cities)}')
# cities.sort()
# print(f'{cities}.\n{len(cities)}')
# cities.sort(reverse=True)
# print(f'{cities}.\n{len(cities)}')
# cities.reverse
# print(cities, end='\n\n\n')

# cars =['bmw', 'vw', 'audi', 'mercedes', 'horch', 'opel', 'chevy']
# length = len(cars)
# print(f'Cars list is: {cars}.\nLength is: {length}.')
#
# for x in cars:
#     print(x.upper())
#
# my_cars = cars[::]
# print(my_cars)
#
# my_cars = cars[:]
# del my_cars[-1]
# print(my_cars)

# mynumber_list = list(range(0, 10))
# print(f'\n{mynumber_list}')
#
# for x in mynumber_list:
#     x = x * 2
#     print(f'{x}')
#
# mynumber_list.sort(reverse=True)
# print(f'\n{mynumber_list}')
#
# print(f'\n{max(mynumber_list)}')
#
# print(f'\n{min(mynumber_list)}')
#
# print(f'\n{sum(mynumber_list)}')


# x = [1, 2, 'car', 10, 20]
# print(x)
# import numpy as np
# t = np.linspace(0, 1, 5)
# print(t)
# y = np.array([1, 2, 3.5, 10, 20])
# print(y)
# import matplotlib.pyplot as plt
# plt.plot(t, y, 'ro')
# plt.show()
# var = x[1:-1]
# print(var)

#---
# print("Heelo, world!")
# x = ("Heelo, world!")
# print(x)
# print(type(x))
#---
# a = 2
# b = 5
# tmp = a
# a = b
# b = tmp
# c = a + b
# print(c)
# print(f'{a, b}')
# print(type(c))
#---
# a = 2
# b = 5
# tmp1 = a
# tmp2 = b
# a = tmp2
# b = tmp1
# print(f"{a, b}")
#---
# a = b = c = 0 # каскадное присваивание
# d, e, f = 1, 2, 3 # множественное присваивание
# print(f"{a, b, c}\n{d, e, f}")
#---
# a = 2
# b = 3
# tmp2, tmp1 = a, b
# a, b = tmp1, tmp2
# print(f'{a, b}')
#---
# a = 2 # присвоеие через временный кортеж, после вычисления удаляется
# b = 3
# a, b = b, a
# print(f"{a, b}")
#---
# унарные операции > приоритета, чем бинарные
"""
1. 
-возведение в степень
x ** y
-корень из 3 квадратный
3 ** 0.5
-а в степени б в степени с
a ** b ** c
2. унарный минус
- x = -x
3. умножение и деление
 x * y
 x / y
 деление с отбрасыванием остатка
 x // y
 деление с остатком 
 x % y
 -в ахритектурно-ориентированных языках
 --(-12)//10=-1 div
 --(12)%10=-2 mod
 - в питоне, не ахритектурно-ориентированном языке
 --(-12)//5=-3 div
 --(12)%=3 mod 
 --(-11)//10=-2
 --(-11)%10=9
 4. сложение и вычитание
 x-y
 z+y
 """
# циклы и ветвления
# while, for(syntax sugar)
# итерация-однократное выполнение тела цикла
# range(start, stop, step)

# full_name = str(input("Enter the full name: "))
# print(full_name, type(full_name))
# short_full_name = (full_name.split()[0])[0].upper() + '.' + (full_name.split()[1])[0].upper() + '.'
# print(short_full_name, type(short_full_name))

# Given an array of numbers (in string format), you must return a string.
# The numbers correspond to the letters of the alphabet in reverse order: a=26, z=1 etc.
# You should also account for '!', '?' and ' ' that are represented
# by '27', '28' and '29' respectively.
# def switcher(arr):
#     d = {str(i): chr(123-i) for i in range(1,27)}
#     d.update({'27':'!'})
#     d.update({'28':'?'})
#     d.update({'29':' '})
#     d.update({'0':''})
#     return ''.join([d[str(i)] for i in arr])

# import string
# letters = string.ascii_lowercase[::-1] + '!? '
# def switcher(arr):
#     return ''.join([letters[ch-1] for ch in map(int, arr) if ch])

# chars = "_zyxwvutsrqponmlkjihgfedcba!? "
# def switcher(arr):
#     return "".join(chars[int(i)] for i in arr if i != "0")

# STR = "+zyxwvutsrqponmlkjihgfedcba!? "
# def switcher(arr):
#     return "".join(STR[int(x)] for x in arr).replace("+", "")

# def century(year):
#     # Finish this :)
#     return (year) // 100 + 1
# print(century(2021))

# def even_or_odd(number):
#     # return 'Odd' if number % 2 else 'Even'
#     if (number % 2) == 0:
#         return 'Even'
#     else:
#         return 'Odd'
#
# print(even_or_odd(4))

# # Your task is to write a function
# # which returns the sum of following series upto nth term(parameter).
# def series_sum(n):
#     # Happy Coding ^_^
#     count = 0
#     for i in range(n):
#         count += 1/(1+(3*i))
#     # return format(count, '.2f')
#     return round(count, 2)
#
# print(series_sum(3))

# factirial
# import math
# print(math.factorial(int(input("Enter the integer: "))))

def factorial(n):
    count = 1
    i = 1
    while i < n + 1:
        count *= i
        i += 1
    return f"Factorial of {n} = {count}"

print(factorial(int(input("Enter the integer: "))))











