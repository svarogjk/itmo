


# ---- EXCEPTIONS ---- Исключения

#except: # [ ТАК НЕ НАДО !!! ]

# Обработка исключения
# try:
#     open('nhgnhngh')
# except FileNotFoundError as e:
#     print('[ Ошибка ] {} {}'.format(e, 123))
#
# print('Продолжается программа')

try:
    #1 / 0
    f = open('__init__.py')
    #f.write('vbfvbdf')
except FileNotFoundError as e:
    print('FileNotFoundError')
# except ZeroDivisionError:
#     print('ZeroDivisionError')
# except ArithmeticError as e:
#     pass
except (FileNotFoundError, IOError):
    print('FileNotFoundError')
except IOError:
    print('IOError')
else:
    print('!!!') # не было исключения
finally:
    print('finally')


# BaseException
#     Exception
#         ArithmeticError
#             ZeroDivisionError

# try:
#     f = open('zapis.txt', 'w')
#     f.write('vbfvbdf')
#     1 / 0
# finally: # блок кода далее произойдет в любом случае
#     print('Закрываем файл')
#     f.close()

# with open('zapis.txt', 'w') as f:
#     f.write('vbfvbdf')
#     1 / 0

