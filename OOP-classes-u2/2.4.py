class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        if self.age >= 0 and self.age <= 19:
            self.age = age
        else:
            self.age = None
            print("Возраст кошки не может быть отрицательным и выше 19 лет.")
    def info(self):
        print(self.name, self.age)

class Sfinks(Cat):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.sherst = "Лысая"
        self.type = "Крысолов"
    def info(self):
        super().info()
        print(self.sherst, self.type)

class Meinkun(Cat):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.sherst = "Длинная шерсть"
        self.type = "Домашняя"
    def info(self):
        super().info()
        print(self.sherst, self.type)

class Korat(Cat):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.sherst = "Средняя шерсть"
        self.type = "Игрун"
    def info(self):
        super().info()
        print(self.sherst, self.type)


sfinks = Sfinks("Венди", 20)
meinkun = Meinkun("Джек", 5)
korat = Korat("Дружок", 7)

sfinks.info()
meinkun.info()
korat.info()