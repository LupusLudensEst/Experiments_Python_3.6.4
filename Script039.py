"""
Абсолютная величина(применима к и  отр. и к не отриц. числам) или модуль числа |x|, не отрицательное число.
Результат превоащения любого числа в не отрицательное число.
Геометрически это расстояние до числа от начала координат на оси.
Не натурального числа, а вещественного(комплексного) числа-возникающего естественным образом при счёте. Для счёта непрерывных величин.
"""

# absolute number
# abs()

"""
a = -10
b = abs(a)
print(b)


thermometer = input("Enter the temperature, pls: ") 
print(thermometer)

def thermometer(temperature):
    if temperature > 0:
        print('The temperature is', temperature, 'above zero', sep = ' ')
    elif temperature == 0:
            print('The temperature is zero')
    else:
            print('The temperature is', abs(temperature), 'below zero', sep = ' ')
"""

# This is an achievent! Dt 05 January 2017!!!
def thermometer(temp):
    if int(temp) >= 0:
        print('The temperature is:', temp, 'above zero', sep = ' ')
    elif temp == 0:
            print('The temperature is zero:')
    else:
            print('The temperature is:', abs(int(temp)), 'below zero', sep = ' ')
temp = input("Enter the temperature, pls: ")
print(thermometer(temp))








        
