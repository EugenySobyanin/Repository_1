
# Заимствованное решение из интернета

def decoding_str(code: str) -> str:
    stack: list = []
    current_num: int = 0
    current_str: str = ''
    
    for el in code:
        if el.isdigit():
            current_num = current_num * 10 + int(el)
        elif el == '[':
            stack.append((current_num, current_str))
            current_num = 0
            current_str = ''
        elif el == ']':
            prev_num, prev_str = stack.pop()
            current_str = prev_str + current_str * prev_num
        else: 
            current_str += el
    return current_str

test1 = '3[a]2[bc]' # aaabcbc
test2 = '3[a2[c]]' # accaccacc
test3 = '2[abc]3[cd]ef' # abcabccdcdcdef


print(decoding_str(test1))
print(decoding_str(test2))
print(decoding_str(test3))


'''Решение для отправки на контест'''
import sys


def decoding_str(code: str) -> str:
    stack: list = []
    current_num: int = 0
    current_str: str = ''
    
    for el in code:
        if el.isdigit():
            current_num = current_num * 10 + int(el)
        elif el == '[':
            stack.append((current_num, current_str))
            current_num = 0
            current_str = ''
        elif el == ']':
            prev_num, prev_str = stack.pop()
            current_str = prev_str + current_str * prev_num
        else: 
            current_str += el
    return current_str
    
    
if __name__ == '__main__':
    input_str = sys.stdin.readline().rstrip()
    print(decoding_str(input_str))
