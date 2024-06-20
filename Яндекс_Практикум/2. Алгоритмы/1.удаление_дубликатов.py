#///////////// черновое решение
# numbers = [1, 1, 1, 2, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 8, 9]
# result_nums = []
# doubles = []

# for el in numbers:
#     if el not in result_nums:
#         result_nums.append(el)
#     else:
#         doubles.append('_')

# result_nums.extend(doubles)

# print(result_nums)
        


#//////////////// основное решение 1
# import sys 

# el_count = int(sys.stdin.readline().rstrip())
# numbers = []


# def foo():
#     double = []
#     for i in range(el_count):
#         num = sys.stdin.readline().rstrip()
#         if num not in numbers:
#             numbers.append(num)
#         else:
#             double.append('_')
#     numbers.extend(double)
#     print(' '.join(numbers))

# foo()




#/////////////////// вариант решения 2
# import sys

# def foo():
#     el_count = int(sys.stdin.readline().rstrip())
#     numbers = []
#     double = []
#     for i in range(el_count):
#         num = sys.stdin.readline().rstrip()
#         if num not in numbers:
#             numbers.append(num)
#         else:
#             double.append('_')
#     numbers.extend(double)
#     print(' '.join(numbers))

# if __name__ == '__main__':
#     foo()




#/////////////////// вариант решения 3
import sys


def foo():
    el_count = int(sys.stdin.readline().rstrip())
    nums = sys.stdin.readline().rstrip().split()
    double = []
    result = []
    for i in nums:
        if i not in result:
            result.append(i)
        else:
            double.append('_')
    result.extend(double)
    print(' '.join(result))

    
if __name__ == '__main__':
    foo()


