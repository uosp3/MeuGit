import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

#  CRUD  -  Create   Read    Update  Delete
#           INSERT   SELECT  UPDATE  DELETE

# CUIDADO: Fazendo delete sem where, apaga tudo na tabela
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

# DELETE mais cuidadoso
cursor.execute(  # zera os id
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

# Cria a tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

# Registrar valores na tabela
sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES '
    '(?, ?)'  # os valores são repassados depois, por segurança.
)
cursor.execute(sql, ['Edson', 67.3])  # aqui vão os valores
cursor.executemany(
    sql,
    (  # feito com tupla mas pode ser com list também
         ('Luisa', 50), ('Laine', 55), ('Bianca', 52)
    )
)  # para vários valores
connection.commit()

if __name__ == '__main__':
    print(sql)

    cursor.close()
    connection.close()

# No lugar de (?, ?), linha 37, pode ser usado (:nome, :peso), neste caso
# so valores devem ser um dictionary, conforme abaixo
"""
cursor.executemany(sql, (
    {'nome': 'Joãozinho', 'peso': 3},
    {'nome': 'Maria', 'peso': 2},
    {'nome': 'Helena', 'peso': 4},
    {'nome': 'Joana', 'peso': 5},
))
"""

#  https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/36988164#questions
#  https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/36989234#questions
#  https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/37006456#questions
#  https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/37165524#questions
