
f = open('f3_global.py')

print(f.read(100)) # читаем

print(f.read(100)) # читаем

f.seek(0) # промотать до позиции в файле

print('----')

#print(f.read()) # читаем весь файл

for line in f:
    #print('line:', line.rstrip())
    print('line:', line[:-1])

