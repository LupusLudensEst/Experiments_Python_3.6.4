# def function_name(argument):

# def=define/declare

#  pass-operator of emthy function/statement
# def function_name(argument):
#    pass

def butterbrott(bread_loaves, butter_gramms, cheese_gramms, sausage_gramms):
    bread = (bread_loaves * 15) // 2
    butter = butter_gramms // 5
    cheese = cheese_gramms // 10
    sausage = sausage_gramms // 10
    amount = min(bread, butter, cheese, sausage)
    return amount
print("You will get: ", butterbrott(10, 500, 1000, 1500), "pieces.")
