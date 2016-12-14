
# names = ['Иван', 'Петр', 'Василий']
# surnames = ['Иванов', 'Петров', 'Сидоров', 'Михайлов']
#
# people = [a+' '+b for a in names
#               for b in surnames]
#
# print(people)


# numbers = [1, 2, 3, 4, 5]
# gen_numbers = [(a, b, c) for a in numbers
#                    for b in numbers
#                    for c in numbers]
#
# print(gen_numbers)


lst = [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
]

new_lst = [c for a in lst
             for b in a
             for c in b]

print(new_lst)
