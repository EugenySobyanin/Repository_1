
def sumStr(a, b):
    result = ''
    a2= a
    b2 = b
    
    for i in range(min(len(a), len(b))):
        result += a[i]
        a2 = a2[1:]
        result += b[i]
        b2 = b2[1:]

    if (a2 == ''):
        reminder = b2
    else:
        reminder = a2

    return result + reminder


test1 = 'abcd'
test2 = 'defxerox'


print(sumStr(test1, test2))
