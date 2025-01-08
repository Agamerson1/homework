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
            random_num = random.randint(50, 100)
            if self.balance >= 500 and lock.locked:
                lock.release()
            self.balance += random_num
            print(f'Пополнение: {random_num}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            random_num = random.randint(50, 100)
            print(f'Запрос на {random_num}')
            if random_num == self.balance or random_num <= self.balance:
                self.balance -= random_num
                print(f'Снятие: {random_num}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств на счету')
                lock.acquire()
            time.sleep(0.001)


bk = Bank(0, lock)
