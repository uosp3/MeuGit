# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import os

import dotenv
import pymysql
import pymysql.cursors

TABLE_NAME = 'customers'

dotenv.load_dotenv()  # carregar as configurações do .env

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor,
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id)'
            ') '
        )
        # CUIDADO: ISSO LIMPA A TABELA
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
    connection.commit()  # facultativo para create table

    # Começo a manipular dados a partir daqui

    # inserindo valor usando placeholder e um iterável
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%s, %s) '  # evita mandar dados junto com o comando (injection)
        )
        data = ('Edson', 62)  # os valores são atribuidos a variável(tupla)
        result = cursor.execute(sql, data)  # a variável é repassada aqui
        # print(sql, data)
        # print(result)
    connection.commit()

    # inserindo valor usando placeholder e um dict
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '  # a ordem da linha 56 deve ser a mesma desta
            'VALUES '
            '(%(name)s, %(age)s) '  # evita mandar dados junto com o comando
        )
        data2 = {  # a ordem abaixo não precisa ser a mesma da linha 56
            'name': 'Gomes',
            'age': 36,
        }
        result = cursor.execute(sql, data2)  # a variável é repassada aqui
        # print(sql)
        # print(data2)
        # print(result)
    connection.commit()

    # inserindo varios valores usando placeholder e uma tupla de dicts
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '  # a ordem da linha 56 deve ser a mesma desta
            'VALUES '
            '(%(name)s, %(age)s) '  # evita mandar dados junto com o comando
        )
        data3 = (  # a ordem abaixo não precisa ser a mesma da linha 56
            {"name": "Laine", "age": 57, },
            {"name": "Bianca", "age": 33, },
            {"name": "Luisa", "age": 26, },
        )
        result = cursor.executemany(sql, data3)  # type: ignore
        # print(sql)
        # print(data3)
        # print(result)
    connection.commit()

    # inserindo vários valores usando placeholder e uma tupla de tuplas
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '  # a ordem da linha 56 deve ser a mesma desta
            'VALUES '
            '(%s, %s) '  # evita mandar dados junto com o comando
        )
        data4 = (  # neste caso a ordem dos dados deve ser a mesma da linha 91
            ("João", 17, ),
            ("Maria", 19, ),
            ("Luiz", 19, ),
        )
        result = cursor.executemany(sql, data4)  # type: ignore
        # print(sql)
        # print(data4)
        # print(result)
    connection.commit()

    # Lendo os valores com SELECT
    with connection.cursor() as cursor:
        # menor_id = int(input('Digite o menor id: '))
        # maior_id = int(input('Digite o maior id: '))
        menor_id = 2
        maior_id = 4

        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE id BETWEEN %s AND %s '
        )

        cursor.execute(sql, (menor_id, maior_id))
        # print(cursor.mogrify(sql, (menor_id, maior_id)))
        data5 = cursor.fetchall()

        # for row in data5:
        #     print(row)

    # Apagando com DELETE, WHERE e placeholders no PyMySQL
    with connection.cursor() as cursor:
        sql = (
            f'DELETE FROM {TABLE_NAME} '
            'WHERE id = %s'
        )
        cursor.execute(sql, (7,))
        connection.commit()

        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        # for row in cursor.fetchall():
        #     print(row)

    # Editando com UPDATE, WHERE e placeholders no PyMySQL
    with connection.cursor() as cursor:
        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET nome=%s, idade=%s '
            'WHERE id=%s'
        )
        cursor.execute(sql, ("Mariana", 25, 6))
        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        # for row in cursor.fetchall():
        #     _id, name, age = row
        #     print(_id, name, age)

        for row in cursor.fetchall():
            print(row['nome'])
    connection.commit()

#  https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/37412066#questions