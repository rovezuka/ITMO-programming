import check1 as cl
from check1 import ValueOutOfRangeError
from threading import Thread

while True:
    try:
        c = input('Введите, чей поединок хотите устроить: 1 - футболистов, 2 - хоккеистов, 3 - хоккеиста с футболистом \n')  # пользователь вводит цифру
        while c.isdigit() == True and 0 < int(c) <= 3:  # пока введено верное значение
            cl.asyncio.run(cl.waiting())
            ter_1 = cl.Duel(c).fight()
            ter_2 = cl.second_fight()
            t1 = Thread(target=ter_1)
            t2 = Thread(target=ter_2)

            t1.start()
            t2.start()
            #b = cl.Duel(c)

            #b.fight()
            break
        else:
            raise ValueOutOfRangeError
    except ValueOutOfRangeError:
        print('Ошибка! Введите число от 1 до 3')
        continue
    else:
        end_fight = cl.End_fight().go_to_peace()
        break

