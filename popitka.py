# coding: utf-8

x = 10

f = open('popitka.txt', "w")

if x > 3:
    f.write(str(x) + '\n')

f.write('Привет')

f.close()


# s = """fvfdvfd
#
# vfdvfd
#
# vfdvfd
#
# """