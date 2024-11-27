class Vehicle:
    __COLOR_VARIANTS = ['pink', 'red', 'black', 'green', 'yellow']

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self, model):
        return f'Модель: {self.__model}'

    def get_horsepower(self, engine_power):


class Sedan(Vehicle):
    def __init__(self):
