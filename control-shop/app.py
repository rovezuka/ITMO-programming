from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.ttk import Combobox  # импортируем библиотеку tkinter для создания графического интерфейса
import datetime  # импортируем для вывода даты

def delete():  # функция удаления значения из словаря
    txt1.delete(0, END)  # очиста поля ввода
    txt2.delete(0, END)
    txt3.delete(0, END)
    txt4.delete(0, END)

def chdate(dat):  # проверка корректности ввода даты
    try:
        datetime.datetime.strptime(dat, '%d.%m.%Y')  # если формат значения верный
    except ValueError:
        messagebox.showinfo('Ошибка', 'Введите дату в формате дд.мм.гггг')  # иначе вывод сообщения об ошибке
        txt4.delete(0, END)  # удаляем значение из словаря
        return False
    return True

def chprice(pr):  # проверка корректности ввода цены
    for i in pr:
        if i not in '0123456789':  # если введены не цифры, то выводим сообщение об ошибке
            messagebox.showinfo('Ошибка', 'Введите корректное значение цены')
            txt3.delete(0, END)
            return False
        else:
            return True

def append():
    name = format(txt1.get()) # в эти переменные добавляются значения из окна ввода
    category = format(txt2.get())
    dt = format(txt4.get())
    price = format(txt3.get())  # методом get() получаем значение по ключу
    if len(name) != 0:
        names.append(name)
        if len(category) != 0:
            categ.append(category)
            if chprice(price):
                prices.append(price)
                if chdate(dt):
                    date.append(dt)  # если ввод значений корректный, то добавляем значение в соответствующий массив
        else:
            messagebox.showinfo('Ошибка', 'Все поля должны быть заполнены')
    else:
        messagebox.showinfo('Ошибка', 'Все поля должны быть заполнены')  # если ввод некорректный
    if category not in c:
        c.append(category)
    if dt not in d:  # если значения еще нет в массиве
        d.append(dt)
    comboone['values'] = tuple(c)  # два виджета для просмотра значений, добавляем в них элементы
    combotwo['values'] = tuple(d)
    if len(names) == len(date) ==len(prices) == len(categ):
        all.append(names[-1] + ' ' + categ[-1] + ' ' + prices[-1] + ' ' + date[-1])
        combothree['values'] = tuple(all)
        txt.insert('1.0', names[-1] + ' ' + categ[-1] + ' ' + prices[-1] + ' ' + date[-1]+'\n')
        f = open('moneyy.txt', 'a')
        f.write(names[-1] + ' ' + categ[-1] + ' ' + prices[-1] + ' ' + date[-1]+'\n')  # значение всех переменных записываются в файл moneyy.txt
    delete()

def sortub():
    zipped = list(zip(prices, names, categ, date))
    zipped.sort(key=lambda n: int(n[0]))
    return zipped

def sortvoz():
    zipped = list(zip(prices, names, categ, date))
    zipped.sort(reverse=True, key=lambda n: int(n[0]))
    return zipped

def cl():  # для сортировки по убыванию
    s = sortub()
    price, name, categ, date = zip(*s)  # обьединяет элементы разных типов данных в один
    txt.delete(1.0, END)  # очистка поля и вывод отсортированного набора
    for i in range(len(name)):
        txt.insert('1.0', name[i] + ' ' + categ[i] + ' ' + price[i] + ' ' + date[i] + '\n')  # сортировка при нажатии кнопки на виджете

def click():  # для сортировки по возрастанию
    s = sortvoz()
    price, name, categ, date = zip(*s)
    txt.delete(1.0, END)
    for i in range(len(name)):
        txt.insert('1.0', name[i] + ' ' + categ[i] + ' ' + price[i] + ' ' + date[i] + '\n')

def pocat():  # показ элементов первого виджета по категории
    choice = comboone.get() # записываем выбранный элемент
    zipped = list(zip(names, categ, prices, date))
    txt.delete(1.0, END)
    for i in range(len(zipped)): # проходимся по всем элементам
        if zipped[i][1] == choice:  # если совпадает
            for j in range(4):
                txt.insert('1.0', str(zipped[i][j])+' ')
            txt.insert('1.0','\n')  # выводим эту запись в текстовое поле

