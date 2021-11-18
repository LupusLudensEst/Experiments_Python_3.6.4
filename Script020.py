"""
Lists
list = [item1, item2, item3, item4]
listTwo = [item7, item9, item15, item16]
listthree = [list, listTwo, listThree]
"""

""" 
Name, Lastname, Functional,
Fuel capacity, Fuel usage per hour, Hardware reserve, Hardware usage per hour, Distance per hour, Weapons	Ammunition, Ammunition usage per hour
"""

"""
Fuel capacity	Fuel usage per hour	Hardware reserve	Hardware usage per hour	Distance per hour	Weapons	Ammunition	Ammunition usage per hour
Coordinator	1000000	1	0	0	20	yes	1000	100
Infector	500000	2	1000	10	15	no	0	0
Soldier	500000	2	0	0	20	yes	2000	200
Technician	500000	3	1000	20	15	yes	1000	100
Scout	1000000	2	0	0	30	yes	1000	100
Construction worker	500000	3	1500	40	10	no	0	0
Newcomer	0	0	0	0	0	no	0	0
"""


bobSmith = ['Bob', 'Smith', 'Coordinator', 1000000, 1, 0, 0, 20, 'yes', 1000, 100]
marthaSmith = ['Martha', 'Smith', 'Infector', 500000, 2, 1000, 10, 15, 'no', 0, 0]
johnSmith = ['John', 'Smith', 'Soldier', 500000, 2, 0, 0, 20, 'yes', 2000, 200]
smithBrigade = [bobSmith, marthaSmith, johnSmith]
#print(smithBrigade)

robTrump = ['Rob', 'Trump', 'Technician', 500000, 3, 1000, 20, 15, 'yes', 1000,	100]
suziTrump = ['Suzi', 'Trump', 'Scout', 1000000,	2, 0, 0, 30, 'yes', 1000, 100]
hulkTrump = ['Hulk', 'Trump', 'Construction worker', 500000, 3, 1500, 40, 10, 'no', 0, 0]
trumpBrigade = [robTrump, suziTrump, hulkTrump]
#print(trumpBrigade)

print(smithBrigade, trumpBrigade)
