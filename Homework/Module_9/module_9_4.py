# "Функциональное разнообразие"
from random import choice
"""
Lambda-функция
Список совпадения букв в той же позиции first & second
Вывод на консоль:
[False, True, True, False, False, False, False, False, True, False, False, False, False, False]
"""

first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x, y: x == y, first, second)))

"""
Замыкание
"""


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='UTF8') as file:
            for item in data_set:
                file.write(str(item) + '\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

"""
Метод __call__:
"""


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
