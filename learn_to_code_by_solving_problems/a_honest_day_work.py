# https://dmoj.ca/problem/wc18c3j1 wc18c3j1
paint = int(input())
bottlecap = int(input())
dollars_per_bottlecap = int(input())
left_over_liter = 1
cash_for_badges = paint // bottlecap * dollars_per_bottlecap
cash_for_left_over_liter = paint % bottlecap * left_over_liter
total_cash = cash_for_badges + cash_for_left_over_liter
print(total_cash)