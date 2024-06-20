# type()
a = 5
print(type(a))

# ord() - возвращает код символа
print(ord('i'))

# choice - случайный выбор эл.та из списка/кортежа
from random import choice
a = [1, 2, 3, 4, 5]
b = choice(a)
print(b)

# replace() - 1ый арг - эл.т который надо заменить
          # - 2oй арг - эл.т на который заменяем
# например. с помощью этого метода можно убрать пробелы из строки
a = 'я люблю свежую выпечку'
b = a.replace(' ','').capitalize()
print(b)

# permutations() возвращает итерируемый объект со всеми возможными комбинациями элементов заданной последовательности
from itertools import permutations

a = [1, 2, 3]
combs = permutations(a)
for el in combs:
    print(el)
combs = permutations(a)
for i, el in enumerate(combs):
    print(i, el)