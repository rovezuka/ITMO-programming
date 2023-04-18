import time
import functools
from abc import ABC, ABCMeta, abstractmethod, abstractproperty


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        runtime = time.perf_counter() - start
        print(f"Время выполнения заказа {runtime:.4f} секунд")
        return result

    return wrapper

class Done:
    __metaclass__ = ABCMeta
    @abstractmethod
    def done(self):
        pass
        '''Готовность пиццы'''

class Pizzeria():
    def __init__(self, name='name', dough='dough', sauce='sous', ingredient='ingred', price=10):
        self.__name = name
        self.dough = dough
        self.sauce = sauce
        self.price = price
        self.ingredient = ingredient
        # конструктор класса пиццы

    def __str__(self):  # перегрузка базового метода str
        return f'Пицца: {self.__name}, соус: {self.dough}, ингредиент: {self.ingredient}, цена: {self.price} руб.'


    # Методы приготовления пиццы
    def get_ready(self):
        return ('Пицца ' + self.__name + ' готовится')

    def dough_b(self):
        return ("Тесто " + self.dough + " замешивается")

    def sauce_b(self):
        return ('Соус ' + self.sauce + ' добавляется')

    def ingredient_b(self):
        return ("Главный ингредиент " + self.ingredient + ' добавляется')

    def baking(self):
        return ("Пицца " + self.__name + " отправлена в печь")

    def slicing(self):
        return ('Пицца ' + self.__name + ' нарезается')

    def packing(self):
        return ('Пицца ' + self.__name + ' упаковывается')

    @property  # функция-геттер для приватного атрибута name
    def name(self):
        return self.__name


class Pepperoni(Pizzeria, Done):  # дочерние классы класса пиццы (разновидности пицц)
    def __init__(self):
        super().__init__("Пепперони")
        self.__name = 'Пепперони'
        self.dough = "тонкое"
        self.sauce = "томатный"
        self.ingredient = "колбаса"
        self.price = 100
        # Дочерний класс "Пепперони"
    @abstractmethod
    def done(self):
        print('Пицца Пепперони выдана!')


P = Pepperoni()


class Barbeque(Pizzeria):
    def __init__(self):
        super().__init__("Барбекю")
        self.__name = 'Барбекю'
        self.dough = "тонкое"
        self.sauce = "барбекю"
        self.ingredient = 'курица'
        self.price = 200
        # Дочерний класс "Барбекю"

    @abstractmethod
    def done(self):
        print('Пицца Барбекю выдана!')


B = Barbeque()


class Marine(Pizzeria):
    def __init__(self):
        super().__init__('Дары моря')
        self.__name = 'Дары моря'
        self.dough = "толстое"
        self.sauce = "сливочный"
        self.ingredient = "морепродукты"
        self.price = 300
        # Дочерний класс "Дары моря"

    @abstractmethod
    def done(self):
        print('Пицца Дары моря выдана!')


M = Marine()


