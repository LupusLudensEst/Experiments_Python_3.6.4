# ЛП0041 - Объекты и классы в питоне - Ленивый питон
# объект-набор характеристик(информационный шкаф, вечно непустеющий холодильник)
# создаём класс, а потом на его базе создаёь оюьекты
# нельзя указывать параметры/атрибуты/поля в скобках, как у функций
# сначала обьявляется класс и только потом обьект
"""
variables = parameters
price = 210
weight = 3500
produced_by = 'Samsongin'
resolution = 'HD'
model = 'smsngn415'
"""

# smsngn415.price//object = 210//parameter

"""
smsngn415.price = 210
smsngn415.weight = 3500
smsngn415.produced_by = 'Samsongin'
smsngn415.resolution = 'HD'
smsngn415.model = 'smsngn415'
"""

class monitor:
    price = 0
    weight = 0
    produced_by = ''
    resolution = ''
    model = ''
    
smsngn416 = monitor()
smsngn416

"""
output = ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'model', 'price', 'produced_by', 'resolution', 'weight']
"""
