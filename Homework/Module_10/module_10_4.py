# "Потоки гостей в кафе"
from threading import Thread
from time import sleep
from queue import Queue
from random import randint


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, tables):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            unfree_table = True
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest.name
                    print(f'{table.guest} сел(-а) за стол номер {table.number}')
                    unfree_table = False
                    table.guest = Guest(table.guest)
                    table.guest.start()
                    break
            if unfree_table:
                self.queue.put(guest)
                print(f'{guest.name} в очереди.')

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                if not self.queue.empty() and table.guest is None:
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    table.guest.start()


# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()