class Order:
    count = 0
    B = Barbeque()
    P = Pepperoni()
    M = Marine()

    def __init__(self):  # конструктор класса
        self.pizzainZ = []
        Order.count += 1

    def __str__(self):
        sum = 0
        print('Заказ N', Order.count)
        for i in range(len(self.pizzainZ)):
            if self.pizzainZ[i] == 'P':
                print(P.__str__())
                sum = int(P.price) + sum
            if self.pizzainZ[i] == 'B':
                print(B.__str__())
                sum = int(B.price) + sum
            if self.pizzainZ[i] == 'M':
                print(M.__str__())
                sum = int(M.price) + sum
        print("Сумма заказа:", sum, 'руб')
        return ''

    def add(self, numberofpizza):  # список заказнных пользователем пицц
        self.numberofpizza = numberofpizza
        if numberofpizza == 1:
            self.pizzainZ.append('P')
        if numberofpizza == 2:
            self.pizzainZ.append('B')
        if numberofpizza == 3:
            self.pizzainZ.append('M')

    def zsum(self):  # Подсчет суммы заказанной пиццы
        summ = 0
        for i in range(len(self.pizzainZ)):
            if self.pizzainZ[i] == 'P':
                summ = int(P.price) + summ
            if self.pizzainZ[i] == 'B':
                summ += int(B.price)
            if self.pizzainZ[i] == 'M':
                summ = int(M.price) + summ
        return summ
    @timer
    def do(self):  # функция выполнения заказа, декоратор на время выполнения функции
        print('Заказ поступил на выполнение')
        time.sleep(1)
        for i in range(len(self.pizzainZ)):
            if self.pizzainZ[i] == 'P':
                print(i + 1, '.', P.name)
                time.sleep(1)
                print(P.get_ready())
                time.sleep(1)
                print(P.dough_b())
                time.sleep(1)
                print(P.sauce_b())
                time.sleep(1)
                print(P.ingredient_b())
                time.sleep(1)
                print(P.baking())
                time.sleep(1)
                print(P.slicing())
                time.sleep(1)
                print(P.packing())
                time.sleep(1)
                P.done()
            if self.pizzainZ[i] == 'M':
                print(i + 1, '.', M.name)
                time.sleep(1)
                print(M.get_ready())
                time.sleep(1)
                print(M.dough_b())
                time.sleep(1)
                print(M.sauce_b())
                time.sleep(1)
                print(M.ingredient_b())
                time.sleep(1)
                print(M.baking())
                time.sleep(1)
                print(M.slicing())
                time.sleep(1)
                print(M.packing())
                time.sleep(1)
                M.done()
            if self.pizzainZ[i] == 'B':
                print(i + 1, '.', B.name)
                time.sleep(1)
                print(B.get_ready())
                time.sleep(1)
                print(B.dough_b())
                time.sleep(1)
                print(B.sauce_b())
                time.sleep(1)
                print(B.ingredient_b())
                time.sleep(1)
                print(B.baking())
                time.sleep(1)
                print(B.slicing())
                time.sleep(1)
                print(B.packing())
                time.sleep(1)
                B.done()


O = Order()


class Terminal:
    otmena = -1
    ok = 0

    def __init__(self):
        self.menu = [P.__str__(), B.__str__(), M.__str__()]
        self.pizzazakaz = None
        self.viewmenu = True

    def __str__(self):
        return 'Добро пожаловать! '

    def view_menu(self):  # функция для просмотра меню
        print('Меню:')
        print('1. ', P.__str__())
        print('2. ', B.__str__())
        print('3. ', M.__str__())  # вывод меню
        print('Выберите номер пиццы! \nДля отмены заказа и выхода введите -1 \nДля подтверждения заказа введите 0')
        self.viewmenu = False
        if not self.viewmenu:
            return

    def process(self, com):  # функция обработки команд
        if com == '-1' or com == '0' or com == '1' or com == '2' or com == '3':
            com = int(com)
            if com == Terminal.otmena:
                print("Отмена заказа")
            elif com == Terminal.ok:
                if len(O.pizzainZ) > 0:
                    print("Подтверждение заказа")
                    O.__str__()
                    T.payment()
                    O.do()
                else:
                    print("Отмена заказа")
            elif 1 <= com <= 3:
                O.add(com)
                print()
        else:
            print("Некорректные данные, повторите ещё раз")

    def odd_money(self, oplata):  # функция выдачи сдачи
        return oplata - O.zsum()

    def payment(self):  # функция оплаты
        oplata = int(input("Введите сумму:"))
        if oplata == int(O.zsum()):
            print("Вы внесли ", oplata, " руб. Сдача: 0 руб.")
        if oplata > int(O.zsum()):
            vernyt = (T.odd_money(int(oplata)))
            print("Вы внесли ", oplata, "руб. Сдача: ", vernyt, " руб.")
        if oplata < int(O.zsum()):
            print("Оплата меньше стоимости заказа! Введите сумму снова!")
            T.payment()


T = Terminal()

if __name__ == '__main__':
    t = Terminal()
    print(t)
    while True:
        t.view_menu()
        com = input()
        t.process(com)
        if com == '-1':
            break
        if com == '0':
            break