def podat():  # показ элементов второго виджета по дате
    choice = combotwo.get()  # записываем выбранный элемент
    zipped = list(zip(names, categ, prices, date))
    txt.delete(1.0, END)
    for i in range(len(zipped)):
        if zipped[i][3] == choice:
            for j in range(4):
                txt.insert('1.0', str(zipped[i][j])+' ')
            txt.insert('1.0','\n')

def dell():  # функция для удаления элемента
    choice = combothree.get()  # удаляем эту запись из виджета
    if choice == '':
        return
    for i in range(len(all)):
        if all[i] == choice:
            all.remove(all[i])
            txt.delete('1.0', END)
            combothree['values'] = tuple(all)
            break
    f = open('moneyy.txt', 'w')  # файл перезаписывается
    for i in range(len(all)):
        f.write(all[i] + '\n')
        txt.insert(f'{i+1}.0', all[i] + '\n')


date, prices, categ, names, c, d, all = [], [], [], [], [], [], []
window = Tk()
window.title('Кошелек')
window.geometry('600x450')
lbl1 = Label(window, text='Наименование', font=('Arial Bold', 10))
lbl1.grid(column=1, row=0)
lbl2 = Label(window, text='Категория', font=('Arial Bold', 10))
lbl2.grid(column=1, row=2)
lbl3 = Label(window, text='Цена', font=('Arial Bold', 10))
lbl3.grid(column=1, row=4)
lbl4 = Label(window, text='Дата (дд.мм.гггг)', font=('Arial Bold', 10))
lbl4.grid(column=1, row=6)

txt1 = Entry(window,width=20)
txt1.grid(column=2,row=0)
txt2 = Entry(window, width=20)
txt2.grid(column=2, row=2)
txt3 = Entry(window, width=20)
txt3.grid(column=2, row=4)
txt4 = Entry(window, width=20)
txt4.grid(column=2, row=6)
btn = Button(window,text='добавить', command=append)
btn.grid(column=2, row=8)
lbl0 = Label(window, text='  ', font=('Arial Bold', 10))
lbl0.grid(column=2, row=10)
lbl0 = Label(window, text='  ', font=('Arial Bold', 10))
lbl0.grid(column=0, row=0, rowspan=11)
lbl0 = Label(window, text='  ', font=('Arial Bold', 10))
lbl0.grid(column=3, row=0, rowspan=11)

txt = scrolledtext.ScrolledText(window, width=50, height=10)
txt.grid(column=1, row=11, columnspan=2, rowspan=8)
btn = Button(window,text='сортировать по убыванию', command=cl)
btn.grid(column=1, row=19)
btn = Button(window,text='сортировать по возрастанию', command=click)
btn.grid(column=2, row=19)
lbl0 = Label(window, text='  ', font=('Arial Bold', 10))
lbl0.grid(column=1, row=20)
lbl0 = Label(window, text='просмотр по категории:', font=('Arial Bold', 10))
lbl0.grid(column=1, row=21)
comboone = Combobox(window)
comboone.grid(column=1, row=22)
btn = Button(window,text='просмотр', command=pocat)
btn.grid(column=1, row=23)

lbl0 = Label(window, text='просмотр по дате:', font=('Arial Bold', 10))
lbl0.grid(column=2, row=21)
combotwo = Combobox(window)
combotwo.grid(column=2, row=22)
btn = Button(window,text='просмотр', command=podat)
btn.grid(column=2, row=23)
lbl0 = Label(window, text='удаление:', font=('Arial Bold', 10))
lbl0.grid(column=3, row=13)
btn = Button(window,text='удалить', command=dell)
btn.grid(column=3, row=15)
combothree = Combobox(window)
combothree.grid(column=3, row=14)
combothree['state'] = 'readonly'
window.mainloop()