"""Испоьзуются декораторы:
@classmethod - имеет доступ к атрибутам класса,
            но не имеет доступ к атрибутам экземпляра
@staticmethod - не имеет доступа не к атрибутам класса
            не к атрибутам экземпляра
"""


class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        """Метод класса можно вызывать через сам класс
        Не может обращаться к атрибутам экземпляра
        т.к нет параметра self"""
        print("Сработал метод validate")
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y) -> None:
        self.x = self.y = 0
        # Вместо self можно было указать имя класса
        if self.validate(x) and Vector.validate(y):
            self.x = x
            self.y = y

    def get_coord(self):
        return self.x, self.y

    @staticmethod
    def norm2(x, y):
        print('Сработал статический метод norm2')
        return x * x + y * y


v = Vector(1, 2)
print(Vector.validate(5))
print(Vector.norm2(4, 5))
res = v.get_coord()
print(res)
