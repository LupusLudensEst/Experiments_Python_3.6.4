# https://dmoj.ca/problem/ccc06j1 ccc06j1
burger, side, drink, dessert = int(input()), int(input()), int(input()), int(input())
if burger == 1:
    cal_bur = 461
elif burger == 2:
    cal_bur = 431
elif burger == 3:
    cal_bur = 420
else:
    cal_bur = 0

if side == 1:
    cal_side = 100
elif side == 2:
    cal_side = 57
elif side == 3:
    cal_side = 70
else:
    cal_side = 0

if drink == 1:
    cal_drink = 130
elif drink == 2:
    cal_drink = 160
elif drink == 3:
    cal_drink = 118
else:
    cal_drink = 0

if dessert == 1:
    cal_dessert = 167
elif dessert == 2:
    cal_dessert = 266
elif dessert == 3:
    cal_dessert = 75
else:
    cal_dessert = 0

total_calories = cal_bur + cal_side + cal_drink + cal_dessert
print(f'Your total Calorie count is {total_calories}.')

