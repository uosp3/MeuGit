#https://www.youtube.com/watch?v=TpnDat8ZYWA&list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR&index=52
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

#consultar a tabela.................
def consulta(conexao,sql):
    c=conexao.cursor()
    c.execute(sql)
    resultado=c.fetchall()
    return resultado

vsql="select * from tb_contatos where T_NOMECONTATO like '%i%'"
res=consulta(vcon,vsql)
for r in res:
    print(r)


vcon.close()