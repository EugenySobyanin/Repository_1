def foo(num):
    if num > 0:
        return [el for el in range(num+1) if not (el % 2)]
    return [el for el in range(num, 1)if not (el % 2)]


print(foo(-10))