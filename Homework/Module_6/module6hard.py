# "Они все так похожи"
from math import pi, sqrt


class Figure:
    sides_count = 0
    filled = False

    def __init__(self, __color=(), *__sides):
        self.__color = __color
        self.__sides = __sides
        if all(isinstance(side, int) for side in __sides):
            if self.sides_count != len(__sides) and len(__sides) > 1:
                self.__sides = [1] * self.sides_count
            elif self.sides_count != len(__sides) and len(__sides) == 1:
                self.__sides = list(__sides) * self.sides_count
            elif self.sides_count == len(__sides):
                self.__sides = list(__sides)

    def __is_valid_color(self, r, g, b):
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            if (r in range(0, 256)
                    and g in range(0, 256)
                    and b in range(0, 256)):
                return True
        return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = r, g, b

    def get_color(self):
        return list(self.__color)

    def __is_valid_sides(self, *new_sides):
        if self.sides_count == len(new_sides) and all(isinstance(side, int) and side > 0 for side in new_sides):
            return True
        else:
            return False

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        else:
            self.__sides = self.__sides

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1
    __radius = int()

    def __init__(self, color, *__sides):
        super().__init__(color, *__sides)
        self.__radius = __sides[0] / (2 * pi)

    def get_square(self):
        return pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *__sides):
        super().__init__(color, *__sides)
        if (self.get_sides()[0] + self.get_sides()[1] > self.get_sides()[2] and
                self.get_sides()[1] + self.get_sides()[2] > self.get_sides()[0] and
                self.get_sides()[2] + self.get_sides()[0] > self.get_sides()[1]):
            self.square = self.get_square()
        else:
            self.set_sides(1, 1, 1)

    def get_square(self):
        p = self.__len__() / 2
        return (sqrt(p * (p - self.get_sides()[0]) *
                         (p - self.get_sides()[1]) *
                         (p - self.get_sides()[2])))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *__sides):
        __sides = [__sides[0]] * self.sides_count
        super().__init__(color, *__sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((222, 35, 130), 6, 10)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))
#
# Проверка объёма (куба):
print(cube1.get_volume())
