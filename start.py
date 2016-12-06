

print("Hello World!")

# Ветвления

x = 12
y = 'cat'
if x > 10:
    pass
elif x == 10:
    if y == 'dog':
        print('dog == 10')
else:
    print('x < 10')

# Циклы

x = 3
while x > 10:
    x += 1
    print(x)

for a in [1, 2, 3, 4]:
    pass




# -------------------------------------------

int
float
str
list # [1, 2, 3, 2]
tuple # кортеж (1, 2, 3)
dict
{'hello': 'World!'}

bool # True, False
set # {1, 2, 3} куча

if 3 in {2, 3, 4}:
    pass

frozenset
None # ничего

# long #? python2 длинный int

f = open('some_file', 'w')
print( dir(f) )

f.write('Hello World!\n')
f.close()