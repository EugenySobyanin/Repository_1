'''Это довольно просто. Ваша цель - создать функцию,
которая удаляет первый и последний символы строки. 
Вам предоставляется один параметр, исходная строка. 
Вам не нужно беспокоиться о строках, содержащих менее двух символов.
'''

test_1 = 'Hello, world'
test_2 = 'ooopsss'

# решение 1 (не проходит тесты где повторяются первые или последние символы)
def remove_char(s):
    s = s.strip(s[0])
    s = s.strip(s[-1])
    return s

#print(remove_char(test_2))



# решение 2 
def remove_char2(s):
    s = list(s)
    s.pop()
    s.pop(0)
    return ''.join(s)

print(remove_char2(test_1))


# решение 2 в одну строку




# решение 3 (самое простое со срезом)

def remove_char3(s):
    return s[1:-1]

print(remove_char3(test_1))