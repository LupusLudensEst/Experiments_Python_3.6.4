# https://dmoj.ca/problem/wc17c3j3 wc17c3j3
password = str(input())
# length = len(password)
# lower = 0
# for i in password:
#       if i.islower():
#             lower += 1
# upper = 0
# for i in password:
#       if i.isupper():
#             upper += 1
# digit = 0
# for i in password:
#       if i.isdigit():
#             digit += 1
# if lower >= 3 and upper >= 2 and digit >= 1 and 8 <= length <= 12:
#     print('Valid')
# else:
#     print('Invalid')

length = len(password)
lower = 0
for i in password:
      if i in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
            lower += 1
upper = 0
for i in password:
      if i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
            upper += 1
digit = 0
for i in password:
      if i.isdigit():
            digit += 1
if lower >= 3 and upper >= 2 and digit >= 1 and 8 <= length <= 12:
    print('Valid')
else:
    print('Invalid')
