class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, cords, speed):
        self._cords = [0, 0, 0]
        self.speed = speed
