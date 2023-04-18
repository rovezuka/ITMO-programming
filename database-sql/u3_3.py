import sqlite3 as sq

try:
    # создание publ.db
    connection = sq.connect('publ.db')
    cursor = connection.cursor()
    print('Соединение с базой данной прошло успешно')

    # создание таблицы пользователей
    # указание какие поля она содержит
    cursor.execute("""CREATE TABLE IF NOT EXISTS tUser(
       userid INT PRIMARY KEY,
       name TEXT,
       year INT,
       gender TEXT);
    """)
    connection.commit()

    # создание таблицы публикаций
    cursor.execute("""CREATE TABLE IF NOT EXISTS tPubl(
           publid INT PRIMARY KEY,
           id_user INT,
           title TEXT,
           description TEXT,
           FOREIGN KEY(id_user) REFERENCES tUser(userid));
        """)

    # создание таблицы комментариев
    cursor.execute("""CREATE TABLE IF NOT EXISTS tComment(
       commentid INT PRIMARY KEY,
       id_publ INT,
       id_user INT,
       textcomment TEXT,
       FOREIGN KEY(id_publ) REFERENCES tPubl(id),
       FOREIGN KEY(id_user) REFERENCES tUsers(id));
    """)

    # указание первоначального значения в таблице пользователей
    cursor.execute("""INSERT INTO tUser(userid, name, year, gender) 
       VALUES(1, 'Мужик из двора', 32, 'муж');""")
    connection.commit()
    # id, имя, возраст, пол в tUser
    more_tUser = [(2, 'Клеопатра Петровна', 79, 'жен'),
                  (3, 'Саша жук', 14, 'муж'),
                  (4, 'Арина', 28, 'жен'),
                  (5, 'Лима', 23, 'жен'),
                  (6, 'Карина', 19, 'жен'),
                  (7, 'Настя', 18, 'жен'),
                  (8, 'Кот', 2, 'муж'),
                  (9, 'Полина', 16, 'жен'),
                  (10, 'Аня', 18, 'жен')]
    cursor.executemany("INSERT OR REPLACE INTO tUser VALUES(?, ?, ?, ?);", more_tUser)
    connection.commit()  # заполнение tUser

    more_tComment = [(2, 7, 6, 'wow!!!'), (3, 9, 2, 'it"s cool')]
    cursor.executemany("INSERT OR REPLACE INTO tComment VALUES(?, ?, ?, ?);", more_tComment)
    connection.commit() # заполнение tComment

    more_tPubl = [(2, 7, 'Car', 'I love it'), (3, 4, 'Angry man', 'I"m hate angry man')]
    cursor.executemany("INSERT OR REPLACE INTO tPubl VALUES(?, ?, ?, ?);", more_tPubl)
    connection.commit() # заполнение tPubl

    # выбор всех значений через SELECT и создание упорядоченного списка через fetchall
    cursor.execute('SELECT * FROM tUser')
    all_results1 = cursor.fetchall()
    print(all_results1)
    cursor.execute('SELECT * FROM tPubl')
    all_results2 = cursor.fetchall()
    print(all_results2)
    cursor.execute('SELECT * FROM tComment')
    all_results3 = cursor.fetchall()
    print(all_results3)

    # возвращает первую запись(fetchone)
    record = cursor.fetchone()
    cursor.close()
except sq.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (connection):
        connection.commit()
        connection.close()
        print("Соединение с SQLite закрыто")