# "Потоки гостей в кафе"
from queue import Queue
from random import randint
from threading import Thread
from time import sleep


class Table:
    number = int()
    guest = str()

    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):
    name = str()

    def __init__(self, name):
        self.name = name
        name=None
        super().__init__(name)

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    queue = Queue()
    tables = []

    def guest_arrival(self, *guests):
        pass

    def discuss_guests(self):
        pass


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
