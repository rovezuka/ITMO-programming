from random import randint
from abc import ABC, abstractmethod
import time
import threading
import asyncio


async def waiting():
    print('Идет подготовка бойцов...')
    await asyncio.sleep(2)
    print('Бойцы размялись успешно!')
    await asyncio.sleep(1)
    print('Бойцы начали драться!')


def second_fight():
    print('Вторичный поток')
    asyncio.run(waiting())
    Duel(input('Введите нужный поединок:')).fight()

def time_of_function(func):  # замер времени выполнения функции
    def timer(*args):
        start_time = time.perf_counter_ns()
        res = func(*args)
        print('Время выполнения функции', func.__name__, (time.perf_counter_ns() - start_time)/10000, 'секунд')
        return res
    return timer


class Health(ABC): # абстрактный класс
    def __init__(self, health):
        self._health = health

    @property
    def health(self):
        return self._health


class Fighter(ABC):  # абстрактный класс
    def __init__(self, name='', health=100, typ='', power=0, stun=0):
        self._name = name
        self._health = Health(health)
        self.type = typ  # тип бойца
        self._power = power
        self._stun = stun

    @property  # невозможно изменить метод напрямую, только косвенно
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @property
    def typ(self):
        return self.type

    @abstractmethod
    def block(self):
        pass

    def get_power(self):
        return self._power

    def get_stun(self):
        return self._stun

    def __add__(self, value=20):  # методы +- здоровья
        return Fighter(self.name, self.health.health + value)

    def __sub__(self, value=20):
        return Fighter(self.name, self.health.health - value)


class Football(Fighter):
    def __init__(self, name='', health=100, stun=1):
        Fighter.__init__(self, name, health, 'Футболисты', stun)  # передаем значения бойца в абстрактный класс

    @time_of_function
    def __add__(self, value=20):
        return Football(self.name, self._health.health + value)

    @time_of_function
    def __sub__(self, value=20):
        return Football(self.name, self._health.health - value)

    def get_health(self): # здоровье футболиста
        return self.health.health

    def get_name(self): # здоровье футболиста
        return self.name

    def get_type(self):
        return self.type

    def ball_stun(self):  # бонусный навык
        if randint(1, 30) == 5:
            return True
        else:
            return False

    def block(self):  # защита
        print(f"{self.name} успел защититься!")


class Hockey(Fighter):
    def __init__(self, name='', health=100, died=15):
        Fighter.__init__(self, name, health, 'Хоккеисты', died)

    def get_health(self):
        return self.health.health  # здоровье хоккеиста

    def get_type(self):
        return self.type

    def get_name(self):  # имя хоккеиста
        return self.name

    def hockey_shelmet(self): # бонусный навык
        if randint(1, 10) == 5:
            return True
        else:
            return False

    @time_of_function
    def __add__(self, value=20):
        return Hockey(self.name, self._health.health + value)

    @time_of_function
    def __sub__(self, value=20):
        return Hockey(self.name, self._health.health - value)

    def block(self):
        print(f"{self.name} успел защититься!")


class End_fight(Football, Hockey):
    def go_to_peace(self):
        return print('После драки дружно пожали руки и разошлись!')


class ValueOutOfRangeError(Exception):  # встроенная ошибка
    pass


class Duel:
    def __init__(self, count):
        self.count = count
        self.flag = True
        if count == '1':  # проверяем какое значение ввел пользователь
            name = input('Введите имя первого футболиста\n')
            self.first = Football(name, 100)  # передаем имя и здоровье в класс футболиста
            name = input('Введите имя второго футболиста\n')
            self.second = Football(name, 100)
        elif count == '2':
            name = input('Введите имя первого хоккеиста\n')
            self.first = Hockey(name, 100) # передаем имя и здоровье в класс хоккеиста
            name = input('Введите имя второго хоккеиста\n')
            self.second = Hockey(name, 100)
        elif count == '3':
            name_1 = input('Введите имя футболиста\n')
            self.first = Football(name_1, 100)
            name_2 = input('Введите имя хоккеиста\n')
            self.second = Hockey(name_2, 100)
    

    def fight(self):  # функция боя
        while True:
            shoot = randint(1, 2)  # рандомно атакует первый, либо второй
            if Hockey().hockey_shelmet() == False and Football().ball_stun() == False:  # если бонусные навыки не сработали
                if shoot == 1:  # атаковал первый боец
                    print('Атаковал первый')
                    self.second = self.second.__sub__(20)  # вычитаем 20 из здоровья
                    print(f'Здоровье первого = {self.first.get_health()}\nЗдоровье второго = {self.second.get_health()}')  # возращаем значения здоровья бойцов
                else:
                    print('Атаковал второй')
                    self.first = self.first.__sub__(20)
                    print(f'Здоровье первого = {self.first.get_health()}\nЗдоровье второго = {self.second.get_health()}')

                if self.first.get_health() == 0: # если здоровье бойца закончилось
                    self.flag = False
                    print('Победил второй')
                    break
                elif self.second.get_health() == 0:
                    self.flag = False
                    print('Победил первый')
                    break
            else:
                if Hockey().hockey_shelmet(): 
                    print('Успешно проведен прием "хоккейный шлем"')
                    print(f'Здоровье первого = {self.first.get_health()}\nЗдоровье второго = {self.second.get_health()}')
                else:
                    print('Противник обездвижен')
                    print(f'Здоровье первого = {self.first.get_health()}\nЗдоровье второго = {self.second.get_health()}')
            next_step = 1
            while next_step:
                next_step = input('Чтобы продолжить нажмите Enter: ')
                format(next_step)



