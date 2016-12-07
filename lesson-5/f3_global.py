# У нас есть 30 столов, 30 стульев, 1 доска.
# Функция принимает на вход название элемента и его кол-во
# Выводит на экран.

ALL_COUNT = 0

def get_object(element, count):
    global ALL_COUNT
    print(element, count)
    ALL_COUNT += count

get_object('столов', 30)
get_object('стульев', 30)
get_object(count=1, element='доска') # именнованные аргументы

print(ALL_COUNT)