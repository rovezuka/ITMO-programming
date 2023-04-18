class Country:
    def set_population(self, population):
        if population > 0:
            self.population = population
        else:
            self.population = None
            print("Недопустимое население")

    def get_population(self):
        return self.population

class Russia(Country):
    def __init__(self):
        self.capital = "Moscow"

class Germany(Country):
    def __init__(self):
        self.capital = "Berlin"

class Canada(Country):
    def __init__(self):
        self.capital = "Ottawa"


russia = Russia()
germany = Germany()
canada = Canada()

print("Russia:")
russia.set_population(-100)
print(russia.capital)
print(russia.get_population())

print("Germany:")
germany.set_population(83000000)
print(germany.capital)
print(germany.get_population())

print("Canada:")
canada.set_population(38000000)
print(canada.capital)
print(canada.get_population())