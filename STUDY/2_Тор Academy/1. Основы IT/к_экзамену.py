from random import randint
'''Задание 1
Мин и макс.значение в списке
'''
numbers = [None] * 10
numbers = [randint(0, 100) for el in numbers]

minimal = numbers[0]
maximum = numbers[0]

for el in numbers:
    if el < minimal:
        minimal = el
    if el > maximum:
        maximum = el

print(numbers)
print(f'Минималный {minimal} \n'
      f'Максимальный {maximum}')


'''Задание 2
Все делители натурального числа
'''
def all_deviders(number):
    
    result_list = []
    
    for el in range(1, number + 1):
        
        if number % el == 0:
            result_list.append(el)
            
    return result_list

print(all_deviders(100))

'''Задание 3
Проверк на полиндром
'''

def is_polindrom(word):
    
    word = word.lower()
    left = 0
    right = len(word) - 1
    
    while left < right:
        
        if word[left] != word[right]:
            return False
        
        left += 1
        right -= 1
        
    return True

print(is_polindrom('Шалашик'))


'''Задание 4
Проверка натурального числа на простоту
'''

def is_natural_number(number):
    
    for i in range(1, number):
        
        if number % i == 0:
            
            return False
        
    return True

print(is_natural_number(3))
        