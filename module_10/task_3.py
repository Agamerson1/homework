import threading
import random
import time

lock = threading.Lock()


class Bank:
    def __init__(self, balance, lock):
        self.balance = balance
        self.lock = lock

    def deposit(self):
        for i in range(100):
            self.balance += random.randint(50, 100)
            if self.balance >= 500 and lock.locked:
                lock.release()
            print(f'Пополнение: {random.randint(50, 100)}')
            time.sleep(0.001)

    def take(self):
