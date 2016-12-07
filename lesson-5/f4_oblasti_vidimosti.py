
# Области видимости

# в глобальной области
COUNT = 0

def func(a):
    global COUNT # взять из глоб области для изменения

    # в локальной области
    loc_perem = 12 + COUNT
    COUNT = 100 # всегда создание локальной переменной

    return a + loc_perem


result = func(10)
print(result)
#print(loc_perem)

print('COUNT:', COUNT)


