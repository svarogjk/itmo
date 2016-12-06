
#      0    1   2    3   4
#      -5   -4   -3  -2  -1
lst = [1, -17, 233, 10, 12]

#lst = lst[2 :  : -2]
#print(lst)
#lst = lst[-1]

lst = lst[-3 : -6 : -2]
print(lst)

lst = lst[::-1]
lst = reversed(lst)
