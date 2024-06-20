# ID посылки 105910221

import sys


def calculate_robots() -> int:

    robots: list = sys.stdin.readline().rstrip().split()
    robots = [int(el) for el in robots]
    limit: float = float(sys.stdin.readline().rstrip())
    result: int = 0
    left_indx: int = 0
    right_indx: int = len(robots) - 1
    robots.sort()

    while left_indx <= right_indx:

        if robots[right_indx] == limit:
            result += 1
            right_indx -= 1

        elif robots[right_indx] + robots[left_indx] > limit:
            result += 1
            right_indx -= 1

        elif robots[right_indx] + robots[left_indx] <= limit:
            result += 1
            left_indx += 1
            right_indx -= 1

    return result


print(calculate_robots())
