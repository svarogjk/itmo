
lst = [1, -17, 233]


lst = sorted(lst, reverse=True)


print(lst)

print(
    sorted(
        ['b', 'arc', 'z'],
        key=lambda i:len(i)
    )
)
