# Counting operations of deviding
# / usual deviding
# a = 10
# b = 3
# c = a/b
# print(c)

# // deviding with integer output of no rest
# d = 20
# e = 3
# f = d//e
# print(f)

# % deviding with real output with no rest
# cg = 14
# h = 3
# i = g%h
# print(i)

# socks

priceSocks = 3
moneyOnSocks = 50
pairsBought = moneyOnSocks // priceSocks
print(pairsBought)
socksMoneyRest = moneyOnSocks % priceSocks
print(socksMoneyRest)

# t-shirts

priceTshirts = 7
moneyOnTshirts = 50
tshirtsBought = moneyOnTshirts // priceTshirts
print(tshirtsBought)
tshirtsMoneyRest = moneyOnTshirts % priceTshirts
print(tshirtsMoneyRest)

# shirts

priceShirts = 12
moneyOnShirts = 50
shirtsBought = moneyOnShirts // priceShirts
print(shirtsBought)
shirtsMoneyRest = moneyOnShirts % priceShirts
print(shirtsMoneyRest)

restTotal = socksMoneyRest + tshirtsMoneyRest + shirtsMoneyRest
print(restTotal)
