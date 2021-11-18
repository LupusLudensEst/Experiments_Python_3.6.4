"""
https://lenivii.wordpress.com/2015/06/
https://docs.google.com/document/d/1qSeDWsczxpv5fqKLAH5Uhi_GqP6JLdYJ5JFZ-K96CHA/edit
"""

b = ['text', 10, 'oneMoreText', 1.5]
order = 1
for fragment in b:
    print(order, '. ',  fragment, sep = '')
    order = order + 1

superList = ['super', 'evenMoreSuper', 'theSuperest']
order = 1
for super in superList:
    print(order, '. ', super, sep = '')
    order = order + 1


b = ['Timothy', 'Sean', 'Anthony', 'Mike']
order = 1
for human in b:
    print(order, '. ', human, sep = '')
    order = order + 1

b = ['Timothy', 'Sean', 'Anthony', 'Mike']
order = 1
for human in b:
    print(order, '. ', b[order], sep = '')
    order = order + 1

