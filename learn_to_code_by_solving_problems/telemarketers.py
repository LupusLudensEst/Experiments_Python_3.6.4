# https://dmoj.ca/problem/ccc18j1 ccc18j1
first, second, third, forth = int(input()), int(input()), int(input()), int(input())
if 8 <= first <= 9 and 8 <= forth <= 9 and second == third:
    print('ignore')
else:
    print('answer')
# python telemarketers.py < telemarketers_input.txt
