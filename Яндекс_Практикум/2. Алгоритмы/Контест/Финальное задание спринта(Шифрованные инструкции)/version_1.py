# id посылки 107934539
import sys


def decoding(code: str) -> str:
    '''
    Возвращает расшифрованную строку - последовательность букв.
    '''
    stack: list = [tuple[int, str]]
    current_num: int = 0
    result: str = ''

    for el in code:
        if el.isdigit():
            current_num = current_num * 10 + int(el)
        elif el == '[':
            stack.append((current_num, result))
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
