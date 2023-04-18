class Pupil:
    def __init__(self):
        self.name = "Radomir"
        self.age = 8
        self.classNumber = "1-A"
    def set_age(self, age):
        self.age = age
    def get_age(self):
        return self.age
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def set_classNumber(self, classNumber):
        self.classNumber = classNumber
    def get_classNumber(self):
        return self.classNumber
    def info(self):
        return self.name, self.age, self.classNumber


radomir = Pupil()

daniil = Pupil()
daniil.set_name("Daniil")
daniil.set_age(9)
daniil.set_classNumber("2-A")

ivan = Pupil()
ivan.set_name("Ivan")
ivan.set_age(10)
ivan.set_classNumber("3-A")

nikolai = Pupil()
nikolai.set_name("Nikolai")
nikolai.set_age(11)
nikolai.set_classNumber("4-A")

sergey = Pupil()
sergey.set_name("Sergey")
sergey.set_age(12)
sergey.set_classNumber("5-A")

print(radomir.info())
print(daniil.info())
print(ivan.info())
print(nikolai.info())
print(sergey.info())
