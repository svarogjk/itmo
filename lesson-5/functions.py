
#   название функции
def func():
    print('Hello World from func!')


# Запуск функции
func() # - всегда запуск!!!
# func()
# func()
# func()


# (1, 2, 3) - это  кортеж, а не запуск функции

import datetime

f = open('log.txt', 'w')

def log_time():
    now = datetime.datetime.now()
    f.write(str(now)+'\n')

log_time()
log_time()


