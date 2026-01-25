"""Механизм инкапсуляции
Одно Подчеркивание только сигнализирует программисту
Два подчеркивания реально ограничевает доступ из вне
protected _x(одно нижнее подчеркивание) - доступ везде
private __x (два подчеркивания) - доступ только внутри класса
"""


class Point:
    def __init__(self, x=0, y=0):
        self._x = self.__y = 0
        if self.__check_coords(x) and self.__check_coords(y):
            self._x = x
            self.__y = y

    # private метод
    @classmethod
    def __check_coords(cls, x):
        """Метод проверяет переданный тип данных"""
        return type(x) in (int, float)


pt = Point("4", 2)
print(pt._x)

try:
    print(pt.__y)
except AttributeError:
    print("Нет доступа из вне")

pt = Point(33, 44)

# Нюанс! можно обратиться к private атрибутам!
# кодовые имена можно посмотреть с помощью ф.ции dir()
print(dir(pt))
# а теперь...
print(pt._Point__y)
# c помощью модуля accessify можно дополнительно защитить методы
# с помощью декораторов
