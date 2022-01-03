# https://dmoj.ca/problem/ccc15j1 ccc15j1
month = int(input())
day = int(input())
if month == 2 and day == 18:
    print('Special')
elif (month == 2 and day < 18) or (month < 2):
    print('Before')
else:
    print('After')
