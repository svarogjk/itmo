
users = [
    ['Юля', 20, True],
    ['Степа', 25, False],
    ['Иван', 20, False],
    ['Володя', 20, True],
]

def active_users(users):
    for name, age, active in users:
        if active:
            yield name, age

# выдача конкретно активных польователей
for name, age in active_users(users):
    print(name, age)
