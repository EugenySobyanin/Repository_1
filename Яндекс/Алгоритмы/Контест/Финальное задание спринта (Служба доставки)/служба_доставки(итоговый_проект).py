#Задание служба доставки

# Наивное решение 1 
# на первый взгляд решение работает

# test_1 = [1, 2]
# limit_1 = 3

# test_2 = [3, 2, 2, 1]
# limit_2 = 3

# test_3 = [3, 5, 3, 4]
# limit_3 = 5


# def foo(robots, limit):

#     robots.sort()

#     result = 0
#     left = 0
#     right = len(robots) - 1

#     while left <= right:

#         if robots[right] == limit:
#             result += 1
#             right -= 1

#         elif robots[right] + robots[left] > limit:
#             result += 1
#             right -=1 

#         elif robots[right] + robots[left] <= limit:
#             result += 1
#             left += 1
#             right -= 1


#     return result

        
# print(foo(test_3, limit_3))





# Переписываем наивное решение 1 под проверку на контесте(без аннотации)
import sys


def calculate_robots():

    robots = sys.stdin.readline().rstrip().split()
    robots = [int(el) for el in robots]
    limit = int(sys.stdin.readline().rstrip())
    result = 0
    left_indx = 0
    right_indx = len(robots) - 1
    robots.sort()

    while left_indx <= right_indx:

        if robots[right_indx] == limit:
            result += 1
            right_indx -= 1

        elif robots[right_indx] + robots[left_indx] > limit:
            result += 1
            right_indx -=1 

        elif robots[right_indx] + robots[left_indx] <= limit:
            result += 1
            left_indx += 1
            right_indx -= 1

    return result


print(calculate_robots())