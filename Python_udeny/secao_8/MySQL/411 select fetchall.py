# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import os

import pymysql
import dotenv

TABLE_NAME = 'customers'

dotenv.load_dotenv()  # carregar as configurações do .env

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4'
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
        )
        result = cursor.executemany(sql, data4)  # type: ignore
        # print(sql)
        # print(data4)
        # print(result)
    connection.commit()

    # Lendo os valores com SELECT
    with connection.cursor() as cursor:
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
        )
        cursor.execute(sql)
        data5 = cursor.fetchall()

        for row in data5:
            print(row)
#  https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/37407826#questions/22076959
