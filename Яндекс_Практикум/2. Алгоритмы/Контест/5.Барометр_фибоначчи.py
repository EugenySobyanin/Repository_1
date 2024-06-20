'''Алгоритмы
Тема: Рекурсия
Урок: Базовый и рекурсивный случаи
Контест: Барометр Фибоначчи
'''


'''Решение 1 (через цикл while)'''

# def fibonacci_barometer(generation: int) -> int:
#     num1 = 1
#     num2 = 1
#     i = 0
    
#     while i <= generation - 2:
#         num1, num2 = num2, num1 + num2
#         i += 1
        
#     return num2

# print(fibonacci_barometer(10))


'''c Решение 2 (через цикл for)'''

# def fibonacci_barometr_2(generation: int) -> int:
#     num1 = num2 = 1
    
#     for i in range(2, generation):
#         num1, num2 = num2, num1 + num2
#         print(num2, end = " ")
    
# fibonacci_barometr_2(6)


'''Решешние 3 (через рекурсию) (непонятен смысл такого решения)'''

# def fibonacci_barometr_3(generation):
#     if generation in (0, 1):
#         return 1
#     return fibonacci_barometr_3(generation - 1) + fibonacci_barometr_3(generation - 2)

# print(fibonacci_barometr_3(6))


''' Решение на отправку 1 (решение прошло тесты, но смысл непонятен)''' 
import sys


def fibonacci_barometr(generation):
    if generation in (0, 1):
        return 1
    return fibonacci_barometr(generation - 1) + fibonacci_barometr(generation - 2)

if __name__ == '__main__':
    generation_test = int(sys.stdin.readline().rstrip())
    print(fibonacci_barometr(generation_test))

    