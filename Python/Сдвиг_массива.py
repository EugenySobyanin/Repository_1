'''сдвиг одномерного массива вправо'''
numbers = [1, 2, 3, 4, 5]
swing = 4
size = len(numbers)

for i in range(swing):
    last_el = numbers[size - 1]
    indx = size - 2
    while indx >= 0:
        numbers[indx + 1] = numbers[indx]
        indx -= 1
    numbers[0] = last_el

# print(numbers)


'''сдвиг двумерного массива вправо'''
numbers = [[1, 2, 3, 4, 5, ], [6, 7, 8, 9, 10]]
swing = 5

for i in range(swing):
    for j in range(len(numbers)):
        size = len(numbers[j]) # size = 5
        last_el = numbers[j][size - 1] 
        indx = size - 2
        while indx >= 0:
            numbers[j][indx + 1] = numbers[j][indx]
            indx -= 1
        numbers[j][0] = last_el


# for el in numbers:
#     for j in el:
#         print(j, end=' ')
#     print()


'''сдвиг  двумерного массива влево'''
numbers = [[1, 2, 3, 4, 5, ], [6, 7, 8, 9, 10]]
swing = 1

for i in range(swing):
    for j in range(len(numbers)):
        size = len(numbers[j])
        first_el = numbers[j][0]
        indx = 1
        while indx <= size - 1:
            numbers[j][indx - 1] = numbers[j][indx]
            indx += 1
        numbers[j][size - 1] = first_el


# for el in numbers:
#     for j in el:
#         print(j, end=' ')
#     print()


'''сдвиг двумерного массива по вертикали вверх'''
numbers = [[1, 2, 3, 4, 5, ], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
swing = 3

#Вывод исходного массива
# for el in numbers:
#     for j in el:
#         print(j, end=' ')
#     print()


for i in range(swing):
    
    size = len(numbers) - 1
    first_el = numbers[0]
    indx = 1
    
    while indx <= size:
        numbers[indx - 1] = numbers[indx]
        indx += 1

    numbers[size] = first_el
    

print('Результат')
for el in numbers:
    for j in el:
        print(j, end=' ')
    print()



'''Сдвиг двумерного массива по вертекали вниз'''

numbers = [[1, 2, 3, 4, 5, ], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
swing = 3

#Вывод исходного массива
print('Исходный массив')
for el in numbers:
    for j in el:
        print(j, end=' ')
    print()

for i in range(swing):

    last_indx = len(numbers) - 1
    last_el = numbers[last_indx]
    indx = last_indx - 1

    while indx >= 0:
        numbers[indx + 1] = numbers[indx]
        indx -= 1

    numbers[0] = last_el


print('Результат')
for el in numbers:
    for j in el:
        print(j, end=' ')
    print()
