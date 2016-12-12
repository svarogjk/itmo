
# JSON (javascript)
import json

lst = [1, 2, 3, 'Олеся', {17: 12}, (1, 2, 34), list({1, 2, 3}), None]

filename = 'lst.json'

# Запись в JSON файл
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(lst, f, ensure_ascii=False)

# Чтение
with open(filename) as f:
    lst2 = json.load(f)

    print(lst2)
