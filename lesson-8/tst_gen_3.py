
# ---- Генератор словаря ----

# d = {
#     'Мария': 133,
#     'имра': 100
# }
#
# new_dict = { a:d[a] for a in d } # d.get(a)


# lst = [1, 2, 3]
# lst_2 = [10, 20, 30]
#
# d = { a:b for a, b in zip(lst, lst_2) }
# print(d)


###############

# d = {1:1, 2:2, 3:3, 3:5}
# d.update({2:7, 10:10})
# print(d)

# zip(<iterator A>, <iterator B>) -> (A1, B1), (A2, B2), ...


students = [
    ['Иван', 'Иванов', 13],
    ['Мария', 'Иванова', 20]
]

new_dict = { a[0]: a[2] for a in students if a[2] > 18 }
print(new_dict)
















