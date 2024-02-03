test_1 = 'world'
test_2 = 'hello'
test_3 = 'h'

# решение 1
def reverse_string(string):
    return string[::-1]

# решение 2
def reverse_string2(string):
    return ''.join([string[el] for el in range(len(string) - 1, - 1, -1)])

# решение 3 


print(reverse_string(test_1))
print(reverse_string(test_2))
print(reverse_string(test_3))

print(reverse_string2(test_1))
print(reverse_string2(test_2))
print(reverse_string2(test_3))


