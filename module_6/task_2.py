class Vehicle:
    __COLOR_VARIANTS = ['pink', 'red', 'black', 'green', 'yellow']

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.color}'

    def print_info(self):
        print(f'Владелец: {self.owner}')
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())

    def set_color(self, new_color):
        if new_color in Vehicle.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    def __init__(self):
