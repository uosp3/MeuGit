#https://www.youtube.com/watch?v=lP67hxVNCmo&list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR&index=50
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

#deletar da tabela.................
def deletar(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Dados deletados com sucesso")
    except Error as ex:
        print(ex)

vsql="delete from tb_contatos where N_IDCONTATO=1"
deletar(vcon,vsql)

vcon.close()