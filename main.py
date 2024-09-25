import threading
from threading import Thread, Lock
from random import randint
from time import sleep

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            amount = randint(50,100)
            self.lock.acquire()
            try:
                self.balance += amount
                print(f'Пополнение: {amount}. Баланс: {self.balance}')
            finally:
                self.lock.release()
            sleep(0.001)


    def take(self):
        print(f'Запрос на {randint(50, 500)}')
        for i in range(100):
            diff = randint(50,100)
            self.lock.acquire()
            try:
                if diff <= self.balance:
                    self.balance -= diff
                    print(f'Снятие: {diff}. Баланс: {self.balance}')
                else:
                    print('Запрос отклонён, недостаточно средств')
            finally:
                self.lock.release()
            sleep(0.001)


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
