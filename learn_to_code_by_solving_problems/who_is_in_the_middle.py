# https://dmoj.ca/problem/ccc07j1 ccc07j1
one, two, three = int(input()), int(input()), int(input())
# mama = 0
# if one <= two <= three:
#     mama += two
# elif two <= one <= three:
#     mama += one
# else:
#     mama += three
# print(mama)
mama = (one + two + three) - max(one, two, three) - min(one, two, three)
print(mama)
