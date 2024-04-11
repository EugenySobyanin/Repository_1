from random import randint


def square(foo):
    def wrapper():
        original_result = foo()
        modified = [el**2 for el in original_result]
        return modified
    return wrapper

@square
def make_list(size) -> list:
    result = [randint(0, 10) for i in range(size + 1)]
    return result


nums = make_list(10)
print(nums)