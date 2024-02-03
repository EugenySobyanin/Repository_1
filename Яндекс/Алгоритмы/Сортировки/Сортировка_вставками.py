def insertion_sort(arr):
    for i in range(1, len(arr) - 1):

        # текущий элемент
        current = arr[i]
        # предыдущий индекс
        prev = i - 1

        # сравниваем current c предыдущим элементом
        # и двигаес предыдущий элемент на одну позицию вправо,
        # пока он больше current и не достигнуто начало массива
        while prev >= 0 and arr[prev] > current:
            arr[prev + 1] = arr[prev]
            prev -= 1
        # Вставляем current в отсортированную часть массива на нужное место.
        arr[prev + 1] = current
        print(f'Шаг {i}, отсортировано элементов: {i + 1}, {arr}')


insertion_sort([2, 9, 11, 7, 1])
