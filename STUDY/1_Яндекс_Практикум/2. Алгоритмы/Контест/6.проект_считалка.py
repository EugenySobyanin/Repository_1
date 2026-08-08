'''Алгоритмы
Тема: Рекурсия
Урок: Рекурсия или цикл
'''

'''Задача проект С.Ч.И.Т.А.Л.К.А
Входные данные: количество человек
                количество тактов в считалке
Выходные данные: Вернуть номер участника

'''


'''Наивное решение 1 - решешение прошло тесты!!!!!'''

count_peoples_test = 500
takts_test = 500

import sys


def scitolochka(count_peoples, takts):
    
    people_list = [el for el in range(1, count_peoples + 1)]
    count = 0
    
    while len(people_list) > 1:
    
        
        for takt in range(1, takts + 1):

            if takt == takts:
                people_list.pop(count)
                
                if count == len(people_list):
                    count = 0

            elif count < len(people_list) - 1:
                count += 1

            else:
                count = 0
    
    return people_list[0]


# if __name__ == '__main__':
#     count_peoples_test2 = int(sys.stdin.readline().rstrip())
#     takts_test2 = int(sys.stdin.readline().rstrip())
    
#     print(scitolochka(count_peoples_test2, takts_test2))
    



print(scitolochka(count_peoples_test, takts_test))

    

        
        
    