import sqlite3 as sq

# Попытаться открыть соединение к базе
try:
    # осуществить подключение к БД sqlitePy
    connection = sq.connect('city.db')
    
    # создать курсор для выполнения запросов
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS city(
       userid INT PRIMARY KEY,
       city_name TEXT);
    """)

    connection.commit()
    print("База данных создана и успешно подключена к SQLite")
    
    #  создание таблицы с первоначальным значением
    cursor.execute("""INSERT INTO city(userid, city_name) 
       VALUES('1', 'Moscow');""")
    
    # Метод connect.commit() фиксирует текущую транзакцию. 
    # Если не вызывать этот метод, то все, что сделано после последнего вызова connect.commit(), 
    # не будет видно из других соединений с базой данных.
    connection.commit()

    # список городов
    more_city = [('2', 'Ufa'),
                 ('3', 'Kazan'),
                 ('4', 'Moscow'),
                 ('5', 'Saint-Petersburg'),
                 ('6', 'Barcelona'),
                 ('7', 'Madrid'),
                 ('8', 'Ekaterinburg'),
                 ('9', 'Volgograd'),
                 ('10', 'Krasnodar')]
    # добавление значений в БД
    cursor.executemany("INSERT INTO city VALUES(?, ?);", more_city)
    connection.commit()

    # Выбрать все значения из таблицы city, которая находится в базе данных city
    cursor.execute("SELECT * FROM city;")

    # получить первое значение
    first_result = cursor.fetchone()
    print(f'Первое значение в базе данных: {first_result}')

    cursor.execute("SELECT * FROM city;")
    five_results = cursor.fetchmany(5)
    print(f'Пять значений из базы данных: {five_results}')

    cursor.execute("SELECT * FROM city;")
    all_results = cursor.fetchall()
    print(f'Все значения из базы данных {all_results}')

    # вывести текущую версию БД
    select_query = "select sqlite_version();"
    cursor.execute(select_query)
    
    record = cursor.fetchall()
    print("Версия базы данных SQLite: ", record)
    
    # закрыть курсор
    cursor.close()

# если соединение не открылось
except sq.Error as error:
    print("Ошибка при подключении к sqlite", error)

finally:
    # закрыть соединение с базой
    if (connection):
        connection.commit()
        connection.close()
        print("Соединение с SQLite закрыто")

