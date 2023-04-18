class Soda:
    def __init__(self, add):
        self.add = add
        if not self.add: self.add = 'Обычная газировка'

    def show_my_drink(self):
        if self.add == 'Обычная газировка':
            return self.add
        return f'Газировка и {self.add}'

soda = Soda(input('Введите добавку: '))
print(soda.show_my_drink())