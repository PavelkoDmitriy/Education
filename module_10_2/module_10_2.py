from threading import Thread
from time import sleep as delay


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.__enemies = 100
        self.__days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.__enemies > 0:
            self.__enemies -= self.power
            self.__days += 1
            print(f"{self.name} сражается {self.__days}..., осталось {self.__enemies} воинов.")
            delay(1)
        print(f"{self.name} одержал победу спустя {self.__days} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print("Все битвы закончились!")
