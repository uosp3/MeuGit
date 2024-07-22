#https://www.youtube.com/watch?v=OfX_5mpmRm4&list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR&index=49
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

def inserir(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Dados inseridos com sucesso")
    except Error as ex:
        print(ex)
nome=""
while nome!="SAIR":
    nome=input("Digite o nome ou SAIR para finalizar: ")
    if nome!="SAIR":
        telefone=input("Digite o telefone: ")
        email=input("Digite o email: ")
        #sql de inserção...............................
        vsql="Insert into tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO) values('"+nome+"','"+telefone+"','"+email+"')"
        inserir(vcon,vsql)

vcon.close()