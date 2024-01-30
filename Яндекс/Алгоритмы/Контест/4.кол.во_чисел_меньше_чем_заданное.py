# Решение 1 (наивное решение)
import sys



def check_numbers():
    
    numbers = sys.stdin.readline().rstrip().split()
    numbers = [int(el) for el in numbers]
    result = []
    
    for i in numbers:
        counter = 0
        for j in numbers:
            if i > j:
               counter += 1
        result.append(str(counter))
    return ' '.join(result)

print(check_numbers())