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
        self.name = name

    def run(self):
        timeout = random.randint(0, 10)
        time.sleep(timeout)


class Cafe:
    def __init__(self, tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            self.queue.put(guest)
            print(f'{guest.name} has arrived at the cafe.')

    def discuss_guest(self):
        while self.queue.empty
