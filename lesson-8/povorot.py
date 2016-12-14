

train_speed = 90

# 1. функция генерирует исключение, если ей на вход дали
# tupik = True

# 2. Запускаем такую функцию и обрабатываем исключение.
# Если исключение, то train_speed = 0


def check_tupik(tupik):
    if tupik == True:
        raise Exception('Ba-bah')

try:
    check_tupik(True)
except Exception:
    train_speed = 0

print('Итого поезд движется со скоростью - {}'.format(
    train_speed))