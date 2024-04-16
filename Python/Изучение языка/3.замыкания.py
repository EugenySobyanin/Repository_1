
def fib():
    x1 = 0
    x2 = 1
    def get_next_number():
        nonlocal x1, x2
        x3 = x1 + x2
        x1, x2 = x2, x3
        return x3
    return get_next_number


foo = fib()

for i in range(10):
    print(f'Итерация {i}')
    print(foo())