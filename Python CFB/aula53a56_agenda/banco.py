import sqlite3
from sqlite3 import Error
import os

pastaApp=os.path.dirname(__file__)#pega o caminho do arquivo
nomeBanco=pastaApp+"\\agenda.db"
nomeBanco=nomeBanco.replace("aula53a56_agenda","bancos")#ajuste do caminho
print("caminho do arquivo: ",nomeBanco)
def ConexaoBanco():
    con=None
    try:
        con=sqlite3.connect(nomeBanco)
    except Error as ex:
        print(ex)
    return con

def dql(query): #select -- DQL Data Query Language - Linguagem de Consulta de dados.
    vcon=ConexaoBanco()
    c=vcon.cursor()
    c.execute(query)
    res=c.fetchall()
    vcon.close()
    return res

def dml(query): #insert, update, delete -- DML Data Manipulation Language - Linguagem de Manipulação de Dados.
    try:
        vcon=ConexaoBanco()
        c=vcon.cursor()
        c.execute(query)
        vcon.commit()
        vcon.close()
    except Error as ex:
        print("erro aqui: ", ex)