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
        service_time = randint(3, 10)
        sleep(service_time)


class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()
        self.free_table = []
        self.guests_threads = []

    def guest_arrival(self, *guests):
        for guest in guests:
            unfree_table = True
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest.name
                    self.free_table = table
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    guest_thread = Guest(guest.name)
                    guest_thread.start()
                    self.guests_threads.append(guest_thread)
                    unfree_table = False
                    break
            if unfree_table:
                self.queue.put(guest)
                print(f'{guest.name} в очереди.')

    def discuss_guests(self):
        for guest_thread in self.guests_threads:
            guest_thread.join()
            for table in self.tables:
                if table.guest == guest_thread.name:
                    print(f'{table.guest} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
            if not self.queue.empty():
                next_guest = self.queue.get()
                self.guest_arrival(next_guest)
                sleep(1)


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


