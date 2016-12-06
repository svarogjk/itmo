
lst = [
    ['Юля', 20],
    ['Степа', 25],
    ['Иван', 20],
    ['Иван', 20],
]

# Вариант 1

# print( len(lst) )
#
# for i in range(0, len(lst), 2):
#
#     print("Имя: " + lst[i][0] + " Возраст: " + str(lst[i][1]))

# Вариант 2

# i = 0
# for name, age in lst:
#     if i % 2 == 0:
#         print("Имя:", name, "Возраст:", age)
#     i += 1

for i, item in enumerate(lst):
    if i % 2 == 0:
        print("Имя:", item[0], "Возраст:", item[1])

for i, (name, age) in enumerate(lst):
    if i % 2 == 0:
        print("Имя:", name, "Возраст:", age)


# Со словарем:

# d = {
#     'Юля': 20,
#     'Степа': 25,
#     'Иван': 20,
#     'Иван': 20,
# }
#
# i = 0
# for key in d:
#     if i % 2 == 0:
#         print(key, d[key])
#     i += 1

