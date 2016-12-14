# --- Генераторы данных ---

# === Генераторы данных ===

lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Как соединить в один список?


# lst10 = [a*3 for a in range(10)]
# print(lst10)
#
# string = 'Hello, World!'
# res = [a for a in string if a not in ',!']
# print(res)
# print(''.join(res))

# 'Hello, World!'.replace(',','').replace('!','')

lst = [127, -30, 556, 17, 223, 400]

#x % 2 == 0

dev_2 = [a for a in lst if a % 2 == 0]
print(dev_2)
