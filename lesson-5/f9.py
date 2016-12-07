

def func(*args, **kwargs):
    print('args:', args)
    print('kwargs:', kwargs)

    # СОВЕТ - не надо так!!
    if 'key' in kwargs:
        print('key:', kwargs['key'])


func(key=123, b=17, c=12, g=10) # запуск с именованным аргументом





