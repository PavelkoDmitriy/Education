class Figure:
    sides_count = 0

    def __init__(self, color, sides):
        self.__sides = sides  # список сторон
        self.__color = list(color)  # список цветов
        self.filled = bool()

    def get_color(self):
        return self.__color  # возвращает список цветов

    def __is_valid_color(self, r, g, b):
        range_ = range(256)
        return r in range_ and g in range_ and b in range_

    def __is_valid_sides(self, sides):
        if len(sides) == self.sides_count:
            for side in sides:
                if side <= 0 or not isinstance(side, int):
                    return False
            return True
        return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_sides(self):
        return self.__sides

    def __len__(self):
        perimeter = 0
        for side in self.__sides:
            perimeter += side
        return perimeter

    def set_sides(self, *new_sides):
        sides = list(new_sides)
        if self.__is_valid_sides(sides):
            self.__sides = sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, radius):
        super().__init__(color, [1])
        self.__radius = radius
        self.set_sides(radius)

    def get_square(self):
        square = 3.14159 * self.__radius ** 2
        return square


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, [1, 1, 1])
        self.set_sides(*sides)

    def get_square(self):
        s = sum(self.__sides) / 2
        square = (s * (s - self.__sides[0]) * (s - self.__sides[1]) * (s - self.__sides[2])) ** 0.5
        return square


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side):
        super().__init__(color, [1] * 12)
        self.__sides = [side] * 12
        self.set_sides(*([side] * 12))

    def get_volume(self):
        volume = self.__sides[0] ** 3
        return volume


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
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
