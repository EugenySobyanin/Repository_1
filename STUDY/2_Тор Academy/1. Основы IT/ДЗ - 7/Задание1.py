'''Найти сумму всех четных элементов рада Фибоначи
не превышающих 4млн.
'''


def sum_even_fibonaci(limit=4_000_000):

    num1 = num2 = 1
    result = 0

    while True:

        num1, num2 = num2, num1 + num2

        if not num2 % 2:
            result += num2

        if num1 + num2 > limit:
            break

    return result


print(sum_even_fibonaci())






















'''c Решение 2 (через цикл for)'''

# def fibonacci_barometr_2(generation: int) -> int:
#     num1 = num2 = 1
    
#     for i in range(2, generation):
#         num1, num2 = num2, num1 + num2
#         print(num2, end = " ")
    
# fibonacci_barometr_2(6)