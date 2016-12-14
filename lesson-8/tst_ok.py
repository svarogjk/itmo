
# Кстати

import os

if os.path.exists('some_file'): # Существует ли файл
    print('exists')

    # Является ли он файлом?
    if os.path.isfile('some_file'):
        print('really file')

    elif os.path.isdir('some_file'): # директория?
        print('really dir')


    # Узнать размер файла
    os.path.getsize('some_file')


# Написать модуль check_disk.py
# - функция 1 - получает на вход путь к директории,
#         считает размер суммы файлов.
# * в том числе с вложенными поддиректориями
#
# - функция 2 - пробегает по указанной директории,
#         находит все файлы с указанной подстрокой в имени.
# * в самом файле

