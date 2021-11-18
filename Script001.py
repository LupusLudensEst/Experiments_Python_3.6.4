# price1 = 20
# price2 = 19
# print(price1+price2)

# original = "EXAMPLE"
# removed = original.replace("M", "")
# print(original+';\n'+removed)

# нужно удалить каждое третье слово из строки и заменить его предыдущим
# s = 'Here Comes The Sun And I Say It Is Alright'.split()
# for i in range(2, len(s), 3):
#     s[i] = s[i - 1]
# print(' '.join(s)) # 'Here Comes Comes Sun And And Say It It Alright'

# stopwords=['what','who','is','a','at','is','he']
# query='What is hello'
# for word in stopwords:
#     if word in query:
#         query = query.replace(word, '')
#         print(word)

# query = 'What is hello'
# stopwords = ['what', 'who', 'is', 'a', 'at', 'is', 'he']
# querywords = query.split()
# resultwords  = [word for word in querywords if word.lower() not in stopwords]
# result = ' '.join(resultwords)
# print(result)

# import re
# query = 'What is hello? Says Who?'
# stopwords = {'what','who','is','a','at','is','he'}
# resultwords  = [word for word in re.split("\W+",query) if word.lower() not in stopwords]
# print(resultwords)








