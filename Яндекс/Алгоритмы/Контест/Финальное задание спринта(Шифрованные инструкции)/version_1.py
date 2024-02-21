# id посылки 107665224
import sys


def decoding(code: str) -> str:
    '''
    Возвращает расшифрованную строку - последовательность букв.
    '''
    stack: list = [tuple(int, str)]
    current_num: int = 0
    current_str: str = ''
    
    for el in code:
        if el.isdigit():
            current_num = current_num * 10 + int(el)
        elif el == '[':
            stack.append((current_num, current_str))
            current_num = 0
            result = ''
        elif el == ']':
            prev_num, prev_str = stack.pop()
            result = prev_str + result * prev_num
        else: 
            result += el
    return result
    
    
if __name__ == '__main__':
    print(decoding(sys.stdin.readline().rstrip()))