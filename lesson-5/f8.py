

factorial_6 = 1 * 2 * 3 * 4 * 5 * 6
#print(factorial_6)

factorial_7 = 1 * 2 * 3 * 4 * 5 * 6 * 7


# Напишите функцию факториала

def fact(a):
    count = 1

    for i in range(1, a+1):
        count *= i

    return count

print( fact(6) )


# Рекурсия

def fact(a):
    if a == 0:
        return 1
    return fact(a-1)

fact(6)


# Есть предел рекурсии - где-то около ~1000






