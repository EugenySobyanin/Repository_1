mask = [5, 7, 2, 3]
test = [9, 8, 7, 6, 5, 4, 3, 2, 1]

def foo(item):
    return mask[item]

print(sorted(test, key=foo))