# https://dmoj.ca/problem/dmopc15c7p2 dmopc157p2
string = input(str('Enter the string: '))
# 1th desision
# total_words = string.lower().count(' ') + 1
# 2d desision
total_words = 0
for n in string:
    if n == ' ':
        total_words += 1
print(total_words + 1)
