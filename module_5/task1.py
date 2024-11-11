class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        cur_floor = 0
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for cur_floor in range(new_floor):
                print(cur_floor + 1)


h1 = House('ЖК Победа', 300)
h2 = House('Гараж', 2)
h1.go_to(7)
h2.go_to(-1)
