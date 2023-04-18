class Car:
    def __init__(self):
        self.color, self.type, self.year = None, None, False
        self.launch, self.disable = False, True


    def launch_car(self):
        if self.launch: print('Нельзя завести уже заведенный автомобиль')
        else:
            self.launch = True
            self.disable = False
            print('Автомобиль заведен')


    def disable_car(self):
        if self.disable: print('Нельзя заглушить уже заглушенный автомобиль')
        else:
            self.disable = True
            self.launch = False
            print('Автомобиль заглушен')


    def year_of_issue(self, year):
        if 2023 <= int(year) >= 1886:
            self.year = year
        else: print('Год неверный')
    def color_car(self, color):
        self.color = color


    def type_car(self, type):
        self.type = type


    def car_info(self):
        if self.year: print(self.color, self.type, self.year)

car = Car()
car.launch_car()
car.color_car(input('Введите цвет автомобиля: '))
car.type_car(input('Введите тип автомобиля: '))
car.year_of_issue(input('Введите год выпуска: '))
car.car_info()