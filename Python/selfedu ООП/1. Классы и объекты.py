class Point():
    color = 'black'
    circle = 10


# print(Point.color, Point.circle)

a = Point()
# print(a)
# print(a.color, a.circle)


"""методы setattr, getattr, hasattr"""
"""setattr() - можно динамически добавлять атрибуты и менять их значения"""
setattr(a, 'x', 100500)  # добалвен новый атрибут
setattr(a, 'color', 'red')
# print(a.x, a.color)

"""getattr() (если нет поля в простронстве имен
- вызывается ошибка, если не указать 3ий аргумент False)"""
# print(getattr(a, 'x'))
# print(getattr(a, 'y', False))

# hasattr() - булевый метод
# print(hasattr(a, 'x'))
# print(hasattr(Point, 'x'))


# коллекция __dict__ (можно применять к классам и объектам)
# print(a.__dict__)


"""удаление атрибутов
c помощью оператора del
- вызывает ошибку если атрибута нет в классе или объекте"""
del a.x
d = a.__dict__
print(d)
"""c помощь delattr - применяется тольк к текущему пространству имен
(для которого вызывается)"""
delattr(a, 'color')
d = a.__dict__
print(d)
