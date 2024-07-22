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

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%s, %s) '  # evita mandar dados junto com o comando (injection)
        )
        data = ('Edson*', 62)  # os valores são atribuidos a variável(tupla)
        result = cursor.execute(sql, data)  # a variável é repassada aqui
        print(sql, data)
        print(result)
    connection.commit()

#  https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/37407102#questions/21848100
#  https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/37407102#questions
