# просто что бы работало
a = []
for el in range(101):
    a.append(el)


def find_index(numbers, element):
    left = 0
    right = len(numbers) - 1
    while True:
        mid = (left + right) // 2
        if numbers[mid] == element:
            return mid
        elif left == right and element > numbers[mid]:
            return mid + 1
        elif left == right:
            return mid
        elif left > right:
            return mid + 1
        else:
            if element > numbers[mid]:
                left = mid + 1
            else:
                right = mid - 1

    return None


b = [3, 4, 2, 23, 45, 12, 11, 9, 1, 7, 6]
b.sort()
# print(b)
# print(find_index(b, -1))


# ///// на проверку вариант 1 
import sys

def find_element():
    numbers = sys.stdin.readline().rstrip().split()
    numbers = [int(el) for el in numbers]
    element = int(sys.stdin.readline().rstrip())
    left = 0
    right = len(numbers) - 1
    while True:
        mid = (left + right) // 2
        if numbers[mid] == element:
            while numbers[mid] == numbers[mid - 1] and mid != 0: # цикл для обработки повторяющихся значений, чтобы возращалось всегда первое
                mid -= 1
            return mid
        elif left == right and element > numbers[mid]:
            return mid + 1
        elif left == right:
            return mid
        elif left > right:
            return mid + 1
        else:
            if element > numbers[mid]:
                left = mid + 1
            else:
                right = mid - 1

    return None


if __name__ == '__main__':
    print(find_element())
