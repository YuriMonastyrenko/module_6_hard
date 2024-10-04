import math
class Figure:

    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = []
        self.__color = list(color)
        self.filled = False

        if len(sides) == self.sides_count:
            self.set_sides(*sides)
        else:
            self.__sides = [1] * self.sides_count

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            return

    def __is_valid_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            for i in new_sides:
                if isinstance(i, int) and i > 0:
                    return True
                else:
                    return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
            return self.__sides
        else:
            return

class Circle(Figure):

    sides_count = 1

    def __init__(self, color, circumference):
        super().__init__(color, circumference)

        self.__radius = circumference / (2 * math.pi)

    def get_square(self):
        square = math.pi * (self.__radius ** 2)
        return square

    def get_radius(self):
        return self.__radius

class Triangle(Figure):

    sides_count = 3

    def __init__(self, color, a, b, c):
        if b is None or c is None:
            super().__init__(color, a, a, a)
        else:
            super().__init__(color, a, b, c)

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        square = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return square

class Cube(Figure):

    sides_count = 12

    def __init__(self, color, side = 1):
        super().__init__(color)
        self.set_sides(*[side] * self.sides_count)

    def get_volume(self):
        side_lenght = self.get_sides()[0]
        volume = side_lenght ** 3
        return volume

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())










