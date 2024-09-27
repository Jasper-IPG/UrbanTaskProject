# "Банковские операции"
from random import randint
from threading import Thread, Lock
from time import sleep


class Bank:
    balance = int()
    lock = Lock()

    def __init__(self):
        pass

    def deposit(self):
        operation_lim = 100
        while operation_lim:
            i = randint(50, 500)
            self.balance += i
            print(f'Пополнение: {i}. Баланс: {self.balance}.')
            operation_lim -= 1
            sleep(0.001)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

    def take(self):
        operation_lim = 100
        while operation_lim:
            i = randint(50, 500)
            print(f'Запрос на {i}.')
            if i <= self.balance:
                self.balance -= i
                print(f'Снятие: {i}. Баланс: {self.balance}.')
            elif i > self.balance:
                print(f'Запрос отклонён, недостаточно средств.')
                self.lock.acquire()
            operation_lim -= 1
            sleep(0.001)


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
