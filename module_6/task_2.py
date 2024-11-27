class Vehicle:
    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.model = model
        self.engine_power = engine_power
        self.color = color


class Sedan(Vehicle):
    def __init__(self):
