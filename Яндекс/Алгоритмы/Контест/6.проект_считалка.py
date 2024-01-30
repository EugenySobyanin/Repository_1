'''Алгоритмы
Тема: Рекурсия
Урок: Рекурсия или цикл
'''

'''Задача проект С.Ч.И.Т.А.Л.К.А
Входные данные: количество человек
                количество тактов в считалке
Выходные данные: Вернуть номер участника

'''


'''Наивное решение 1'''

count_peoples_test = 5
takts_test = 2

import sys


def scitolochka(count_peoples, takts):
    
    people_list = [el for el in range(1, count_peoples + 1)]
    
    
    
    
    count = 0
    
    while len(people_list) > 1:
    
        
        for takt in range(takts):
            if takt < len(people_list) - 1 or takt == 0:
                count += 1
            else:
                count = 0
        
        
            if takt == takts - 1:

                people_list.pop(count)
    
    print(people_list )
    return people_list[0]


# if __name__ == '__main__':
#     count_peoples_test2 = int(sys.stdin.readline().rstrip())
#     takts_test2 = int(sys.stdin.readline().rstrip())
    
    # print(scitolochka(count_peoples_test2, takts_test2))
    



print(scitolochka(count_peoples_test, takts_test))

    

        
        
    