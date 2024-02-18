from random import randint


def counting_sort(arr: list, maximum: int) -> list:
    # Создаем массив для подсчета всех значений
    count = [0] * (maximum + 1)

    for item in arr:
        # Для каждого значения массива array увеличиваем счётчик 
        # в соответствующей ячейке массива count.
        # Например, увидели в array значение 2 - добавляем единицу к значению count[2].
        count[item] += 1

    sorted_arr = []

    for item in range(maximum + 1):
        # Добавляем в sorted_array уникальный элемент столько раз, 
        # сколько он встретился в исходном массиве.
        sorted_arr += [item] * count[item]

    return sorted_arr


test_arr = [randint(0, 30) for el in range(1, 50)]
result = counting_sort(test_arr, 30)
print(result)