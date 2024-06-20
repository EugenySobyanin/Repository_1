'''Проверяем правильная ли скобочная последовательность
'''

#наивное решение 1 ///// решение не проходит все тесты, непрвальная логика работ
# import sys


# def is_correct_bracket_seq():
#     staples = sys.stdin.readline().rstrip()
#     staples = [el for el in staples]
    
#     indx_left = 0
#     indx_right = len(staples) - 1
    
#     if len(staples) % 2 != 0:
#         return False
    
#     for i in range(len(staples)):
#         if staples[i] == staples[indx_right]:
#             return False
#         else:
#             indx_right -= 1
        
#     for i in range(len(staples)):
#         if staples[i] == '}':
#             staples[i] = '{'
#         elif staples[i] == ']':
#             staples[i] = '['
#         elif staples[i] == ')':
#             staples[i] = '('
            
#     indx_left = 0
#     indx_right = len(staples) - 1
            
#     while True:
#         if indx_left > indx_right:
#             return True
#         if staples[indx_left] != staples[indx_right]:
#             return False
#         else:
#             indx_left += 1
#             indx_right -= 1


# навивное решение № 2 (не проходит все тесты, непраильная логика, надо решать через стек)
# import sys


# def is_correct_bracket_seq():
    
    
#     staples = sys.stdin.readline().rstrip()
    
#     flag_open = True
#     flag_close = False
#     for el in staples:
#         if el == '(' or el == '[' or el == '{':
#             flag_open = True
#             flag_close = False
#         if el == ')' or el == ']' or el == '}' and flag_open == False:
#             return False
        
    
#     a = staples.count('(')
#     b = staples.count(')')
#     c = staples.count('[')
#     d = staples.count(']')
#     e = staples.count('{')
#     f = staples.count('}')
    
#     if a != b or c != d or e != f:
#         return False
#     else:
#         return True
        
        

# if __name__ == '__main__':
#     print(is_correct_bracket_seq())


#наивное решение 3 (через стек)   //////// это решение сработало
import sys


class Stack():
    
    
    def __init__(self) -> None:
        self.__items = []        #приватныый атрибут
        
        
    def push(self, item):        #добавить элемент в стек
        self.__items.append(item)
    
        
    def pop(self):               #изъятие последнего элемента из стека
        return self.__items.pop()
    
    
    def size(self):
        return len(self.__items) #вернуть размер стека
    
    
    def peek(self):
        return self.__items[-1]
    

    
def is_correct_bracket_seq():
    
    
    staples = sys.stdin.readline().rstrip()
    staples_stack = Stack()
    
    for el in staples:
        
        if el == '(' or el == '[' or el == '{':
            staples_stack.push(el)
            
        else:
            
            if staples_stack.size() == 0:
                return print(False)
            
            if el == ')':
                if staples_stack.peek() == '(':
                    staples_stack.pop()
                    
                else:
                    return print(False)
                
            elif el == ']':
                if staples_stack.peek() == '[':
                    staples_stack.pop()
                    
                else:
                    return print(False)
            
            elif el == '}':
                if staples_stack.peek() == '{':
                    staples_stack.pop()
                    
                else:
                    return print(False)          
            
    print(staples_stack.size() == 0)


if __name__ == '__main__':
    is_correct_bracket_seq()

            
    

    
    
    