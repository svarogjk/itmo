from datetime import datetime

def logger():
    with open('log.log', 'a') as f:
        while True:
            text = yield
            f.write(str(datetime.now()) + ': ' + text + '\n')



l = logger()
next(l) # обязательно (печалька)...

l.send('Hello!')
l.send('Buy!')


# * задействовать генераторы для поиска файлов