
def range_3():
    for a in range(3):
        yield a

for a in range_3():
    print(a)

# g = gen()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# Список студентов с параметром active = True/False.
# Генератор, выдающий всех активных пользователей (студентов).