# Генератор set

# s = { a for a in range(10) }
# print(s)
#
# s = set([ a for a in range(10) ])
# print(s)



# Генераторное выражение (генератор)

def gen():
    return ( a for a in range(3) ) # запоминается порядок действий
print(gen())
print(gen())

# for a in g:
#     print(a)

# g[3] - выдаст ошибку !!!
# for a in g:
#     print(a)

print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())

