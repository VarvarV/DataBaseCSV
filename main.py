# Импорт библиотеки
import sqlite3
import csv

# Подключение к БД
con = sqlite3.connect("films_db.sqlite")

# Создание курсора
cur = con.cursor()

# Выполнение запроса и получение всех результатов
result = cur.execute("""
    SELECT films.id,
       films.title,
       year,
       genres.title,
       duration
  FROM films
  inner join genres
      on genres.id = films.genre
  where duration <= 5  
  order by genres.title, films.title
      """).fetchall()

# with open('res_file.csv', 'w', newline='', encoding="utf8") as csvfile:
with open('res_file.csv', 'w', newline='') as csvfile:
    writer = csv.writer(
        csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for elem in result:
        print(elem)
        writer.writerow(elem)

con.close()