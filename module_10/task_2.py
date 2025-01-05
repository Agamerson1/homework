import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!\n')
        days_count = 0
        enemy_count = 100
        while enemy_count > 0:
            time.sleep(1)
            days_count += 1
            enemy_count = enemy_count - self.power
            print(f'{self.name} сражается {days_count} день(дня)..., осталось {enemy_count} воинов\n')
        print(f'{self.name} одержал победу спустя {days_count} дней(дня)\n')


first_knight = Knight('William', 10)
first_knight.start()
second_knight = Knight('Arthur', 20)
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')
