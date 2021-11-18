"""
признаки обьектно ориентированного:
обьекты-обмениваются друг
с другом сообщениями, за обьектом
закрупляется его участок в памяти,
в обьекте есть подобьекты,
у обьекта есть класс.
есть методы/функции.
читать IBM документации-т.к.
качественно написаны.
"""
"""
class monitor:
smsngn415/object/обьект = monitor()/class instance/класс
dir(smsngn415)
object property/свойства обьекта
property name/имя свойства
property value/значение свойства
object method/метод свойства
del rectangle_class:
"""

"""
class rectangle_class:
        height = 0
        width = 0
        def area(self):
            return self.height * self.width

rectangle_1 = rectangle_class()
rectangle_1

a = input("Enter the height, please: ")
rectangle_1.height = int(a)

b = input("Enter the width, please: ")
rectangle_1.width = int(b)

rectangle_1.area
rectangle_1.area()
print("Rectangle area is: ", float(rectangle_1.area()))
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
       return ((self.side_1 + self.side_2 + self.side_3) / 2  * (int(self.side_1 + self.side_2 + self.side_3) / 2  - self.side_1) * (int(self.side_1 + self.side_2 + self.side_3) /2  - self.side_2) * (int(self.side_1 + self.side_2 + self.side_3) / 2  - self.side_3)) ** 0.5
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
e = input('Enter meaning of b: ')
d = input ('Enter meaning of a: ')
b = float(e)
a = float(d)
c = b + a
print("Sum of 'a' and 'b' is: ", float(c))
"""
    
    
















