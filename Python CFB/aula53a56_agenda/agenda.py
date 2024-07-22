import os
import sqlite3
from sqlite3 import Error

#Conexão
def ConexaoBanco():
    caminho="E:\\Cursos\\Tudo\\Python\\bancos\\agenda.db"
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon=ConexaoBanco()

def query(conexao,sql): #para insert, update e delete
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Operação realizada com sucesso.")
        #conexao.close()

def consultar(conexao,sql):
    c=conexao.cursor()
    c.execute(sql)
    res=c.fetchall() #retorno da consulta
    #conexao.close()
    return res
    
def menuPrincipal():
    os.system('cls')
    print("1 - Inserir Novo Registro")
    print("2 - Deletar Registro")
    print("3 - Atualizar Registro")
    print("4 - Consultar Registros")
    print("5 - Consultar Registro por Nome")
    print("6 - Sair")

def menuInserir():
    os.system("cls")
    vnome=input("Digite o nome: ")
    vtelefone=input("Digite o telefone: ")
    vemail=input("Digite o email: ")
    vsql="insert into tb_contatos (t_nomecontato, t_telefonecontato, t_emailcontato) values ('"+vnome+"','"+vtelefone+"','"+vemail+"')"
    query(vcon,vsql)

def menuDeletar():
    os.system("cls")
    vid=input("Digite o ID do registro a ser deletado: ")
    vsql="delete from tb_contatos where n_idcontato="+vid
    query(vcon,vsql)

def menuAtualizar():
    os.system("cls")
    vid=input("Digite o ID do registro a ser alterado: ")
    r=consultar(vcon,"select * from tb_contatos where n_idcontato="+vid)
    rnome=r[0][1]
    rtelefone=r[0][2]
    remail=r[0][3]
    vnome=input("Digite o nome: ")
    vtelefone=input("Digite o telefone: ")
    vemail=input("Digite o email: ")
    if(len(vnome)==0):
        vnome=rnome
    if(len(vtelefone)==0):
        vtelefone=rtelefone
    if(len(vemail)==0):
        vemail=remail
    vsql="update tb_contatos set t_nomecontato='"+vnome+"', t_telefonecontato='"+vtelefone+"', t_emailcontato='"+vemail+"' where n_idcontato="+vid
    query(vcon,vsql)

def menuConsultar():
    vsql="select * from tb_contatos"
    res=consultar(vcon,vsql)
    vlim=10
    vcont=0
    for r in res:#na linha abaixo {N:.<X}, N=indice do array, o "." é o caractere de preenchimento dos espaços, "<" coloca o texto à esquerda e X é a quantidade de caracteres total de cada campo.
        print("ID: {0:_<3} Nome:{1:.<30} Telefone:{2:.<16} E-mail:{3:.<30}".format(r[0],r[1],r[2],r[3]))
        vcont+=1
        if(vcont>=vlim):
            vcont=0
            os.system("pause")
            os.system("cls")
    print("Fim da lista")
    os.system("pause")


def menuConsultarNomes():
    vnome=input("Digite o nome: ")
    vsql="select * from tb_contatos where t_nomecontato like '%"+vnome+"%'"
    res=consultar(vcon,vsql)
    vlim=10
    vcont=0
    for r in res:#na linha abaixo {N:.<X}, N=indice do array, o "." é o caractere de preenchimento dos espaços, "<" coloca o texto à esquerda e X é a quantidade de caracteres total de cada campo.
        print("ID: {0:_<3} Nome:{1:.<30} Telefone:{2:.<16} E-mail:{3:.<30}".format(r[0],r[1],r[2],r[3]))
        vcont+=1
        if(vcont>=vlim):
            vcont=0
            os.system("pause")
            os.system("cls")
    print("Fim da lista")
    os.system("pause")

opc=0
while opc != 6:
    menuPrincipal()
    opc=int(input("Digite uma opção: "))
    if opc==1:
        menuInserir()
    elif opc ==2:
        menuDeletar()
    elif opc ==3:
        menuAtualizar()
    elif opc ==4:
        menuConsultar()
    elif opc ==5:
        menuConsultarNomes()
    elif opc ==6:
        os.system("cls")
        print("Fim do programa")
    else:
        os.system("cls")
        print("Opção inválida")
        os.system("pause")

vcon.close()
os.system("pause")