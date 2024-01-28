# ID посылки 105910221

import sys


def calculate_robots(rodts: list, limit: float) -> int:
    '''Принимает список с данными о весе роботов и максимальный вес,
    который можно перевести за один раз. Сортирует массив,
    проверяет сколько роботов мы можем увезти за раз (2 или 1)
    и возвращает минимальное количество поездок
    за которое можно перевезти всех роботов.
    '''
    result: int = 0
    left_indx: int = 0
    right_indx: int = len(robots) - 1
    sorted_rodots = sorted(robots)

    while left_indx <= right_indx:

        if sorted_rodots[right_indx] + sorted_rodots[left_indx] <= limit:
            left_indx += 1

        result += 1
        right_indx -= 1

    return result


if __name__ == '__main__':

    robots: list = sys.stdin.readline().rstrip().split()
    robots = [int(el) for el in robots]
    limit: float = float(sys.stdin.readline().rstrip())
    print(calculate_robots(robots, limit))
