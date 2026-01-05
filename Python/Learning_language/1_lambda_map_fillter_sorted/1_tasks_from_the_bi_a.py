# Задачи
# 1 Квадрат чисел:
# Напиши лямбда-функцию, которая принимает список чисел и возвращает новый список, содержащий квадраты этих чисел.

# 2 Четные числа:
# Напиши лямбда-функцию, которая принимает список чисел и возвращает новый список, содержащий только четные числа.

# 3 Сортировка по длине:
# Напиши лямбда-функцию, которая принимает список строк и сортирует его по длине строк.

# 4 Фильтрация по первой букве:
# Напиши лямбда-функцию, которая принимает список строк и возвращает новый список, содержащий только те строки, которые начинаются с буквы 'A'.

# 5 Сумма значений:
# Используй лямбда-функцию в сочетании с reduce из модуля functools, чтобы вычислить сумму всех чисел в списке.

# 6 Генерация пар:
# Напиши лямбда-функцию, которая принимает два списка (например, чисел и строк) и возвращает новый список, где элементы объединены в пары (число, строка).

from functools import reduce


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
strings = ["apple", "banana", "avocado", "grape", "orange", "kiwi"]


# Задача № 1
square = list(map(lambda x: x**2, numbers))
print(square)

# Задача № 2
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)

# Задача № 3
len_sort = sorted(strings, key=len)
print(len_sort)

# Задача № 4
first_letter_filter = list(filter(lambda x: x[0].upper() == 'A', strings))
print(first_letter_filter)

# Задача № 5
sum_with_reduce = reduce(lambda x, y: x + y, numbers)
sum_with_reduce_with_start = reduce(lambda x, y: x * y, list(filter(lambda x: x != 0, [0, 1, 2, 3, 4, 5])), 1) # решение случая с нулем в списке
print(sum_with_reduce)
print(sum_with_reduce_with_start)

# Задача № 6
generation_pairs = list(map(lambda x, y: (x, y), numbers, strings))
print(generation_pairs)
