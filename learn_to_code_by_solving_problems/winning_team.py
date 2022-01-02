# https://dmoj.ca/problem/ccc19j1 ccc19j1
three_point_apple, two_point_apple, one_point_apple = int(input()), int(input()), int(input())
three_point_bananas, two_point_bananas, one_point_bananas = int(input()), int(input()), int(input())
A = three_point_apple * 3 + two_point_apple * 2 + one_point_apple * 1
B = three_point_bananas * 3 + two_point_bananas * 2 + one_point_bananas * 1
if A > B:
    print('A')
elif A < B:
    print('B')
else:
    print('T')




