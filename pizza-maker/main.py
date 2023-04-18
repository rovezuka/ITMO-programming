import classes
menu = classes.Terminal()  # импорт класса Terminal - выводит меню пиццерии
print(menu)
while True:
    menu.view_menu()
    com = input()
    menu.process(com)
    if com == '-1':
        break
    if com == '0':
        break
