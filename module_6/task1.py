class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name

    def eat(self, food):
        if food.edible is True:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name


class Mammal(Animal):


class Predator(Animal):
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    pass
