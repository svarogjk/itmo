
# Генератор списка

names = ['Василий', 'Маша', 'Гера']

#       преобразование  - цикл for
lst = [ len(a) for a in names if len(a) > 4 ]

print( lst )
