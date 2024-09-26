# "За честь и отвагу!"
from threading import Thread, Lock
from time import sleep

lock = Lock()


class Knight(Thread):
    name = str()
    power = int()

    def __init__(self, name, power):
        self.name = name
        self.power = power
        super().__init__()

    def run(self):
        num_of_enemies = 100
        day_of_battle = 0
        print(f'{self.name}, на нас напали!')
        while num_of_enemies:
            sleep(1)
            day_of_battle += 1
            num_of_enemies = num_of_enemies - self.power
            with lock:
                print(f'{self.name}, сражается {day_of_battle} день(дня)..., осталось {num_of_enemies} воинов.')
                if num_of_enemies == 0:
                    print(f'{self.name} одержал победу спустя {day_of_battle} дней(дня)!')
                    break


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print('Все битвы закончились!')
