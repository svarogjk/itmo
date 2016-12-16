users = [
    'Юля',
    'Степа',
    'Иван',
    'Володя',
    'Ванадий',
    'Иван Иванович',
]


def gen(in_gen, filter, count):
    i = 0
    for a in in_gen:
        if filter in a.lower():
            yield a # висит здесь
            i += 1
            if i == count:
                return

for a in gen(users, filter='ван', count=2):
    print(a)

