'''Алгоритмы
Тема: Сортировки
Урок: Сортировка вставками
'''

# решение 1
test_arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
pattern1 = [2, 1, 4, 3, 9, 6]

def pattern_sort(arr, pattern):

    for j in range(len(pattern)):

        for i in range(1, len(arr)):
            current = arr[i]
            prev = i - 1

            while prev >= 0 and arr[prev] != pattern[j]:
                arr[prev + 1] = arr[prev]
                prev -= 1
            arr[prev + 1] = current

    return arr

print(pattern_sort(test_arr1, pattern1))
