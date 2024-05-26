class Point():
    color = 'black'
    circle = 111

    def set_coords1():
        print('Вызов метода setcoords без self')  # можно вызвать для класса

    def set_coords2(self, x=10, y=20):
        """Создали локальные атрибуты экземпляра класса"""
        print('Вызов метода setcoords c self')  # можно вызвать для экземпляра
        self.x = x
        self.y = y


Point.set_coords1()
a = Point()

# Эквивалентные записи
a.set_coords2()
Point.set_coords2(a)

d = a.__dict__
print(d)
