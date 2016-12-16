def train(count):
    for i in range(count):
        if i == 0:
            yield 'Тепловоз'
        else:
            yield 'Вагон ' + str(i)

for a in train(10):
    print(a)


def train(count):
    yield 'Тепловоз'
    for i in range(1, count+1):
        yield 'Вагон ' + str(i)