#https://www.youtube.com/watch?v=-TrS7xM5edk&list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR&index=51
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

#atualizar a tabela.................
def atualizar(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Dados atualizados com sucesso")
    except Error as ex:
        print(ex)

vsql="update tb_contatos set T_NOMECONTATO='Edson G Santos', T_TELEFONECONTATO='(33)99999.11111' where N_IDCONTATO=2"
atualizar(vcon,vsql)

vcon.close()