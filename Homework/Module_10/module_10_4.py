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
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()
        self.free_table = []
        self.guests_threads = []

    def guest_arrival(self, *guests):
        for guest in guests:
            free_table_ = True
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest.name
                    self.free_table.append(table)
                    guest_thr = Guest(guest)
                    guest_thr.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    free_table_ = False
                    self.guests_threads.append(guest_thr)
                    break
            if free_table_:
                self.queue.put(guest)
                print(f'{guest.name} в очереди.')

    def discuss_guests(self):
        for i in self.guests_threads:
            i.join()
            print(f'{self.free_table[i].guest} покушал(-а) и ушёл(ушла)')
            print(f'Стол номер {self.free_table[i].number} свободен')
            self.free_table[i].guest = None
            if not self.queue.empty() and not i.is_alive():
                next_guest = self.queue.get()
                self.guest_arrival(next_guest)


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



