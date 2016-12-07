
def global_func():
    pass

def func():

    print(1)

    def new_finc():
        pass

    def new_finc_1():
        pass

    new_finc()
    new_finc_1()
    global_func()

    return new_finc


print(func())




