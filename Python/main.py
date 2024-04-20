<<<<<<< HEAD
from jinja2 import Template
=======
class Bird:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    
    def describe(self, full=False):
        return f'Размер птицы {self.name} — {self.size}.'
    

class Parrot(Bird):
    def __init__(self, name, size,color):
        super().__init__(name, size)
        self.color = color

    def describe(self, full=False):
        if full:
            return (f'Попугай {self.name} — заметная птица, окрас её перьев — {self.color}, '
                    f'а размер — {self.size}. Интересный факт: попугаи чувствуют ритм, '
                    f'а вовсе не бездумно двигаются под музыку. Если сменить композицию, '
                    f'то и темп движений птицы изменится.')
        else: 
            return super().describe(full)

    

class Penguin(Bird):
    def __init__(self, name, size,genus):
        super().__init__(name, size)
        self.genus = genus
    
    def describe(self, full=False):
        if full:
            return (f'Размер пингвина {self.name} из рода {self.genus} — {self.size}. '
                    f'Интересный факт: '
                    f'однажды группа геологов-разведчиков похитила пингвинье яйцо, '
                    f'и их принялась преследовать вся стая, не пытаясь, впрочем, при этом нападать. '
                    f'Посовещавшись, похитители вернули птицам яйцо, и те отстали.')
        else:
            return super().describe(full)

kesha = Parrot('Ара', 'средний', 'красный')
kowalski = Penguin('Королевский', 'большой', 'Aptenodytes')

print(kesha.describe())
print(kowalski.describe(True))
>>>>>>> c9c9338ac2bf5aebad9bfbcd614b159f86afd298
