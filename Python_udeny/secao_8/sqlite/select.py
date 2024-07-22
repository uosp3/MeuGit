import sqlite3

from create_insert import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    f'SELECT * FROM {TABLE_NAME}'
)

for row in cursor.fetchall():
    _id, name, weight = row  # desempacotando a tupla
    print(_id, name, weight)


print('='*30)

cursor.execute(
    f'SELECT * FROM {TABLE_NAME} '
    'WHERE id = "3"'
)
row = cursor.fetchone()
_id, name, weight = row  # desempacotando a tupla
print(_id, name, weight)

cursor.close()
connection.close()

# https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/37168300#questions/19918772
