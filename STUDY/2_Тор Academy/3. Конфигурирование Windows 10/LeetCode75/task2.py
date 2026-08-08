def foo(list):

    list_str = ''.join(list)

    current_group = ''
    result = ''
    count = 0

    for i in range(1, len(list_str)):
        current_group += list_str[i]
        count += 1

        if (list_str[i] != list[i - 1] or i == len(list_str) - 1):
            result += current_group[0]
            result += str(count)
            current_group = ''
            count = 0

    return len(result)
    

test = ['A', 'A', 'B', 'B', 'B', 'B', '']



print(foo(test))


