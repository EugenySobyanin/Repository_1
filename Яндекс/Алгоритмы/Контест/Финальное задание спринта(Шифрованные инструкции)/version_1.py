# id посылки 107665224
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
