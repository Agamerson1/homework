from threading import Thread
from queue import Queue
import time
import random


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        timeout = random.randint(3, 10)
        time.sleep(timeout)


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        if self.tables.guest is None:
            for guest in guests:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty:
            for table in self.tables:
                if table.guest is None:
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} сел(-а) за стол номер {table.number}.')
                    table.guest.start()
                    table.guest.join()
                    if not table.guest.is_alive():
                        print(f'{table.guest.name} покушал(-а) и ушёл (ушла)')
                        print(f'Стол номер {table.number} свободен')
                        table.guest = None


tables = [Table(number) for number in range(1, 6)]
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)

cafe.guest_arrival(*guests)
cafe.discuss_guests()
