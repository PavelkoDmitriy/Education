import threading
from random import randint
from time import sleep as delay


class Bank:
    def __init__(self):
        self.balance = int()
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            if self.lock.locked() and self.balance >= 500:
                self.lock.release()
            random_cash = randint(50, 500)
            self.balance += random_cash
            print(f"Пополнение: {random_cash}. Баланс: {self.balance}")
            delay(0.001)

    def take(self):
        for i in range(100):
            random_cash = randint(50, 500)
            print(f"Запрос на {random_cash}")
            if random_cash <= self.balance:
                self.balance -= random_cash
                print(f"Снятие: {random_cash}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
