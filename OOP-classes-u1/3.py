class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition(self):
        return self.a + self.b
    def multiplication(self):
        return self.a * self.b
    def division(self):
        if self.b == 0:
            return 'Деление на ноль невозможно'
        return self.a / self.b
    def subtraction(self):
        return self.a - self.b

math = Math(int(input('Введите первое число: ')), int(input('Введите второе число: ')))
print(math.addition())
print(math.multiplication())
print(math.division())
print(math.subtraction())