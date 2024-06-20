'''Алгоритмы
Тема: Сортировки
Урок: Сортировка вставками
'''

import sys

# решение 1
test_arr1 = [8, 4, 9, 3, 10, 3, 3,]
pattern1 = [8]

def pattern_sort(arr, pattern):
    
    indx_mask = 0
    indx_sort = 0
    
    for pat in range(len(pattern)):
        for ar in range(len(arr)):
            
            #надо проверить эту часть кода ........................
            if arr[ar] == pattern[pat]:
                temp = arr[ar]
                arr[ar] = pattern[indx_mask]
                arr[indx_mask] = temp
                indx_mask += 1
                
    
    for el in range(indx_mask + 1, len(arr)):
        
        current = arr[el]
        prev = el -1
        
        while prev >= indx_mask - 2 and arr[prev] > current:
            arr[prev + 1] = arr[prev]
            prev -= 1
            
        arr[prev + 1] = current

pattern_sort(test_arr1, pattern1)

print(test_arr1)
                
# if __name__ == '__main__':
    
#     len_arr = int(sys.stdin.readline().rstrip())
#     #arr1 = [int(sys.stdin.readline().rstrip()) for el in range(len_arr)]
#     arr1 = sys.stdin.readline().rstrip().split()
#     arr1 = [int(el) for el in arr1] 
    
#     len_mask = int(sys.stdin.readline().rstrip())
#     #mask1 = [int(sys.stdin.readline().rstrip()) for el in range(len_mask)]
#     mask1 = sys.stdin.readline().rstrip().split()
#     mask1 = [int(el) for el in mask1]
    
#     pattern_sort(arr1, mask1)
#     print(' '.join([str(el) for el in arr1]))
        
 
 
            
            
            