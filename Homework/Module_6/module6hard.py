# "Они все так похожи"
class Figure:
    sides_count = 0
    filled = False

    def __init__(self, __color=(), __sides=int()):
        self.__color = __color
        self.__sides = __sides

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = r, g, b

    def __is_valid_color(self, r, g, b):
        if (r in range(0, 256)
                and g in range(0, 256)
                and b in range(0, 256)):
            return True
        return False

    def get_color(self):
        return list(self.__color)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        else:
            self.__sides = [self.__sides]

    def __is_valid_sides(self, *new_sides):
        if self.sides_count == len(new_sides) and all(i > 0 for i in new_sides):
            return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        pass


class Circle(Figure):
    sides_count = 1
    __radius = int()

    def get_square(self):
        pass


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        pass


class Cube(Figure):
    sides_count = 12


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

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
# print(len(circle1))
#
# # Проверка объёма (куба):
# print(cube1.get_volume())
