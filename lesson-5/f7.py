"""
Строка документирования

"""

def func():
    x = 5
    print( locals() ) # выдает словарь с локальными переменными

func()

# выдает все глобальные переменные
print('globals:', globals())
print( 'DOC:', __doc__ )
print( 'DOC:', __name__ )

# builtins: print, sum, len, ...
