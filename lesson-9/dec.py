# coding: utf-8

# from decimal import Decimal
#
# result = (Decimal('0.5') + Decimal('0.5')) ** Decimal('2') / Decimal('2')
#
# print(float(result))
#
#
# from decimal import getcontext
#
# print(getcontext().prec) # точность (коли-во знаков до и после запятой)
#
# print(Decimal('0.57874868436'))
#
#
# getcontext().prec = 5 # изменяем точность ВЫЧИСЛЕНИЙ
# print(Decimal('0.57874868436') + Decimal('128.57874868436'))
#print( randint(1, 100) )

from math import log
from random import randint # randint(0, 100)
from decimal import Decimal, getcontext

getcontext().prec = 6

def poezd(count):
    yield ('Паровоз', 1576)
    y = 'Вагон'

    for i in range(1, count+1):
        x = randint(1, 100)
        x = ( Decimal(x) / Decimal(150) )
        yield (y + str(i) + ' вес груза: ' + str(x), x)

summa = 0
for a, ves in poezd(count=10):
    print( a, ves )
    summa += ves

print('summa (ves): {}'.format(summa))








