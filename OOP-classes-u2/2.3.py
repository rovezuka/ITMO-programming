class Doctor:
    default_name = "Айболит"
    default_age = 25
    def __init__(self, name, age):
        if name:
            self.name = name
        else:
            self.name = Doctor.default_name
        if age:
            if isinstance(age, int) and age > 18 and age < 110:
                self.age = age
            else:
                self.age = Doctor.default_age
        else:
            self.age = Doctor.default_age
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name


class Pediatrist(Doctor):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.type = "Pediatrist"
    def getName(self):
        return self.type, super().getName()

class Oculist(Doctor):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.type = "Oculist"
    def getName(self):
        return self.type, super().getName()

class Dentist(Doctor):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.type = "Dentist"
    def getName(self):
        return self.type, super().getName()


pediatrist = Pediatrist("","")
oculist = Oculist("Ivan", 200)
dentist = Dentist("Oleg", 40)

print(pediatrist.getName())
print(oculist.getName())
print(dentist.getName())
print(dentist.type)
