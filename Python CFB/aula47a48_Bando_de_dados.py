#https://www.youtube.com/watch?v=sItdTqb79Hs&list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR&index=48
import sqlite3
from sqlite3 import Error

def ConexaoBanco():#criar conexão .....................
    caminho="E:\\Cursos\\Tudo\\Python\\banco\\agenda.db"
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon=ConexaoBanco()

#Criar tabela
vsql="""Create table tb_contatos(
            N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
            T_NOMECONTATO VARCHAR(30),
            T_TELEFONECONTATO VARCHAR(14),
            T_EMAILCONTATO VARCHAR(30)
        )"""
def criarTabela(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        print("Tabela criada")
    except Error as ex:
        print(ex)

criarTabela(vcon,vsql)

vcon.close()