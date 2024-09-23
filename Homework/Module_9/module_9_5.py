# "Range - это просто"
class StepValueError(ValueError):
    pass


class Iterator:
    start = int()  # целое число с которого начинается итерация
    stop = int()  # целое число на котором заканчивается итерация
    step = int()  # шаг с которой совершается итерация
    pointer = int()  # указывает на текущее число в итерации (изначально start)

    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        if step == 0:
            raise StepValueError()

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        pointer = self.pointer
        if self.step > 0 and self.pointer > self.stop:
            raise StopIteration
        elif self.step < 0 and self.pointer < self.stop:
            raise StopIteration
        else:
            self.pointer += self.step
        return pointer


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()

'''
Вывод на консоль:
Шаг указан неверно
-5 -4 -3 -2 -1 0 1
6 8 10 12 14
5 4 3 2 1
'''
