class Progression:
    def arif_prog(self, a, n, s):
        return s + (n-1)*number
    def geom_prog(self, a, n, s):
        return step*number**(n-1)
print('Какую последовательность будем вводить? 1 - арифметическая, 2 - геометрическая')
if input() == '1': why = True
else: why = False
print('Введите шаг последовательности: ')
number = int(input())
print('Введите n-ый член прогрессии, который необходимо найти')
n = int(input())
step = int(input('Введите первый член последовательности: '))
progression = Progression()
if why: print(progression.arif_prog(number, n, step))
else: print(progression.geom_prog(number, n, step))
