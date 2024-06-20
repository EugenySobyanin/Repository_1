# ID посылки 105910221

import sys


def calculate_robots(robots: list[int], limit: int) -> int:
    '''
    Возвращает миниальное количество перевозок роботов.

        Параметры:
                robots (list[int]): вес каждого робота
                limit (int): максимальный вес
                который можно перевезти за один раз

        Возвращаемое значение:
                result (int): минимально количество перевозок
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

    robots1: list = sys.stdin.readline().rstrip().split()
    robots1 = [int(el) for el in robots1]
    limit1: int = int(sys.stdin.readline().rstrip())
    print(calculate_robots(robots1, limit1))
