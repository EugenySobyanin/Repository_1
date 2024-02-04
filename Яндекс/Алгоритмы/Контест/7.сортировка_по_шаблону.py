'''Алгоритмы
Тема: Сортировки
Урок: Сортировка вставками
'''

# решение 1
test_arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
pattern1 = [2, 1, 4, 3, 9, 6]

def pattern_sort(arr, pattern):
    
    for i in range(len(pattern)):
        for j in range(len(arr)):
            