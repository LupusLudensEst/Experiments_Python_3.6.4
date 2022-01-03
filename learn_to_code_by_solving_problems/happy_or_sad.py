# https://dmoj.ca/problem/ccc15j2 ccc15j2
# string = str(input()).split()
# happy, sad = 0, 0
# for i in range(0, len(string)):
#     if ':-)' in string[i]:
#         happy += 1
#     elif ':-(' in string[i]:
#         sad += 1
# if happy == sad and happy != 0 and sad != 0:
#     print('unsure')
# if happy > sad:
#     print('happy')
# elif happy < sad:
#     print('sad')
# elif happy == sad == 0:
#     print('none')

n = input()
h = 0
s = 0
for i in range(0, len(n)):
    if n[i] == ':':
        if i + 1 < len(n):
            if n[i + 1] == '-':
                if i + 2 < len(n):
                    if n[i + 2] == ')':
                        h += 1
                    elif n[i + 2] == '(':
                        s += 1
if s > h:
    print('sad')
elif s < h:
    print('happy')
elif h == s and h != 0:
    print('unsure')
else:
    print('none')


