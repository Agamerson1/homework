class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f'Название: {self.name}, количество этажей: {self.number_of_floors}')

    def go_to(self, new_floor):
        cur_floor = 0
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for cur_floor in range(new_floor):
                print(cur_floor + 1)


h1 = House('ЖК Победа', 300)
h2 = House('Гараж', 2)
# __str__
print(h1)
print(h2)
# __len__
print(len(h1))
print(len(h2))
