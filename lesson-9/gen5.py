# --- Сопрограмма ---

from datetime import datetime

def gen():
    name = yield # требуем значение из-вне


def gen_2():
    while True:
        text = yield
        print(datetime.now(), text)


g = gen_2()
next(g) # ОБЯЗАТЕЛЬНО

g.send('Hello world from soprogramma!')
g.send('Hello 2')