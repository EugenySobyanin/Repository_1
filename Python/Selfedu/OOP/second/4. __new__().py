# Метод __new__() вызывается перед созданием объекта
# все классы наследуются от объекта object
"""Неполная реализация паттерна sigleton
Singleton - может существовать только один экземпляр класса"""


class Point:
    __instance = None  # ссылка на экземпляр класса

    def __new__(cls, *args, **kwargs):  # cls - указатель на сам класс Point
        """Должен возращать адрес нового созданного объекта"""
        print(f'Вызов __new__ для {cls}')

        """Здесь можно как-то использовать аргументы
        которые были переданы в конструктор"""
        print(args[0])
        print(args[1])
        print(args)

        # Sigleton
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance
        # return super().__new__(cls)

    def __init__(self, x=10, y=20):  # self - указатель на экземпляр класса
        print(f'Вызов __init__ для {self}')
        self.x = x
        self.y = y


a = Point(22, 33)
b = Point(333, 444)
# второй объект не был создан, но атрибуты были переопределены
print(id(a), id(b))
