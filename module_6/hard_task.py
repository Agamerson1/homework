class Figure:
    sides_count = 0

    def __init__(self, color, sides):
        self.__sides = list(sides)
        self.__color = list(color)
        self.filled = False

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if self.is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def is_valid_color(self, r, g, b):
        if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
            return False
        return True

    def is_valid_sides(self, *sides):
        if self.sides_count == len(sides):
            for side in sides:
                if side > 0 and int:
                    continue
                else:
                    return False
            return True
        return False

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.sides_count == len(new_sides):
            self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, radius):
        super().__init__(color, [radius])
        self.filled = False

    def get_square(self):
        return 3.14 * self.get_sides()[0] ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.filled = False

    def get_square(self):
        half_perimeter = sum(self.__sides) / 2
        return (half_perimeter * (half_perimeter - self.get_sides()[0]) * (half_perimeter - self.get_sides()[1]) * (
                half_perimeter - self.get_sides()[2])) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, sides):
        super().__init__(color, [sides] * 12)
        self.filled = False

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)
circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())
print(len(circle1))
print(cube1.get_volume())
