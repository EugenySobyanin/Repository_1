class Point():
    color = 'black'
    circle = 112

    # Конструктор
    def __init__(self, x=10, y=20) -> None:
        self.x = x
        self.y = y

    # Деструктор
    def __del__(self):
        print(f'Удален объект {self}')


a = Point(15, 30)
d = a.__dict__
print(d)
