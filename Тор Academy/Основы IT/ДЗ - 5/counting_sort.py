from random import randint


def counting_sort(arr: list, maximum: int) -> list:
    count = [0] * (maximum + 1)

    for item in arr:
        count[item] += 1

    sorted_arr = []

    for item in range(maximum + 1):
        sorted_arr += [item] * count[item]

    return sorted_arr


test_arr = [randint(0, 30) for el in range(1, 50)]
result = counting_sort(test_arr, 30)
print(result)