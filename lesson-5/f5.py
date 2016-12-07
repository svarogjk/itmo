# coding: utf-8

def sum(a, b, count=0, *args):
    i = 0

    for a in args: # перечисляем элементы списка args
        i += a

    return i


print( sum(1, 2, 1, 3, 4, 5, 6, 7) )

# print(13, 543, 546, end='!!!\n')
# print(13, 543, 546, end='!!!\n')


