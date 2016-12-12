
# pickle
import pickle

lst = [1, 2, 3, 'Олеся', {17: 12}]

FILENAME = 'lst.pickle'

with open(FILENAME, 'wb') as f: # pickle требует wb !!!
    pickle.dump(lst, f)


f = open(FILENAME, 'rb')
lst2 = pickle.load(f)

print(lst == lst2)


# 1. Создать функцию, добавляющую тепловоз в pickle
# 2. Создать функцию, читающую список тепловозов

